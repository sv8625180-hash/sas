from contextlib import asynccontextmanager, redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import socket
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

import anyio
from mcp.types import CallToolResult, ListToolsResult, TextContent, Tool

SCRIPTS = Path(__file__).resolve().parents[1] / "tools/hoplite-research/scripts"
sys.path.insert(0, str(SCRIPTS))

import research_client
import research_mcp
from mcp_runtime import POLICY_BLOCKED, SERVERS


def result(text="Source text", *, error=False, structured=None):
    return CallToolResult(
        content=[TextContent(type="text", text=text)], isError=error, structuredContent=structured,
    )


def session_for(name, response=None):
    return SimpleNamespace(
        list_tools=AsyncMock(return_value=ListToolsResult(tools=[
            Tool(name=tool, inputSchema={}) for tool in SERVERS[name]["tools"]
        ])),
        call_tool=AsyncMock(return_value=response),
    )


def connection(session):
    @asynccontextmanager
    async def connect(name):
        yield session
    return connect


class BridgePolicyTests(unittest.IsolatedAsyncioTestCase):
    async def test_private_url_returns_policy_marker_without_calling_upstream(self):
        upstream = SimpleNamespace(call_tool=AsyncMock())
        addresses = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 80))]
        with patch("mcp_runtime.socket.getaddrinfo", return_value=addresses):
            response = await research_mcp.guarded_call(
                upstream, "fetch", "fetch", {"url": "http://127.0.0.1/"}
            )
        self.assertTrue(response.isError)
        self.assertTrue(response.content[0].text.startswith(f"{POLICY_BLOCKED} "))
        upstream.call_tool.assert_not_called()

    async def test_disallowed_tool_never_reaches_upstream(self):
        upstream = SimpleNamespace(call_tool=AsyncMock())
        response = await research_mcp.guarded_call(upstream, "fetch", "execute_code", {})
        self.assertTrue(response.isError)
        self.assertIn(POLICY_BLOCKED, response.content[0].text)
        upstream.call_tool.assert_not_called()

    async def test_upstream_errors_are_not_relabelled_as_policy_blocks(self):
        failure = result("Connection refused", error=True)
        upstream = SimpleNamespace(call_tool=AsyncMock(return_value=failure))
        with patch("research_mcp.validate_call"):
            response = await research_mcp.guarded_call(upstream, "fetch", "fetch", {})
        self.assertIs(response, failure)
        self.assertNotIn(POLICY_BLOCKED, response.content[0].text)
        upstream.call_tool.assert_awaited_once_with("fetch", {})

    async def test_upstream_value_error_is_outside_policy_handler(self):
        upstream = SimpleNamespace(call_tool=AsyncMock(side_effect=ValueError("upstream failure")))
        with patch("research_mcp.validate_call"), self.assertRaisesRegex(ValueError, "^upstream failure$"):
            await research_mcp.guarded_call(upstream, "fetch", "fetch", {})

    async def test_dns_failure_is_not_a_policy_block(self):
        upstream = SimpleNamespace(call_tool=AsyncMock())
        with patch("mcp_runtime.socket.getaddrinfo", side_effect=socket.gaierror("synthetic DNS failure")):
            with self.assertRaises(socket.gaierror):
                await research_mcp.guarded_call(upstream, "fetch", "fetch", {"url": "https://example.com"})
        upstream.call_tool.assert_not_called()


class EnvelopeTests(unittest.TestCase):
    def test_structured_failure_overrides_nonempty_text(self):
        with self.assertRaises(RuntimeError):
            research_client.checked_text(result(structured={"success": False, "error": "rate limited"}))

    def test_known_nested_failure_envelopes_in_text_and_structured_content(self):
        envelopes = [
            {"data": {"success": False}},
            {"result": {"status": "failed"}},
            {"metadata": {"statusCode": 429}},
            {"data": {"result": {"metadata": {"statusCode": "503"}}}},
            {"result": [{"metadata": {"http_status": 403}}]},
            {"data": {"status_code": 401}},
        ]
        for envelope in envelopes:
            for response in [result(json.dumps(envelope)), result(structured=envelope)]:
                with self.subTest(envelope=envelope, structured=response.structuredContent is not None):
                    with self.assertRaises(RuntimeError):
                        research_client.checked_text(response)

    def test_source_text_and_unrecognized_payloads_are_not_keyword_scanned(self):
        source = 'Documentation explains Error: forbidden, rate_limited and HTTP 429, not a failed request.'
        envelope = {
            "success": True,
            "data": {"markdown": source, "metadata": {"statusCode": 200}},
            "page": {"error": "A quoted source field", "statusCode": 429},
        }
        self.assertEqual(research_client.checked_text(result(source, structured=envelope)), source)
        self.assertEqual(research_client.checked_text(result(json.dumps(envelope))), json.dumps(envelope))


class VerificationPhaseTests(unittest.IsolatedAsyncioTestCase):
    async def test_transport_error_cannot_certify_private_url_guard(self):
        for response in [result("Connection refused", error=True), result(f"{POLICY_BLOCKED} quoted text")]:
            session = session_for("fetch", response)
            with self.subTest(response=response), patch("research_client.connect", side_effect=connection(session)):
                report = await research_client.check(False, ["fetch"])
            self.assertFalse(report["passed"])
            self.assertNotIn("private_url_rejected", report["servers"]["fetch"])
            self.assertIn("Private-URL guard failed", report["servers"]["fetch"]["error"])

    async def test_policy_marker_certifies_only_the_guard(self):
        session = session_for("fetch", result(f"{POLICY_BLOCKED} Private address", error=True))
        with patch("research_client.connect", side_effect=connection(session)):
            report = await research_client.check(False, ["fetch"])
        evidence = report["servers"]["fetch"]
        self.assertTrue(report["passed"])
        self.assertTrue(evidence["private_url_rejected"])
        self.assertEqual(evidence["functional_status"], "not_checked")
        self.assertEqual(evidence["native_discovery"], "not_checked")

    async def test_catalog_success_does_not_claim_functional_or_native_success(self):
        session = session_for("context7")
        with patch("research_client.connect", side_effect=connection(session)):
            report = await research_client.check(False, ["context7"])
        evidence = report["servers"]["context7"]
        self.assertTrue(report["passed"])
        self.assertTrue(evidence["initialized"])
        self.assertTrue(evidence["catalog_matches"])
        self.assertEqual(evidence["functional_status"], "not_checked")
        self.assertEqual(evidence["native_discovery"], "not_checked")
        self.assertNotIn("live_assertion", evidence)
        session.call_tool.assert_not_called()

    async def test_functional_success_still_does_not_claim_native_discovery(self):
        session = session_for("context7", result("Context7-compatible library ID: MCP Python SDK"))
        with patch("research_client.connect", side_effect=connection(session)):
            report = await research_client.check(True, ["context7"])
        self.assertTrue(report["passed"])
        self.assertEqual(report["servers"]["context7"]["functional_status"], "passed")
        self.assertEqual(report["servers"]["context7"]["native_discovery"], "not_checked")

    async def test_functional_failure_preserves_successful_catalog_evidence(self):
        session = session_for("context7", result(
            "Context7-compatible library ID: MCP Python SDK", structured={"metadata": {"statusCode": 429}},
        ))
        with patch("research_client.connect", side_effect=connection(session)):
            report = await research_client.check(True, ["context7"])
        evidence = report["servers"]["context7"]
        self.assertFalse(report["passed"])
        self.assertTrue(evidence["catalog_matches"])
        self.assertEqual(evidence["functional_status"], "failed")
        self.assertEqual(evidence["native_discovery"], "not_checked")


class ClientTimeoutTests(unittest.IsolatedAsyncioTestCase):
    async def test_validation_runs_off_the_event_loop_before_connecting(self):
        event_loop_thread = threading.get_ident()
        validation_threads = []
        session = session_for("fetch", result())

        def validate(*args):
            validation_threads.append(threading.get_ident())

        @asynccontextmanager
        async def connect(name):
            self.assertEqual(len(validation_threads), 1)
            yield session

        with patch("research_client.validate_call", side_effect=validate), patch("research_client.connect", connect):
            self.assertEqual(await research_client.call("fetch", "fetch", {}), "Source text")
        self.assertNotEqual(validation_threads, [event_loop_thread])

    async def test_worker_wait_is_inside_timeout_and_does_not_connect(self):
        fail_after = anyio.fail_after

        async def pending_validation(*args, **kwargs):
            await anyio.sleep_forever()

        with patch("research_client.anyio.fail_after", side_effect=lambda seconds: fail_after(0.02)) as deadline:
            with patch("research_client.anyio.to_thread.run_sync", side_effect=pending_validation) as worker:
                with patch("research_client.connect") as connect, self.assertRaises(TimeoutError):
                    await research_client.call("fetch", "fetch", {})
        deadline.assert_called_once_with(125)
        worker.assert_awaited_once_with(research_client.validate_call, "fetch", "fetch", {}, abandon_on_cancel=True)
        connect.assert_not_called()

    async def test_validation_failure_never_connects(self):
        with patch("research_client.validate_call", side_effect=ValueError("policy rejected")):
            with patch("research_client.connect") as connect, self.assertRaisesRegex(ValueError, "policy rejected"):
                await research_client.call("fetch", "fetch", {})
        connect.assert_not_called()


class ReportHistoryTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        patcher = patch("research_client.PROJECT_ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.history = self.root / ".research/checks"
        self.output = self.root / "verification.json"
        self.failure = {"checked_at": "2026-09-16T00:00:00+00:00", "live": True, "passed": False,
                        "servers": {"fetch": {"status": "failed", "error": "synthetic failure"}}}

    def test_partial_catalog_view_cannot_erase_dated_functional_failure(self):
        partial = {"live": False, "passed": True, "servers": {"context7": {"catalog_matches": True}}}
        with patch("research_client.datetime") as clock:
            clock.now.return_value = datetime(2026, 9, 16, tzinfo=timezone.utc)
            first = research_client.write_report(self.failure, self.output)
            second = research_client.write_report(partial, self.output)
        self.assertNotEqual(first, second)
        self.assertEqual(len(list(self.history.glob("20260916T*.json"))), 2)
        self.assertEqual(json.loads(first.read_text()), self.failure)
        self.assertEqual(json.loads(second.read_text()), partial)
        self.assertEqual(json.loads(self.output.read_text()), partial)

    def test_archive_survives_view_write_failure(self):
        self.output.mkdir()
        with self.assertRaises(IsADirectoryError):
            research_client.write_report(self.failure, self.output)
        archives = list(self.history.glob("*.json"))
        self.assertEqual(len(archives), 1)
        self.assertEqual(json.loads(archives[0].read_text()), self.failure)

    def test_output_cannot_overwrite_history(self):
        archive = research_client.write_report(self.failure, self.output)
        with self.assertRaisesRegex(ValueError, "preserved check history"):
            research_client.write_report({"passed": True}, archive)
        self.assertEqual(json.loads(archive.read_text()), self.failure)

    def test_cli_archives_even_with_an_explicit_output_view(self):
        arguments = ["research_client", "check", "--server", "fetch", "--output", str(self.output)]
        with patch.object(sys, "argv", arguments), patch("research_client.check", new_callable=AsyncMock) as check:
            check.return_value = self.failure
            with redirect_stdout(io.StringIO()), patch("research_client.connect") as connect:
                self.assertEqual(research_client.main(), 1)
        check.assert_awaited_once_with(False, ["fetch"])
        connect.assert_not_called()
        self.assertEqual(len(list(self.history.glob("*.json"))), 1)
        self.assertEqual(json.loads(self.output.read_text()), self.failure)


if __name__ == "__main__":
    unittest.main()

"""Check or call the configured MCPs before a new Hoplite run discovers them."""

import argparse
from contextlib import AsyncExitStack, asynccontextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4

import anyio
import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamablehttp_client

from mcp_runtime import POLICY_BLOCKED, PROJECT_ROOT, SERVERS, isolated_environment, validate_call


def public_http_client(**kwargs):
    return httpx.AsyncClient(**{**kwargs, "trust_env": False, "follow_redirects": False})


@asynccontextmanager
async def connect(name):
    settings = json.loads((PROJECT_ROOT / ".hoplite" / "settings.json").read_text())
    record = next(item for item in settings["mcpServers"] if item["name"] == f"research-{name}")
    if not record.get("enabled", True):
        raise ValueError("This MCP is disabled in the project configuration")
    config = record["config"]
    async with AsyncExitStack() as stack:
        if config["transport"] == "http":
            if config["url"] != SERVERS[name].get("url"):
                raise ValueError("Remote URL differs from the reviewed provider endpoint")
            reader, writer, _ = await stack.enter_async_context(streamablehttp_client(
                config["url"], httpx_client_factory=public_http_client,
            ))
        else:
            params = StdioServerParameters(
                command=config["command"], args=config["args"], cwd=str(PROJECT_ROOT),
                env=isolated_environment(),
            )
            reader, writer = await stack.enter_async_context(stdio_client(params))
        session = await stack.enter_async_context(ClientSession(reader, writer))
        with anyio.fail_after(35):
            await session.initialize()
        yield session


def _check_response_envelope(data):
    if isinstance(data, list):
        for item in data:
            _check_response_envelope(item)
    elif isinstance(data, dict):
        status = str(data.get("status", "")).strip().lower()
        codes = [data.get(key) for key in ("http_status", "statusCode", "status_code")]
        failed_http = any(
            (type(code) is int and code >= 400)
            or (isinstance(code, str) and len(code) == 3 and code.isdecimal() and int(code) >= 400)
            for code in codes
        )
        if (status in {"error", "failed", "rate_limited", "unauthorized", "forbidden"}
                or data.get("error") or data.get("success") is False or failed_http):
            reason = "error field" if data.get("error") else "success=false"
            if status in {"error", "failed", "rate_limited", "unauthorized", "forbidden"}:
                reason = f"status={status}"
            if failed_http:
                reason = "HTTP " + ", ".join(
                    str(code) for code in codes
                    if (type(code) is int and code >= 400)
                    or (isinstance(code, str) and len(code) == 3 and code.isdecimal() and int(code) >= 400)
                )
            raise RuntimeError(f"The source reported a failure or access limit inside its response ({reason})")
        for key in ("data", "result", "metadata"):
            _check_response_envelope(data.get(key))


def checked_text(result):
    texts = [part.text for part in result.content if part.type == "text"]
    text = "\n".join(texts)
    if result.isError or not text.strip() or text.lstrip().startswith("Error:"):
        raise RuntimeError(text or "Tool returned an empty or failed result")
    _check_response_envelope(result.structuredContent)
    for part in texts:
        try:
            data = json.loads(part)
        except json.JSONDecodeError:
            continue
        _check_response_envelope(data)
    return text


def error_summary(error):
    if isinstance(error, BaseExceptionGroup):
        return "; ".join(error_summary(child) for child in error.exceptions)
    return f"{type(error).__name__}: {error}"


async def check(live, selected=None):
    if selected and set(selected) - SERVERS.keys():
        raise ValueError("Unknown MCP selection")
    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(), "live": live,
        "scope": "Requested project-transport smoke tests, not every tool or account-wide availability; catalog success does not establish functional or native availability",
        "servers": {},
    }
    for name, definition in SERVERS.items():
        if selected and name not in selected:
            continue
        evidence = report["servers"][name] = {
            "status": "failed", "functional_status": "not_checked", "native_discovery": "not_checked",
        }
        try:
            with anyio.fail_after(125):
                async with connect(name) as session:
                    evidence["initialized"] = True
                    catalog = await session.list_tools()
                    names = {tool.name for tool in catalog.tools}
                    if names != definition["tools"]:
                        raise RuntimeError("Advertised tools differ from the audited allowlist")
                    evidence["tools"] = sorted(names)
                    evidence["catalog_matches"] = True
                    if name == "fetch":
                        blocked = await session.call_tool("fetch", {"url": "http://127.0.0.1/"})
                        if not blocked.isError or not any(
                            part.type == "text" and part.text.startswith(f"{POLICY_BLOCKED} ")
                            for part in blocked.content
                        ):
                            raise RuntimeError("Private-URL guard failed")
                        evidence["private_url_rejected"] = True
                    elif name == "arxiv":
                        checked_text(await session.call_tool("list_papers", {}))
                    if live:
                        evidence["functional_status"] = "failed"
                        if name == "fetch":
                            text = checked_text(await session.call_tool(
                                "fetch", {"url": "https://example.com", "max_length": 2000}
                            ))
                            if "This domain is for use in documentation examples" not in text:
                                raise RuntimeError("The real webpage did not contain the expected body text")
                            evidence["live_assertion"] = "example.com retrieved and its real body text extracted"
                        elif name == "arxiv":
                            text = checked_text(await session.call_tool("search_papers", {
                                "query": 'ti:"Attention Is All You Need"', "max_results": 2,
                            }))
                            if "Attention Is All You Need" not in text:
                                raise RuntimeError("arXiv did not return the expected real paper")
                            evidence["live_assertion"] = "arXiv search returned Attention Is All You Need"
                        elif name == "context7":
                            text = checked_text(await session.call_tool("resolve-library-id", {
                                "libraryName": "python mcp sdk",
                                "query": "Official Python MCP SDK streamable HTTP client public documentation",
                            }))
                            if "Context7-compatible library ID:" not in text or "MCP Python SDK" not in text:
                                raise RuntimeError("Context7 did not return the expected library metadata")
                            evidence["live_assertion"] = "Context7 resolved real MCP Python SDK documentation"
                        elif name == "firecrawl":
                            text = checked_text(await session.call_tool("firecrawl_scrape", {
                                "url": "https://example.com", "formats": ["markdown"],
                                "onlyMainContent": True,
                            }))
                            if "Example Domain" not in text or "documentation examples" not in text:
                                raise RuntimeError("Firecrawl did not return the expected public page body")
                            evidence["live_assertion"] = "Firecrawl keyless returned example.com content; it may be cached"
                        else:
                            raise RuntimeError("No live assertion is defined for this server")
                        evidence["functional_status"] = "passed"
                    evidence["status"] = "passed"
        except Exception as exc:
            evidence["error"] = error_summary(exc)
    report["passed"] = all(item["status"] == "passed" for item in report["servers"].values())
    return report


async def call(name, tool, arguments):
    with anyio.fail_after(125):
        await anyio.to_thread.run_sync(
            validate_call, name, tool, arguments, abandon_on_cancel=True
        )
        async with connect(name) as session:
            return checked_text(await session.call_tool(tool, arguments))


def write_report(report, output):
    history = PROJECT_ROOT / ".research" / "checks"
    history.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    archive = history / f"{stamp}-{uuid4().hex}.json"
    data = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    with archive.open("x", encoding="utf-8") as file:
        file.write(data)
    output = Path(output)
    if output.resolve().is_relative_to(history.resolve()):
        raise ValueError("--output must be outside the preserved check history")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(data, encoding="utf-8")
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check_parser = commands.add_parser("check", help="Initialize each server and verify its tools")
    check_parser.add_argument("--live", action="store_true", help="Also verify real content from selected public sources")
    check_parser.add_argument("--server", action="append", choices=SERVERS, help="Check only this server; repeat to select more")
    check_parser.add_argument("--output", default=".research/verification.json")
    call_parser = commands.add_parser("call", help="Call one installed capability")
    call_parser.add_argument("server", choices=SERVERS)
    call_parser.add_argument("tool")
    call_parser.add_argument("--arguments", required=True, help="JSON object; never include secrets")
    args = parser.parse_args()
    if args.command == "check":
        report = anyio.run(check, args.live, args.server)
        write_report(report, args.output)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["passed"] else 1
    arguments = json.loads(args.arguments)
    if not isinstance(arguments, dict):
        parser.error("--arguments must be a JSON object")
    print(anyio.run(call, args.server, args.tool, arguments))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

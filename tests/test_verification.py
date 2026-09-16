import asyncio
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "scripts"), str(ROOT / "tools/hoplite-research/scripts")]

from mcp.types import CallToolResult, TextContent
from research_client import check, checked_text, error_summary
from verify_toolkit import verify


class ResultTests(unittest.TestCase):
    def test_real_text_passes(self):
        result = CallToolResult(content=[TextContent(type="text", text="Actual page text")])
        self.assertEqual(checked_text(result), "Actual page text")

    def test_semantic_errors_cannot_pass_as_http_success(self):
        payloads = ["", " ", "Error: throttled", '{"status":"rate_limited"}',
                    '{"http_status":429}', '{"success":false}', '{"error":"unauthorized"}']
        for payload in payloads:
            with self.subTest(payload=payload), self.assertRaises(RuntimeError):
                checked_text(CallToolResult(content=[TextContent(type="text", text=payload)]))
        with self.assertRaises(RuntimeError):
            checked_text(CallToolResult(isError=True, content=[TextContent(type="text", text="looks normal")]))

    def test_exception_groups_keep_failure_context(self):
        error = ExceptionGroup("transport", [RuntimeError("rate limited"), ValueError("schema changed")])
        self.assertIn("rate limited", error_summary(error))
        self.assertIn("schema changed", error_summary(error))

    def test_no_vacuous_success_for_unknown_selection(self):
        with self.assertRaises(ValueError):
            asyncio.run(check(False, ["missing-server"]))


class IntegrityTests(unittest.TestCase):
    def test_all_imported_skills_and_dependencies_match(self):
        report = verify()
        self.assertEqual(report["imported_skills_verified"], 26)
        self.assertEqual(report["skills_verified"], 27)

    def test_unregistered_root_cannot_be_activated_silently(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for relative in [".agents", "docs/provenance"]:
                shutil.copytree(ROOT / relative, root / relative)
            path = root / ".agents/skills/unreviewed/SKILL.md"
            path.parent.mkdir()
            path.write_text("Unreviewed instructions")
            with self.assertRaisesRegex(ValueError, "Unregistered"):
                verify(root)

    def test_mutated_skill_is_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for relative in [".agents", "docs/provenance"]:
                shutil.copytree(ROOT / relative, root / relative)
            manifest = json.loads((root / "docs/provenance/skills-export-manifest.json").read_text())
            path = root / ".agents/skills" / manifest["skills"][0]["path"]
            path.write_text(path.read_text() + "\nUnreviewed modification\n")
            with self.assertRaisesRegex(ValueError, "changed skill hash"):
                verify(root)


if __name__ == "__main__":
    unittest.main()

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_upstreams import AccessLimited, check_sources, inventory, parse_source

PIN = "a" * 40
HEAD = "b" * 40


class UpstreamTests(unittest.TestCase):
    def test_source_urls_require_immutable_public_refs(self):
        self.assertEqual(parse_source(f"https://github.com/owner/repo/blob/{PIN}/skills/test/SKILL.md"),
                         ("owner/repo", PIN, "skills/test/SKILL.md"))
        for url in ["https://example.com/skill", "file:///tmp/skill",
                    "https://raw.githubusercontent.com/owner/repo/main/SKILL.md",
                    f"https://github.com/owner/repo/blob/{PIN}/../secret",
                    f"https://user:pass@github.com/owner/repo/blob/{PIN}/SKILL.md"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                parse_source(url)

    def test_inventory_covers_imported_sources_and_local_skills(self):
        sources, local = inventory()
        names = set(local).union(*(set(value) for value in sources.values()))
        self.assertIn("ai-opportunity-validation", names)
        self.assertIn("copywriting", names)
        self.assertGreaterEqual(len(names), 26)

    def test_changed_source_is_only_an_advisory(self):
        def reader(url):
            if url.endswith("/repos/owner/repo"):
                return json.dumps({"default_branch": "main"}).encode()
            if "/git/ref/" in url:
                return json.dumps({"object": {"type": "commit", "sha": HEAD}}).encode()
            return b"old instructions" if PIN in url else b"unreviewed instructions"

        with patch("check_upstreams.inventory", return_value=({("owner/repo", PIN, "SKILL.md"): {"test"}}, [])):
            report = check_sources(reader=reader)
        self.assertTrue(report["passed"])
        self.assertTrue(report["needs_review"])
        self.assertEqual(report["sources"][0]["status"], "changed_review_required")
        self.assertNotIn("unreviewed instructions", json.dumps(report))

    def test_rate_limit_stops_all_further_requests(self):
        calls = []

        def reader(url):
            calls.append(url)
            raise AccessLimited("HTTP 429; no retry")

        sources = {("owner/one", PIN, "SKILL.md"): {"one"}, ("owner/two", PIN, "SKILL.md"): {"two"}}
        with patch("check_upstreams.inventory", return_value=(sources, [])):
            report = check_sources(reader=reader)
        self.assertFalse(report["passed"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(report["sources"][1]["status"], "not_checked_due_to_limit")


if __name__ == "__main__":
    unittest.main()

import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from uuid import uuid4
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from exportar_kit import (MANIFEST, PREFIX, STATIC_FILES, archive_bytes, build,
                          check, payload, verify_directory)


class PortableBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        for name in STATIC_FILES:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        shutil.copytree(ROOT / ".agents", self.root / ".agents")

    def extract(self):
        destination = Path(self.temp.name) / "extracted"
        with zipfile.ZipFile(io.BytesIO(archive_bytes(self.root))) as archive:
            archive.extractall(destination)
        return destination / PREFIX

    def test_all_skills_mcp_and_hidden_configuration_are_included(self):
        files = payload(self.root)
        inventory = json.loads(files[MANIFEST])
        self.assertEqual(len(inventory["skills"]), 27)
        self.assertEqual(inventory["original_skill_count"], 26)
        self.assertEqual(inventory["additional_skills"], ["cohort-analysis"])
        self.assertEqual(len(inventory["mcp_servers"]), 4)
        guide = files["LEEME-PRIMERO.md"].decode()
        for name in inventory["skills"]:
            self.assertIn(f"`{name}`", guide)
        for server in inventory["mcp_servers"]:
            self.assertIn(f"`{server['name']}`", guide)
        for name in (".hoplite/settings.json", ".hoplite/setup.sh", ".github/dependabot.yml",
                     "tools/hoplite-research/uv.lock", "tools/personal-skills/package-lock.json"):
            self.assertIn(name, inventory["files"])
        self.assertEqual(files["README.md"], files["LEEME-PRIMERO.md"])
        self.assertEqual(len([name for name in files if name.endswith("/SKILL.md")]), 27)

    def test_export_is_reproducible_and_has_safe_unique_paths(self):
        first = archive_bytes(self.root)
        self.assertEqual(first, archive_bytes(self.root))
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            for info in archive.infolist():
                self.assertTrue(info.filename.startswith(f"{PREFIX}/"))
                self.assertNotIn("..", Path(info.filename).parts)
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual((info.external_attr >> 16) & 0o170000, 0o100000)

    def test_unlisted_runtime_credentials_and_history_never_enter_archive(self):
        marker = f"private-test-{uuid4().hex}"
        excluded = (".env", ".hoplite/attachments/original.zip", ".hoplite/runtime/session.json",
                    ".git/config", ".research/checks/history.json", "reports/mcp-health.json",
                    "tools/personal-skills/node_modules/private.js",
                    "tools/hoplite-research/.venv/credentials", "docs/research/private.md")
        for name in excluded:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(marker)
        with zipfile.ZipFile(io.BytesIO(archive_bytes(self.root))) as archive:
            for name in archive.namelist():
                self.assertNotIn(marker, archive.read(name).decode())
            for name in excluded:
                self.assertNotIn(f"{PREFIX}/{name}", archive.namelist())

    def test_clean_extraction_verifies_without_source_repository_or_dependencies(self):
        root = self.extract()
        self.assertFalse((root / ".git").exists())
        self.assertFalse((root / "tools/hoplite-research/.venv").exists())
        result = verify_directory(root)
        self.assertEqual(result["skills_verified"], 27)
        self.assertEqual(result["mcp_configured"], 4)
        self.assertFalse(result["personal_library_imported"])
        self.assertFalse(result["live_mcp_checked"])

    def test_export_cannot_leak_new_configuration_secrets(self):
        path = self.root / ".hoplite/settings.json"
        settings = json.loads(path.read_text())
        settings["mcpServers"][-1]["config"]["headers"] = {"Authorization": "PRIVATE_TEST_VALUE"}
        path.write_text(json.dumps(settings))
        with self.assertRaisesRegex(ValueError, "credential-free") as caught:
            archive_bytes(self.root)
        self.assertNotIn("PRIVATE_TEST_VALUE", str(caught.exception))

    def test_changed_remote_endpoint_is_rejected(self):
        path = self.root / ".hoplite/settings.json"
        settings = json.loads(path.read_text())
        settings["mcpServers"][-1]["config"]["url"] += "?token=PRIVATE_TEST_VALUE"
        path.write_text(json.dumps(settings))
        with self.assertRaisesRegex(ValueError, "credential-free"):
            archive_bytes(self.root)

    def test_missing_server_is_not_presented_as_a_complete_kit(self):
        path = self.root / ".hoplite/settings.json"
        settings = json.loads(path.read_text())
        settings["mcpServers"].pop()
        path.write_text(json.dumps(settings))
        with self.assertRaisesRegex(ValueError, "four MCP"):
            archive_bytes(self.root)

    def test_changed_skill_is_rejected(self):
        path = self.root / ".agents/skills/cohort-analysis/SKILL.md"
        path.write_text(path.read_text() + "\nUnreviewed change\n")
        with self.assertRaisesRegex(ValueError, "changed skill hash"):
            archive_bytes(self.root)

    def test_unregistered_skill_is_not_silently_omitted(self):
        path = self.root / ".agents/skills/unreviewed/SKILL.md"
        path.parent.mkdir()
        path.write_text("Unreviewed")
        with self.assertRaisesRegex(ValueError, "Unregistered"):
            archive_bytes(self.root)

    def test_symlinked_source_is_rejected(self):
        path = self.root / "AGENTS.md"
        outside = Path(self.temp.name) / "private.txt"
        outside.write_text("PRIVATE_TEST_VALUE")
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            archive_bytes(self.root)

    def test_missing_required_file_prevents_incomplete_delivery(self):
        (self.root / "tools/hoplite-research/uv.lock").unlink()
        with self.assertRaises(FileNotFoundError):
            archive_bytes(self.root)

    def test_changed_file_in_extraction_fails_manifest_verification(self):
        root = self.extract()
        path = root / "AGENTS.md"
        path.write_text(path.read_text() + "\nUnexpected change\n")
        with self.assertRaisesRegex(ValueError, "inventory"):
            verify_directory(root)

    def test_changed_manifest_fails_verification(self):
        root = self.extract()
        (root / MANIFEST).write_text("{}")
        with self.assertRaisesRegex(ValueError, "inventory"):
            verify_directory(root)

    def test_changed_portable_readme_fails_verification(self):
        root = self.extract()
        (root / "README.md").write_text("Unexpected instructions")
        with self.assertRaisesRegex(ValueError, "inventory"):
            verify_directory(root)

    def test_archive_and_external_checksum_are_checked(self):
        archive = Path(self.temp.name) / "kit.zip"
        result = build(self.root, archive)
        self.assertGreater(result["bytes"], 0)
        self.assertTrue(check(self.root, archive)["archive_matches_sources"])
        archive.with_suffix(".zip.sha256").write_text("incorrect")
        with self.assertRaisesRegex(ValueError, "checksum"):
            check(self.root, archive)
        archive.write_bytes(b"incorrect")
        with self.assertRaisesRegex(ValueError, "differs"):
            check(self.root, archive)

    def test_output_symlink_cannot_overwrite_another_file(self):
        archive = Path(self.temp.name) / "kit.zip"
        outside = Path(self.temp.name) / "private.txt"
        outside.write_text("Keep me")
        archive.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            build(self.root, archive)
        self.assertEqual(outside.read_text(), "Keep me")


if __name__ == "__main__":
    unittest.main()

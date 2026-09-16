import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("node"), "Node.js is required for the installer tests")
class PersonalInstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.home = Path(self.temp.name) / "home"
        self.home.mkdir()
        for relative in [".agents", "docs/provenance"]:
            shutil.copytree(ROOT / relative, self.root / relative)
        self.installer = self.root / "tools/personal-skills/instalar.mjs"
        self.installer.parent.mkdir(parents=True)
        shutil.copyfile(ROOT / "tools/personal-skills/instalar.mjs", self.installer)

    def run_installer(self, action="preparar"):
        return subprocess.run(["node", str(self.installer), action], text=True, capture_output=True,
                              env={**os.environ, "HOME": str(self.home)}, timeout=30)

    def test_prepare_is_idempotent_and_explicitly_local(self):
        first = self.run_installer()
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertIn("27/27", first.stdout)
        self.assertIn("NO ha importado", first.stdout)
        second = self.run_installer()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("Archivos nuevos: 0", second.stdout)

    def test_collision_aborts_before_copying_any_other_skill(self):
        path = self.home / ".agents/skills/web-search-strategy/SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("Existing user work")
        result = self.run_installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("DISTINTA", result.stderr)
        self.assertEqual(len(list((self.home / ".agents/skills").glob("*/SKILL.md"))), 1)
        self.assertEqual(path.read_text(), "Existing user work")

    def test_symlink_destination_is_rejected(self):
        target = self.home / "outside"
        target.mkdir()
        (self.home / ".agents").symlink_to(target, target_is_directory=True)
        result = self.run_installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("simbólicos", result.stderr)
        self.assertFalse((target / "skills").exists())

    def test_hash_mismatch_copies_nothing(self):
        path = self.root / ".agents/skills/ai-opportunity-validation/SKILL.md"
        path.write_text("Tampered")
        result = self.run_installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Hash incorrecto", result.stderr)
        self.assertFalse((self.home / ".agents").exists())

    def test_duplicate_manifest_name_is_rejected(self):
        path = self.root / "docs/provenance/skills-export-manifest.json"
        manifest = json.loads(path.read_text())
        manifest["skills"].append(manifest["skills"][0])
        path.write_text(json.dumps(manifest))
        result = self.run_installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicado", result.stderr)


if __name__ == "__main__":
    unittest.main()

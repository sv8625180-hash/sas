from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools/hoplite-research/scripts"))
import prepare_readability


class ReaderPreparationTests(unittest.TestCase):
    def test_readiness_fingerprint_includes_manifest_and_lockfile(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            manifest = root / "package.json"
            lock = root / "package-lock.json"
            stamp = root / "readability.sha256"
            manifest.write_text('{"dependencies":{"example":"1.0.0"}}')
            lock.write_text('{"lockfileVersion":3}')
            for name in ["jsdom", "@mozilla/readability", "minimist"]:
                (root / "javascript/node_modules" / name).mkdir(parents=True)
            with patch.multiple(prepare_readability, MANIFEST=manifest, LOCKFILE=lock, STAMP=stamp):
                with patch.object(prepare_readability, "javascript_directory", return_value=root / "javascript"):
                    initial = prepare_readability.dependency_fingerprint()
                    stamp.write_text(initial)
                    prepare_readability.verify_ready()
                    manifest.write_text('{"dependencies":{"example":"2.0.0"}}')
                    self.assertNotEqual(initial, prepare_readability.dependency_fingerprint())
                    with self.assertRaises(RuntimeError):
                        prepare_readability.verify_ready()


if __name__ == "__main__":
    unittest.main()

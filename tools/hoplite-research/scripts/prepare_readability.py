"""Prepare Readability.js during setup, never inside the MCP protocol stream."""

import hashlib
from importlib.util import find_spec
from pathlib import Path
import shutil
import subprocess

from mcp_runtime import ROOT, isolated_environment

LOCKFILE = ROOT / ".hoplite" / "readability" / "package-lock.json"
MANIFEST = LOCKFILE.with_name("package.json")
STAMP = ROOT / ".research" / "readability.sha256"


def javascript_directory():
    spec = find_spec("readabilipy")
    if spec is None or spec.origin is None:
        raise RuntimeError("Run the project setup to install ReadabiliPy")
    return Path(spec.origin).parent / "javascript"


def dependency_fingerprint():
    return hashlib.sha256(MANIFEST.read_bytes() + b"\0" + LOCKFILE.read_bytes()).hexdigest()


def verify_ready():
    expected = dependency_fingerprint()
    modules = javascript_directory() / "node_modules"
    if (not STAMP.is_file() or STAMP.read_text().strip() != expected
            or not all((modules / name).is_dir() for name in ["jsdom", "@mozilla/readability", "minimist"])):
        raise RuntimeError("Reader dependencies are not prepared. Run: bash .hoplite/setup.sh")


def prepare():
    directory = javascript_directory()
    # Do not mutate a file that uv may have hard-linked to its package cache.
    for source in (MANIFEST, LOCKFILE):
        target = directory / source.name
        target.unlink(missing_ok=True)
        shutil.copyfile(source, target)
    environment = isolated_environment()
    environment["npm_config_userconfig"] = "/dev/null"
    environment["npm_config_update_notifier"] = "false"
    subprocess.run([
        "npm", "ci", "--prefix", str(directory), "--ignore-scripts", "--omit=dev",
        "--no-audit", "--no-fund", "--engine-strict", "--registry=https://registry.npmjs.org",
        "--cache", str(ROOT / ".research" / "npm-cache"),
    ], check=True, env=environment)
    from mcp_server_fetch.server import extract_content_from_html
    html = "<html><body><article><h1>Reader check</h1><p>Research reader setup verification.</p></article></body></html>"
    if "Research reader setup verification" not in extract_content_from_html(html):
        raise RuntimeError("The offline HTML extraction check failed")
    STAMP.write_text(dependency_fingerprint() + "\n")
    verify_ready()


if __name__ == "__main__":
    prepare()

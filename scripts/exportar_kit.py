"""Build a reproducible, allowlisted transfer kit without account or runtime data."""

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

from verify_toolkit import verify


ROOT = Path(__file__).resolve().parents[1]
PREFIX = "hoplite-kit-portable"
MANIFEST = "MANIFIESTO-PAQUETE.json"
DEFAULT_ARCHIVE = ROOT / "exports" / f"{PREFIX}.zip"
STATIC_FILES = (
    ".gitignore", "AGENTS.md", "LEEME-PRIMERO.md", "PROMPT-PARA-HOPLITE.txt",
    ".hoplite/settings.json", ".hoplite/setup.sh",
    ".github/dependabot.yml", ".github/workflows/verify.yml",
    ".github/workflows/maintenance.yml", "docs/maintenance.md",
    "docs/provenance/skills-export-manifest.json", "docs/provenance/additional-skills.json",
    "docs/provenance/attachment-integrity.json",
    "docs/provenance/action-pins.json", "docs/provenance/upload-artifact-pin.json",
    "scripts/verify_toolkit.py", "scripts/check_upstreams.py", "scripts/business_math.py",
    "scripts/exportar_kit.py", "examples/business-scenarios.json", "examples/cohorts.json",
    "tests/test_research_runtime.py", "tests/test_mcp_regressions.py",
    "tests/test_upstream_monitor.py", "tests/test_business_math.py",
    "tests/test_verification.py", "tests/test_personal_installer.py",
    "tests/test_readability.py", "tests/test_portable_bundle.py",
    "tools/personal-skills/package.json", "tools/personal-skills/package-lock.json",
    "tools/personal-skills/.npmrc", "tools/personal-skills/instalar.mjs",
    "tools/hoplite-research/pyproject.toml", "tools/hoplite-research/uv.lock",
    "tools/hoplite-research/.hoplite/setup.sh",
    "tools/hoplite-research/.hoplite/readability/package.json",
    "tools/hoplite-research/.hoplite/readability/package-lock.json",
    "tools/hoplite-research/scripts/run_mcp.py",
    "tools/hoplite-research/scripts/mcp_runtime.py",
    "tools/hoplite-research/scripts/research_mcp.py",
    "tools/hoplite-research/scripts/prepare_readability.py",
    "tools/hoplite-research/scripts/research_client.py",
)
EXPECTED_SERVERS = [
    {"name": f"research-{name}", "enabled": True, "config": {
        "transport": "stdio", "command": "python3",
        "args": ["tools/hoplite-research/scripts/run_mcp.py", name],
    }} for name in ("fetch", "arxiv")
] + [
    {"name": f"research-{name}", "enabled": True, "config": {
        "transport": "http", "url": url,
    }} for name, url in (
        ("context7", "https://mcp.context7.com/mcp"),
        ("firecrawl", "https://mcp.firecrawl.dev/v2/mcp"),
    )
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_source(root, relative):
    name = PurePosixPath(relative)
    if name.is_absolute() or str(name) != relative or ".." in name.parts or "\\" in relative:
        raise ValueError("Invalid portable path")
    path = Path(root).absolute() / relative
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError(f"Symlinks cannot be exported: {relative}")
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_size > 4 * 1024 * 1024:
        raise ValueError(f"Invalid or oversized source: {relative}")
    return path.read_bytes()


def payload(root=ROOT):
    root = Path(root)
    files = {name: read_source(root, name) for name in STATIC_FILES}
    original = json.loads(files["docs/provenance/skills-export-manifest.json"])
    additional = json.loads(files["docs/provenance/additional-skills.json"])
    entries = original["skills"] + additional["skills"]
    for entry in entries:
        name = f".agents/skills/{entry['path']}"
        files[name] = read_source(root, name)
    result = verify(root)
    if result != {"skills_verified": 27, "imported_skills_verified": 26,
                  "additional_skills_verified": 1, "mcp_configured": 4}:
        raise ValueError("Expected all 27 skills and exactly four MCP servers")
    settings = json.loads(files[".hoplite/settings.json"])
    expected = {
        "version": 1,
        "scripts": {"setup": {"enabled": True, "command": "bash .hoplite/setup.sh"}},
        "mcpServers": EXPECTED_SERVERS,
    }
    if settings != expected:
        raise ValueError("Only the reviewed credential-free project configuration can be exported")
    # The portable README must not link to research or evidence from the source account.
    files["README.md"] = files["LEEME-PRIMERO.md"]
    inventory = {
        "schema_version": 1,
        "scope": "project-kit; personal-library import requires separate destination authorization",
        "skills": sorted(entry["name"] for entry in entries),
        "original_skill_count": 26,
        "additional_skills": ["cohort-analysis"],
        "mcp_servers": [{"name": server["name"], "transport": server["config"]["transport"]}
                        for server in EXPECTED_SERVERS],
        "files": {name: {"sha256": digest(data), "bytes": len(data)}
                  for name, data in sorted(files.items())},
    }
    files[MANIFEST] = (json.dumps(inventory, ensure_ascii=False, indent=2) + "\n").encode()
    return files


def archive_bytes(root=ROOT):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload(root).items()):
            info = zipfile.ZipInfo(f"{PREFIX}/{name}", date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            mode = 0o755 if name.endswith(".sh") else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def checksum_text(data, archive):
    return f"{digest(data)}  {Path(archive).name}\n"


def build(root=ROOT, archive=DEFAULT_ARCHIVE):
    archive = Path(archive)
    if archive.suffix != ".zip":
        raise ValueError("The output must be a .zip archive")
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    if any(part.is_symlink() for path in (archive, checksum) for part in (path, *path.parents)):
        raise ValueError("Symlinks cannot be used as output paths")
    data = archive_bytes(root)
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_bytes(data)
    checksum.write_text(checksum_text(data, archive), encoding="utf-8")
    return {"archive": str(archive), "bytes": len(data), "sha256": digest(data)}


def check(root=ROOT, archive=DEFAULT_ARCHIVE):
    archive = Path(archive)
    data = archive_bytes(root)
    if archive.read_bytes() != data:
        raise ValueError("The archive differs from the reviewed sources; rebuild it")
    if archive.with_suffix(archive.suffix + ".sha256").read_text() != checksum_text(data, archive):
        raise ValueError("The external archive checksum is missing or incorrect")
    return {"archive_matches_sources": True, "sha256": digest(data)}


def verify_directory(root):
    files = payload(root)
    for name in ("README.md", MANIFEST):
        if read_source(root, name) != files[name]:
            raise ValueError(f"Portable file inventory does not match: {name}")
    return {"files_verified": len(files), "skills_verified": 27, "mcp_configured": 4,
            "personal_library_imported": False, "live_mcp_checked": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("build", "check"):
        commands.add_parser(command).add_argument("--output", type=Path, default=DEFAULT_ARCHIVE)
    commands.add_parser("verify").add_argument("--directory", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        if args.command == "verify":
            result = verify_directory(args.directory)
        else:
            result = {"build": build, "check": check}[args.command](archive=args.output)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()

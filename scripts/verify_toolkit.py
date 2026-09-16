"""Validate the imported skill roots and the project's reproducible configuration."""

import hashlib
import json
from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT):
    manifest = json.loads((root / "docs/provenance/skills-export-manifest.json").read_text())
    if manifest.get("schema_version") != 1 or len(manifest["skills"]) != 26:
        raise ValueError("Expected the 26-skill export manifest")
    entries = list(manifest["skills"])
    additional_path = root / "docs/provenance/additional-skills.json"
    additional = json.loads(additional_path.read_text()) if additional_path.exists() else {"schema_version": 1, "skills": []}
    if additional.get("schema_version") != 1:
        raise ValueError("Unknown additional-skill manifest format")
    entries.extend(additional["skills"])
    names = set()
    for entry in entries:
        name = entry["name"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
            raise ValueError("Invalid or duplicate skill name")
        names.add(name)
        if entry["path"] != f"{name}/SKILL.md":
            raise ValueError(f"Invalid skill path: {name}")
        path = root / ".agents/skills" / entry["path"]
        if any(part.is_symlink() for part in [path, *path.parents]):
            raise ValueError(f"Symlinks are not permitted: {name}")
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["export_root_sha256"]:
            raise ValueError(f"Review and record the changed skill hash: {name}")
        frontmatter = data.decode().split("---", 2)[1]
        if f"name: {name}\n" not in frontmatter or "description:" not in frontmatter:
            raise ValueError(f"Invalid skill metadata: {name}")

    skill_directory = root / ".agents/skills"
    if any(path.is_symlink() for path in skill_directory.rglob("*")):
        raise ValueError("Symlinks are not permitted in the active skill directory")
    active = {str(path.relative_to(skill_directory)) for path in skill_directory.rglob("SKILL.md")}
    expected = {f"{name}/SKILL.md" for name in names}
    if active != expected:
        raise ValueError("Unregistered or missing active skill roots")

    config = json.loads((root / ".hoplite/settings.json").read_text())
    servers = config["mcpServers"]
    if len({server["name"] for server in servers}) != len(servers):
        raise ValueError("Duplicate MCP names")
    for server in servers:
        connection = server["config"]
        if connection["transport"] == "stdio":
            launcher = (root / connection["args"][0]).resolve()
            if not launcher.is_relative_to(root.resolve()) or not launcher.is_file():
                raise ValueError("MCP launcher must be a project file")

    package_path = root / "tools/personal-skills"
    package = json.loads((package_path / "package.json").read_text())
    locked = json.loads((package_path / "package-lock.json").read_text())
    if package["dependencies"] != locked["packages"][""]["dependencies"]:
        raise ValueError("Personal CLI package and lockfile differ")
    for name, version in package["dependencies"].items():
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[\w.-]+)?", version):
            raise ValueError(f"Pin a reviewed exact version for {name}")
        if locked["packages"][f"node_modules/{name}"]["version"] != version:
            raise ValueError(f"Lockfile version mismatch: {name}")
    python = tomllib.loads((root / "tools/hoplite-research/pyproject.toml").read_text())
    if not all("==" in dependency for dependency in python["project"]["dependencies"]):
        raise ValueError("Pin exact Python dependency versions")
    return {"skills_verified": len(names), "imported_skills_verified": len(manifest["skills"]),
            "additional_skills_verified": len(additional["skills"]), "mcp_configured": len(servers)}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))

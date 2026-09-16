"""Launch a research server without inheriting project credentials."""

import argparse
import os

from mcp_runtime import LOCAL_SERVERS, ROOT, isolated_environment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("server", choices=LOCAL_SERVERS)
    args = parser.parse_args()
    python = ROOT / ".venv" / "bin" / "python"
    if not python.is_file():
        parser.error("Dependencies are not installed. Run: bash .hoplite/setup.sh")
    os.chdir(ROOT)
    os.execve(python, [str(python), str(ROOT / "scripts" / "research_mcp.py"), args.server],
              isolated_environment())


if __name__ == "__main__":
    main()

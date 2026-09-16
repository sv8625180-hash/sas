#!/usr/bin/env bash
set -euo pipefail
umask 077

cd "$(dirname "$0")/.."
command -v uv >/dev/null || { echo 'Required: uv (https://docs.astral.sh/uv/).' >&2; exit 1; }
command -v node >/dev/null || { echo 'Required: Node.js for the official Fetch server.' >&2; exit 1; }
command -v npm >/dev/null || { echo 'Required: npm for locked Readability.js dependencies.' >&2; exit 1; }

uv sync --locked --no-dev
mkdir -p .research/home .research/arxiv .research/reports
.venv/bin/python scripts/prepare_readability.py
echo 'Research dependencies installed. Run: .venv/bin/python scripts/research_client.py check --live'

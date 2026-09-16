#!/usr/bin/env bash
set -euo pipefail
umask 077
cd "$(dirname "$0")/.."

python3 scripts/verify_toolkit.py
bash tools/hoplite-research/.hoplite/setup.sh
npm ci --prefix tools/personal-skills --ignore-scripts --no-audit --no-fund --engine-strict --registry=https://registry.npmjs.org
echo 'Project skills and MCP dependencies ready. Personal-library import and live checks are separate.'

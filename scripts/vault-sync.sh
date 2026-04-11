#!/usr/bin/env bash
# Run from repo root: ./scripts/vault-sync.sh
# Fetches latest shared state before reads/writes. Resolve conflicts locally if needed.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ ! -d .git ]]; then
  echo "vault-sync: no .git in $ROOT — initialize Git here or set KNOWLEDGE_VAULT to your vault clone." >&2
  exit 1
fi
git pull origin main

#!/usr/bin/env bash
# Install tracked Obsidian assets into local .obsidian/ (folder is gitignored).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/.obsidian/snippets"
cp -f "$ROOT/meta/obsidian/snippets/cluster-tag-colors.css" "$ROOT/.obsidian/snippets/"
python3 "$ROOT/scripts/refresh_cluster_tree.py"
echo "OK: snippet copied + graph synced. Obsidian → Appearance → enable CSS snippet cluster-tag-colors"

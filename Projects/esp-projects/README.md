---
type: project
title: ESP Projects workspace
slug: esp-projects
status: active
created: 2026-04-11 12:00:00
updated: 2026-04-11 22:25:00
repo: "https://github.com/BusyJan/Knowledge-Cluster-Vault.git"
tags: [project]
---

# ESP Projects workspace

## Current goal

- Maintain firmware and tooling across ESP-related repositories with a unified AI knowledge layer (Obsidian + Cursor + Git).

## Key insights

- Long-term memory lives in the vault; code repos stay authoritative for implementation.
- Default agent context: this file only; pull [[Summary]] or partial [[Notes]] when needed.
- **Before any vault read/write:** `git pull origin main` → edit → `git add .` → `git commit` → `git push origin main`.

## Current state

- Example project scaffold for the knowledge cluster (`esp-projects`).
- Vault automation: `scripts/vaultctl.py`, `scripts/vault-sync.sh`.
- Cursor rules enforce sync + append-only Notes (`## YYYY-MM-DD HH:MM`).

## Quick links

- [[Notes]] — append-only log
- [[Summary]] — compressed knowledge
- [[Decisions]] — durable decisions
- [[Tasks]] — actionable items

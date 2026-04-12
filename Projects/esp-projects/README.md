---
type: project
title: ESP Projects workspace
slug: esp-projects
status: active
created: 2026-04-11 12:00:00
updated: 2026-04-12 15:00:00
repo: "https://github.com/BusyJan/Knowledge-Cluster-Vault.git"
tags: [project]
---

# ESP Projects workspace

## Current goal

- Single **Obsidian knowledge cluster** (this vault path only: `MyKnowledgeVault/` next to `.cursor/`) for **SubZero PCB**, **subzero-pcb-engine**, dashboard, prototypes, and workspace decisions.
- Code stays authoritative in git repos; **narrative + links** live here.

## Key insights

- Long-term memory lives in the vault; code repos stay authoritative for implementation.
- Default agent context: this file; then [[Summary]]; partial [[Notes]] when auditing.
- **Before any vault read/write:** `git pull origin main` → edit → `git add .` → `git commit` → `git push origin main`.
- **Remote:** [BusyJan/Knowledge-Cluster-Vault](https://github.com/BusyJan/Knowledge-Cluster-Vault) (`main`). **Do not** create a parallel `Vault/` or `ObsidianVault/` at workspace root for the same purpose.

## Current state (2026-04)

- **SubZero hardware:** `project-apex/` — MAIN `subzero-main.kicad_pcb`, TOP `subzero-top-fixed.kicad_pcb`; **Prototype 3** current; snapshots under `project-apex/prototypes/prototype-*/`.
- **Tooling:** `subzero-pcb-engine/` — `pcb_parser`, KiCad CLI integration, **LAN dashboard** (`subzero-dashboard`).
- **Vault automation:** `MyKnowledgeVault/scripts/vaultctl.py`, `vault-sync.sh`.
- **Cursor:** `.cursor/rules/obsidian-knowledge-cluster.mdc`, `.cursor/skills/obsidian-memory-sync/SKILL.md`, `.cursor/hooks.json`.

## Other projects in this vault (for Graph + Dashboard)

- [[Graph Hub]] — links every project README (use for **global graph** connectivity)
- [[Projects/project-apex/README]] — KiCad files on disk
- [[Projects/subzero-pcb-engine/README]] — parser + dashboard repo
- [[Projects/nocturn/README]] — Nocturn firmware

## SubZero deep dives (read these)

- [[External-AI-Review-Package]] — **gesamte Hardware von anderen KIs bewerten lassen** (Matrix 12×1–10, konstruktiver Review inkl. BOM/Architektur + Pentest-Tool-Vergleich, 221 Footprints, Fakten-Anhang)
- [[SubZero-PCB-Prototypes]] — P1–P5, components, power chain, planned P4/P5
- [[SubZero-Engine-and-Dashboard]] — parser modes, dashboard, KiCad CLI
- [[Workspace-Repo-Map]] — paths, remotes, filenames
- [[Tooling-and-Comparisons]] — Pineapple / HackRF / Flipper / P4 chip roles

## Meta (vault hygiene)

- [[Notes]] — append-only log
- [[Summary]] — compressed knowledge
- [[Decisions]] — durable decisions
- [[Tasks]] — actionable items
- [[Obsidian Setup]] — Plugins (Dataview), Graph (vault root)

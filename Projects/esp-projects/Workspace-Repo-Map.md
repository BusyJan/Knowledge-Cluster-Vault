---
title: Workspace + repo map (ESP Projects)
tags: [paths, workspace, git]
updated: 2026-04-11
---

# Workspace + repo map

## Workspace root

- **Folder:** `ESP Projects` (Cursor workspace root on this machine)
- Example absolute path: `/home/jdoe/Documents/Projects/ESP Projects`

## Knowledge vault (this cluster only)

- **Path:** `MyKnowledgeVault/` **at workspace root**, next to `.cursor/`
- **Do not** create parallel `Vault/`, `ObsidianVault/`, or duplicate root folders for the same purpose.
- **Remote:** `git@github.com:BusyJan/Knowledge-Cluster-Vault.git` (HTTPS: `https://github.com/BusyJan/Knowledge-Cluster-Vault.git`)
- **Branch:** `main`
- **Sync:** `git pull origin main` → edit → `git add .` → `git commit` → `git push origin main`

## SubZero hardware (KiCad)

- **Directory:** `project-apex/`
- **MAIN:** `subzero-main.kicad_pcb`
- **TOP (display):** `subzero-top-fixed.kicad_pcb` (name kept for history/cache reasons)
- **Prototype snapshots:** `project-apex/prototypes/prototype-1/`, `prototype-2/`, `prototype-3/`
- **Prototype README:** `project-apex/prototypes/README.md` → mirrored in [[SubZero-PCB-Prototypes]]

## SubZero tooling

- **Directory:** `subzero-pcb-engine/` — parser, tests, dashboard FastAPI app
- **Env:** `subzero-pcb-engine/.env` (not committed; points to PCB paths + `KICAD_CLI`)

## Cursor integration (workspace)

- **Rules:** `.cursor/rules/obsidian-knowledge-cluster.mdc`
- **Skill:** `.cursor/skills/obsidian-memory-sync/SKILL.md`
- **Hooks:** `.cursor/hooks.json` (vault sync / session)

## Other repos in workspace (examples)

- `nocturn/`, `ESP32-DIV/`, `exile/`, `netcut-lab/`, etc. — separate firmware/tools; not all documented here unless needed.

## Related

- [[README]] — project `esp-projects` hub
- [[SubZero-Engine-and-Dashboard]]

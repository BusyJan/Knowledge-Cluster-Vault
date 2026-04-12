# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM` (legacy `## [YYYY-MM-DD]` may exist).

## [2026-04-11]

- Insight: A single vault with per-project slugs scales better than unstructured notes.
- Decision: Use README → Summary → Notes (partial) as the default context stack for the agent.
- Problem: Full vault in context is expensive; compression and retrieval rules are mandatory.
- Next Step: Wire Cursor rules + `vaultctl.py` into daily workflow; commit vault to Git.

## 2026-04-11 22:25

- Insight: **`subzero-vault/`** (under `ESP Projects/subzero-vault/`) is the **SubZero technical Obsidian vault** — curated notes + `_mirror/` copies of repo READMEs (prototypes, pcb-engine, dashboard, Cursor skill/hooks). It is **separate** from this **MyKnowledgeVault** cluster but linked by the same workspace.
- Context: User requested a full knowledge dump of prototypes, READMEs, and tool comparisons into Obsidian for offline reading.
- Decision: Keep **canonical** files in git repos; **`subzero-vault/_mirror/`** is refreshed via `cp` (see `subzero-vault/_mirror/README.md`). Narrative notes: `00 - SubZero Home.md`, `SubZero — Full Project Overview (2026).md`, P4 chip reference, etc.
- Next step: Re-run mirror `cp` after README edits; optionally bump `Projects/esp-projects/README.md` `updated:` when major vault changes.

## 2026-04-11 23:50

- Insight: **Canonical cluster memory** for assistants is **`MyKnowledgeVault/`** only (next to `.cursor/`); remote **BusyJan/Knowledge-Cluster-Vault**.
- Context: User asked to store **all** workspace knowledge — prototypes P1–P5, engine + dashboard, repo map, tooling comparisons — **without** creating `Vault/` or extra root folders.
- Decision: Added `SubZero-PCB-Prototypes.md`, `SubZero-Engine-and-Dashboard.md`, `Workspace-Repo-Map.md`, `Tooling-and-Comparisons.md` under `Projects/esp-projects/`; updated [[README]] + [[Summary]].
- Next step: `git pull` → `commit` → `push` after review; keep `project-apex/prototypes/README.md` as source of truth and refresh vault notes when it changes.

## 2026-04-12 12:00

- Insight: Obsidian vault stays useful when **prototype README** and **SubZero-PCB-Prototypes** stay in sync; add **Obsidian Setup** for Dataview/Dashboard.
- Context: User asked to update the vault for Obsidian.
- Decision: Re-synced [[SubZero-PCB-Prototypes]] from `project-apex/prototypes/README.md` (TOP 117, P5 before P4 block order); added [[Obsidian Setup]]; linked from [[00 - Start here]].
- Next step: After each `prototypes/README.md` edit, mirror or run a one-liner reminder in Tasks.

## 2026-04-11 12:00

- Insight: The vault is shared Git state across devices; sync before every memory read/write.
- Context: Cursor agent must run `git pull` then later `commit`/`push` when persisting knowledge.
- Problem: Conflicts must be resolved manually; no force-push or blind overwrites.
- Decision: Mandatory workflow pull → read/write minimal files → add → commit → push.
- Next step: Initialize/configure Git remote on `MyKnowledgeVault` and use `vault-sync.sh` before edits.

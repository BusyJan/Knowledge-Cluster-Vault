# Summary (compressed knowledge)

## Active themes

- **Vault architecture:** Single cluster, per-project slugs, append-only [[Notes]] with periodic roll-up into this file.
- **Token policy:** Agent loads [[README]] by default; [[Summary]] for depth; [[Notes]] only in slices.
- **SubZero (ESP Projects):** Hardware in `project-apex/` (P3 current: power on TOP, flash/PSRAM/RTC/IMU on MAIN); tooling in `subzero-pcb-engine/`; P4 = pentest ICs; P5 = optional expansion + SDR; wired CAN (MCP2551) **out of plan**.

## Compressed history

- **2026-04-11:** Established README/Summary/Notes layering; automation via Python `vaultctl.py`; Cursor rules enforce slug + append semantics.
- **2026-04-11 (late):** Full knowledge dump into vault notes: [[SubZero-PCB-Prototypes]], [[SubZero-Engine-and-Dashboard]], [[Workspace-Repo-Map]], [[Tooling-and-Comparisons]] — mirrors `project-apex/prototypes/README.md` + engine/dashboard READMEs; remote **Knowledge-Cluster-Vault** only under `MyKnowledgeVault/`.

<!-- VAULTCTL:COMPRESSED_START -->
## Recent (from Notes, last 14 days)

## [2026-04-11]

- Insight: A single vault with per-project slugs scales better than unstructured notes.
- Decision: Use README → Summary → Notes (partial) as the default context stack for the agent.
- Problem: Full vault in context is expensive; compression and retrieval rules are mandatory.
- Next Step: Wire Cursor rules + `vaultctl.py` into daily workflow; commit vault to Git.

## 2026-04-11 12:00

- Insight: The vault is shared Git state across devices; sync before every memory read/write.
- Context: Cursor agent must run `git pull` then later `commit`/`push` when persisting knowledge.
- Problem: Conflicts must be resolved manually; no force-push or blind overwrites.
- Decision: Mandatory workflow pull → read/write minimal files → add → commit → push.
- Next step: Initialize/configure Git remote on `MyKnowledgeVault` and use `vault-sync.sh` before edits.

## Rolled up (older)

_None._

<!-- VAULTCTL:COMPRESSED_END -->

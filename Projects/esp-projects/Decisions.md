# Decisions

### [2026-04-11] Centralize long-term memory in one Obsidian vault

- **Context:** Multiple ESP projects; need cross-project recall without loading entire histories into LLM context.
- **Decision:** One Git-backed vault (`MyKnowledgeVault`), one folder per `slug`, agent writes via rules + `vaultctl.py`.
- **Consequences:** Slug is mandatory before persistence; Dashboard aggregates project README frontmatter.

### [2026-04-11] SubZero narrative lives in MyKnowledgeVault only (no duplicate vault roots)

- **Context:** User requested a single place for prototypes, README-derived docs, and comparisons; remote **github.com/BusyJan/Knowledge-Cluster-Vault**.
- **Decision:** All structured SubZero narrative under `MyKnowledgeVault/Projects/esp-projects/` (linked notes); **do not** create `Vault/` or `ObsidianVault/` at workspace root for the same purpose. KiCad + parser truth remains in `project-apex/` and `subzero-pcb-engine/`.
- **Consequences:** Optional `subzero-vault/` elsewhere is supplementary; assistants default to this cluster paths in [[Workspace-Repo-Map]].

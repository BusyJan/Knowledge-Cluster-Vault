# Decisions

### [2026-04-11] Centralize long-term memory in one Obsidian vault

- **Context:** Multiple ESP projects; need cross-project recall without loading entire histories into LLM context.
- **Decision:** One Git-backed vault (`MyKnowledgeVault`), one folder per `slug`, agent writes via rules + `vaultctl.py`.
- **Consequences:** Slug is mandatory before persistence; Dashboard aggregates project README frontmatter.

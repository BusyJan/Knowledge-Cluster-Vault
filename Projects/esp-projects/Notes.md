# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM` (legacy `## [YYYY-MM-DD]` may exist).

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

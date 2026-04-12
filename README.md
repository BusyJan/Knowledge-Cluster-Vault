# MyKnowledgeVault — AI knowledge cluster (Obsidian + Git)

**Obsidian users:** Open **this folder** as the vault (`File → Open folder… → MyKnowledgeVault`). Do **not** open the parent `ESP Projects` folder — otherwise the file tree and graph will not match this repo’s layout. See [[00 - Start here]].

**For assistants:** This folder (`MyKnowledgeVault/` at the workspace root, next to `.cursor/`) is the **only** knowledge vault for this setup. Do **not** create a parallel `Vault/`, `ObsidianVault/`, or other root folder for the same purpose. Project memory lives in `Projects/<slug>/` inside **this** directory.

This directory is the **long-term memory layer** for work across repositories. It is **not** a generic notebook: it is structured, token-efficient, and **shared across devices via Git**.

## Git as source of truth

Treat this folder as **the** vault repo (clone it on every machine; one remote, e.g. GitHub).

### GitHub repository

Remote: **[BusyJan/Knowledge-Cluster-Vault](https://github.com/BusyJan/Knowledge-Cluster-Vault)** (`main`).

Clone elsewhere — **folder name must be `MyKnowledgeVault`** (workspace root, next to `.cursor/`). Do **not** clone into `Vault/`, `ObsidianVault/`, or a second copy under another name for this system.

```bash
git clone https://github.com/BusyJan/Knowledge-Cluster-Vault.git MyKnowledgeVault
# SSH: git clone git@github.com:BusyJan/Knowledge-Cluster-Vault.git MyKnowledgeVault
```

`origin` is already configured on this machine after the initial push.

**Agent workflow (when persisting memory):**

1. `cd` to this directory (the repo root).
2. `git pull origin main` (or `./scripts/vault-sync.sh`).
3. Read/write only the minimal files (see Cursor rules).
4. `git add .`
5. `git commit -m "<meaningful memory update message>"`
6. `git push origin main`

Never force-push. On merge conflicts, stop and resolve locally.

If Git is not initialized yet: `git init`, add remote, first push — then use the workflow above.

## Layout

| Path | Role |
|------|------|
| `Dashboard.md` | Cluster index (Dataview + `refresh-dashboard` fallback) |
| `Projects/<slug>/` | One folder per project (**slug required**) |
| `Templates/` | Seeds for new projects |
| `Inbox/` | Pre-slug capture only |
| `Archive/` | Retired projects |
| `scripts/vaultctl.py` | Scaffold / append / compress (no LLM) |
| `scripts/vault-sync.sh` | `git pull origin main` helper |

Per project: `README.md` (state + YAML), `Summary.md`, `Notes.md` (append-only), `Decisions.md`, `Tasks.md`.

**`esp-projects`:** SubZero PCB + engine notes live as sibling pages under `Projects/esp-projects/` (e.g. `SubZero-PCB-Prototypes.md`, `Workspace-Repo-Map.md`) — see [[Projects/esp-projects/README]].

**Multi-project graph:** [[Graph Hub]] links every `Projects/<slug>/README` so the **global graph** shows connected nodes (see [[Obsidian Setup#Global vs local graph]]).

### README frontmatter (new projects)

`type: project`, `title`, `slug`, `status`, `created`, `updated`, `repo` (may be empty).

### Notes.md

New entries use:

```markdown
## YYYY-MM-DD HH:MM
- Insight:
- Context:
- Problem:
- Decision:
- Next step:
```

Legacy headings `## [YYYY-MM-DD]` are still parsed for compression.

## Token policy

1. Default: `Projects/<slug>/README.md` only.
2. Then `Summary.md` if needed.
3. `Notes.md` — partial reads only unless auditing.

## Automation: `vaultctl.py`

```bash
export KNOWLEDGE_VAULT="/path/to/MyKnowledgeVault"   # optional

python3 scripts/vaultctl.py ensure-project --slug my-project --title "My Project" --repo "https://github.com/BusyJan/Knowledge-Cluster-Vault.git"

python3 scripts/vaultctl.py append-note --slug my-project \
  --insight "..." --context "..." --problem "..." --decision "..." --next-step "..."

python3 scripts/vaultctl.py append-decision --slug my-project --title "..." --body "..."

python3 scripts/vaultctl.py compress --slug my-project --keep-days 14

python3 scripts/vaultctl.py refresh-dashboard

python3 scripts/refresh_cluster_tree.py   # Mermaid tree in CLUSTER-TREE.md
```

`compress` rolls older `Notes` sections into `Summary.md` between HTML comment markers (deterministic, not semantic).

## Cursor integration

- **Rules:** `ESP Projects/.cursor/rules/obsidian-knowledge-cluster.mdc`
- **Skill:** `ESP Projects/.cursor/skills/obsidian-memory-sync/SKILL.md`
- **Hooks (ESP Projects workspace):** `.cursor/hooks.json` runs **`beforeSubmitPrompt`** → `git pull` (fires before each message; use this if **`sessionStart`** does nothing on your build), **`sessionStart`** → pull, **`stop`** / **`afterAgentResponse`** → commit + `git push` if dirty. Open **ESP Projects** as the workspace root; enable **Settings → Hooks**. The agent is still instructed to run the same Git commands in the terminal when touching the vault, so sync works even if hooks fail.

## Dependencies

- Python 3.10+ (stdlib only for `vaultctl.py`).
- Obsidian **Dataview** plugin optional for `Dashboard.md`.

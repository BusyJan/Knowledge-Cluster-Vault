---
tags: [dashboard, cluster]
---

# Knowledge cluster dashboard

**Tree layout (root → projects → files):** open **[[CLUSTER-TREE]]** — a Mermaid diagram. The **Graph** view cannot draw the whole vault as a tree; use that note when you want hierarchy.

## Graph view (center + structure)

Obsidian’s **core graph is not a folder tree** — it’s a **force-directed** layout (nodes pull/push like springs). It will never look exactly like your file tree.

**Get a clear center**

1. With **`Dashboard`** open, open the **Local graph** (not Global). Local graph **centers on the active note** — use this file as the hub.
2. Set **depth** to `1` or `2` so you only see this note plus linked neighbors (less hairball).
3. Open **Settings → Core plugins → Graph view** (or the graph’s **⋯** menu) and tune:
   - **Center force** — **higher** pulls the cluster toward the middle (more “bunched”).
   - **Repel force** — **lower** so nodes don’t fly apart.
   - **Link distance** — shorter = tighter links.

**More tree-like (optional)**

- **Files / Outline** sidebar = real tree; use that when you want hierarchy.
- **Community plugins** with alternate layouts: e.g. **Juggl** (different graph layouts), or build a **MOC** (map of content) note with manual `[[wikilinks]]` — only those links become graph edges.
- **Global graph** with **search/filter** (e.g. path `Projects/`) shrinks the node set so the layout is readable.

**Why your graph looks messy**

- Notes that **don’t link each other** only connect through shared tags or appear as isolated dots.
- The **Dataview table above does not add wikilinks** to the file body, so it usually **does not create new graph edges**. Real edges come from `[[Some note]]` in Markdown.

Aggregates **project index files** under `Projects/`. Requires the [Obsidian Dataview](https://github.com/blacksmithgu/obsidian-dataview) community plugin.

```dataview
TABLE WITHOUT ID
  link(file.path, title) AS Title,
  slug AS Slug,
  status AS Status,
  updated AS Updated,
  repo AS Repo
FROM "Projects"
WHERE file.name = "README.md" AND type = "project"
SORT updated DESC
```

## Manual roll-up (optional)

If Dataview is unavailable, run:

```bash
python3 scripts/vaultctl.py refresh-dashboard --vault .
```

Paste the table below.

---

### Fallback table (paste)

| Title | Slug | Status | Updated | Repo |
|-------|------|--------|---------|------|
| ESP Projects workspace | esp-projects | active | 2026-04-12 14:00:00 | https://github.com/BusyJan/Knowledge-Cluster-Vault.git |
| nocturn | nocturn | active | 2026-04-12 12:00:00 |  |
| project-apex (SubZero KiCad) | project-apex | active | 2026-04-12 12:00:00 |  |
| subzero-pcb-engine | subzero-pcb-engine | active | 2026-04-12 12:00:00 |  |

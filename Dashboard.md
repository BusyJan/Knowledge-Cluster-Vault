---
tags: [dashboard, cluster]
---

# Knowledge cluster dashboard

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
| *(run refresh-dashboard)* | | | | |

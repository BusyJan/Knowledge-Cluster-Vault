---
tags: [cluster/meta, vault, leitfaden]
cluster: meta
---

# Vault-Leitfaden — Baum, Cluster, Farben

## Prinzip

| Ziel | Wie |
|------|-----|
| **Baum / Hierarchie** | Ordner (`Projects/<slug>/`, `Topics/<cluster-slug>/`, `Clusters/`). **`CLUSTER-TREE`** wird aus der Registry neu gerendert (farbig nach Cluster). |
| **Farben** | Obsidian **Graph**: Gruppen in `.obsidian/graph.json` werden von `scripts/refresh_cluster_tree.py` aus **`cluster-registry.json`** gespeist. Im Editor: optionales CSS-Snippet **cluster-tag-colors** (Settings → Appearance → CSS snippets). |
| **Keine unnötigen Verbindungen** | **Kein** `[[wikilink]]`-Spaghetti: nur gezielt (z. B. ein Cluster-MOC in `Clusters/`, oder README → zentrale Übersicht). Stattdessen **Ordner**, **Tags**, **Dataview**. |
| **Neues Thema = neuer Punkt** | **Eine** neue Datei unter `Topics/<cluster>/` (ein Gedanke / eine Frage / ein Entscheid-Punkt). Titel = klar; Frontmatter mit `cluster:` und `tags: [topic]`. Später bei Bedarf **umgruppieren** oder in `Projects/…/Notes.md` zusammenfassen — die Topic-Datei bleibt Archive. |

## Pflege

1. **Neues Projekt** unter `Projects/` anlegen (wie bisher) → Slug in **`cluster-registry.json`** unter dem passenden `clusters.*.projects` eintragen →  
   `python3 scripts/refresh_cluster_tree.py`  
   (aktualisiert **CLUSTER-TREE** + **Graph-Farben**).
2. **Neues Loslösbares Thema:** `Topics/hardware/2026-04-27-beispiel.md` von **`Templates/topic.atomic.md`** duplizieren (oder `vaultctl`/manuell).
3. **Cluster-Übersicht:** optional `Clusters/hardware.md` mit einer **Dataview**-Tabelle über `Topics/hardware` oder nur eine kurze Liste — **wenige** manuelle Links.

## Graph-Ansicht

- **Tags im Graph sind aus** (`showTags: false`), damit Tag-Knoten keine Zusatz-Kanten erzeugen.
- **Projekte** sind nach Cluster **eingefärbt**; `Topics/`, `Clusters/`, Dashboard-Bereich eigene Farbe.
- Für **baumartige** Orientierung immer **Akteure** oder **CLUSTER-TREE** / **Datei-Sidebar**, nicht nur den Graph.

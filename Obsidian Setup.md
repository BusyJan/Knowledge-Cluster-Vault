---
tags: [obsidian, meta]
---

# Obsidian Setup (dieses Vault)

## Vault öffnen

- **Ordner:** nur `MyKnowledgeVault/` (neben `.cursor/`), nicht den Parent `ESP Projects`.
- Siehe [[00 - Start here]] und [[README]].

## Empfohlene Community-Plugins

| Plugin | Grund |
|--------|--------|
| **Dataview** | [[Dashboard]] zeigt die Projekt-Tabelle (`FROM "Projects"` …). Ohne Plugin: Fallback-Tabelle manuell oder `vaultctl.py refresh-dashboard`. |
| **Tag Wrangler** (optional) | Tags in YAML (`tags:`) sortieren. |

Installation: **Einstellungen → Community plugins → Safe mode off → Browse** → installieren → aktivieren.

## Global vs local graph (why “nothing shows”)

Obsidian has **two** graph modes:

| Mode | What you see | Typical mistake |
|------|----------------|-----------------|
| **Local graph** | Only the **current note** + notes it links to (1–2 hops). | Looks “empty” if the open note has few links or you didn’t zoom. |
| **Global graph** (whole vault) | **All notes** and links — this is what you want for “all projects”. | Open graph, then switch to **global** / “show entire vault” (wording varies by version). |

**Do this:** Open **Graph view** → use the control that shows the **full vault** (not “linked to active file” only). Zoom out; enable **Orphans** so even unlinked notes appear as dots.

**Hub note:** [[Graph Hub]] links every `Projects/<slug>/README` so the graph has a **star** of connections even if you mostly use local graph from that file.

Other settings: **Filter** panel → search **empty**; don’t exclude `Projects/`.

## Graph (short)

- Orphans anzeigen, Filter leer lassen — siehe [[00 - Start here#Graph-Ansicht]].

## Git

`.obsidian/` ist in `.gitignore` — **lokale** UI-Einstellungen werden nicht committed. Auf neuem Rechner: Plugins einmal neu installieren.

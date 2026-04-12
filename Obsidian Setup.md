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

## Graph

- Orphans anzeigen, Filter leer lassen — siehe [[00 - Start here#Graph-Ansicht]].

## Git

`.obsidian/` ist in `.gitignore` — **lokale** UI-Einstellungen werden nicht committed. Auf neuem Rechner: Plugins einmal neu installieren.

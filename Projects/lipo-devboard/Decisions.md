# Decisions

Record durable decisions with date and context. One decision per block.

## 2026-04-20 — atopile als Standard für neue Hardware-Projekte

- **Context:** Trial-Projekt `lipo-devboard` mit USB-C → LDO → ESP32 Subsystem in atopile gebaut. 4 Module, 273 LOC, 14 Komponenten, Build in 14s mit echten JLCPCB-Parts und Datasheets. Verglichen mit gleichzeitig laufendem SubZero-Projekt direkt in KiCad (3+ Wochen für ähnliche Funktionalität).
- **Decision:** Alle neuen Hardware-Projekte ab heute starten als atopile-Projekte. SubZero v1 bleibt in KiCad (zu weit für Migration, ~80% complete). atopile-Templates und Atomic-Components werden in einer wiederverwendbaren Library gesammelt (`~/.cursor/skills/pcb-engineer/templates/` für Patterns, projekt-lokal `parts/` für konkrete Parts). Cursor-Skill `pcb-engineer` ist die zentrale Knowledge-Base und unterstützt sowohl atopile-First als auch KiCad-Patches.
- **Consequences:** PRO: 5-10× Speedup für neue Projekte, BOM auto-generiert mit echten Stock-Checked Parts, Datasheets auto-downloadet, git-diffable Hardware-Source, Module copy-paste-reusable, AI kann viel besser Code generieren als Schematic-Klicks. CONTRA: Lernkurve für ato DSL (~2-3h für aufgeschlossene Entwickler), Atomic-Component-Setup bei jedem neuen Custom-Part (~30 min pro IC, einmal), Standard-Library nicht so umfangreich wie KiCad (vor allem Connectoren). Trial bewertet positiv nach 1 Stunde Trial-Build.

## Template

### [YYYY-MM-DD] Short title

- **Context:**
- **Decision:**
- **Consequences:**

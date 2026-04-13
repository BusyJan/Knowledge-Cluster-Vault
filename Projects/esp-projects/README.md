---
type: project
title: ESP Projects workspace
slug: esp-projects
status: active
created: 2026-04-11 12:00:00
updated: 2026-04-13 00:45:00
repo: "https://github.com/BusyJan/Knowledge-Cluster-Vault.git"
tags: [project]
---

# ESP Projects workspace

## AI Briefing — lies das zuerst

> **Stand: 2026-04-13.** Du bist ein neuer Agent auf einem anderen Laptop. Hier ist der aktuelle Zustand.

### Was ist SubZero?

SubZero ist eine **tragbare Pentest-/RF-Forschungsplattform** (80 × 140 mm) mit zwei gestapelten PCBs (**MAIN** + **TOP**), verbunden über einen 30-pin Hirose DF12 B2B-Connector. Zwischen den Boards sitzt ein 60 × 140 × 4 mm Li-Po Akku. Das Gerät vereint: Flipper Zero + Ubertooth + Proxmark3 + HackRF-artig + Rubber Ducky + UWB + iButton + RS232.

### Wo stehen wir?

**Prototype 4 (P4)** ist der aktuelle Entwicklungsstand. P1–P3 sind abgeschlossen (Snapshots unter `project-apex/prototypes/prototype-*/`). P5 (Expansion + SDR) ist optional/Zukunft.

### Was wurde in der letzten Session gemacht (2026-04-12/13)?

1. **6 externe KI-Modelle** (Grok, ChatGPT, Gemini, Claude, VeniceAI, DeepSeek) haben SubZero P4 reviewed
2. Vorher wurde ein **Kalibrierungsexperiment** durchgeführt: Alle 6 KIs reviewten den HackRF One, Ergebnisse wurden gegen bekannte Fakten geprüft → Korrekturtabelle für Bias jeder KI erstellt
3. P4-Reviews mit Kalibrierung ausgewertet → **bereinigte Gesamtnote: 6.8/10**
4. **Alle 8 identifizierten Schwachpunkte** wurden als Engineering Specs gelöst und in `prototypes/README.md` Abschnitt A–I dokumentiert:
   - A) 4-Layer Stackup (Impedanzberechnung)
   - B) B2B 30-Pin komplett durchgezählt (alle Signale verifiziert)
   - C) RF-Koexistenz-Plan (Firmware-Scheduling + Hardware-Gating)
   - D) DW3000 UWB Layout-Regeln
   - E) AT86RF215 Matching-Netzwerk Regeln
   - F) BQ25798 Thermal Management
   - G) Shielding-Can-Zonen (2 Stück auf MAIN)
   - H) RP2040 Debug-Zugang (SWD + BOOTSEL)
   - I) GPIO-Erweiterungen (2. 74LVC125, neue AW9523-Belegung)

### Was steht als Nächstes an?

- **KiCad-Layout**: P4-Komponenten im Layout platzieren — AT86RF215 zuerst, dann DW3000 in Ecke, Shielding-Can-Footprints, Stackup in Board Setup eintragen
- **Optional**: P4-Prompt nochmal an KIs senden mit den neuen Specs → Score sollte auf ~8/10 steigen
- **Firmware-Architektur**: RF-Scheduling-Layer implementieren (Prioritätsmatrix aus Abschnitt C)

### Welche Dateien sind wichtig?

| Datei | Inhalt | Priorität |
|-------|--------|-----------|
| `project-apex/prototypes/README.md` | **Kanonische Quelle** für alle Prototypen P1–P5 + P4 Engineering Specs A–I | Höchste |
| `project-apex/docs/pinmap.md` | GPIO-Belegung ESP32-S3, AW9523 #1/#2, I2C-Adressmap, 74LVC125 Buffer | Hoch |
| `project-apex/generate_2board.py` | Board-Generator-Script mit Netzdefinitionen und Komponentenblöcken | Mittel |
| `project-apex/subzero-main.kicad_pcb` | MAIN PCB (aktuell P3-Stand, P4 muss noch gelayoutet werden) | Hoch |
| `project-apex/subzero-top-fixed.kicad_pcb` | TOP PCB (aktuell P3-Stand, P4 muss noch gelayoutet werden) | Hoch |
| `MyKnowledgeVault/Projects/esp-projects/External-AI-Review-Package.md` | AI-Review-Prompt + Ergebnisse P3 + P4 + Kalibrierung | Mittel |
| `MyKnowledgeVault/Projects/esp-projects/Notes.md` | Chronologischer Append-Only-Log aller Entscheidungen | Archiv |

### P4-Architektur in 30 Sekunden

- **MAIN** (4-Layer): 3 MCUs (ESP32-S3, ESP32-C6, nRF52840) + 6 RF-Module (2×CC1101, SX1262, nRF24) + 3 P4-ICs (AT86RF215 SDR, CC2400 BT Classic, DW3000 UWB) + Flash/PSRAM/RTC/IMU + Power Regulators + 4× TPS22918 Load Switches
- **TOP** (2-Layer): Display + Touch + USB2 Hub + 3 USB-Ports + BQ25798 Charger + STUSB4500 PD + Battery Protection + GPS + NFC/RFID + Audio + SE050C1 Secure Element + 3 P4-ICs (RP2040 BadUSB, DS2482 iButton, MAX3232 RS232)
- **B2B**: 30-pin → 5 GND, 3 VBAT, VBUS, V5V, USB D+/D-, I2C, FSPI, Display-Signale, MAX3232 UART, 3 Spare
- **USB3 → USB2 downgegradet** (EMI-Reduktion, 2.4 GHz sauber)
- **TP4056 (U16) + R701: DNP** (BQ25798 ersetzt sie komplett)

### KI-Kalibrierungstabelle (für zukünftige Reviews)

| Modell | Korrektur | Tendenz |
|--------|-----------|---------|
| Grok | -0.5 | Leicht wohlwollend, unterschätzt Risiken |
| ChatGPT | -0.5 | Leicht wohlwollend, aber gründlich |
| Gemini | -1.0 | Erfindet Probleme, mit [ANNAHME]-Prompt deutlich besser |
| Claude | ±0 | Analytischstes Modell, konservativ aber ehrlich |
| VeniceAI | Fakten prüfen | Oberflächlich, erfindet Redundanzen |
| DeepSeek | +0.5 bis +1.0 | Systematisch zu negativ, gute Details aber pessimistisch |

### Bekannte Designator-Fallen

- **U42** existiert auf BEIDEN Boards: MAIN U42 = DS3231 RTC, TOP U42 = STUSB4500 PD → nicht verwechseln
- **U13** (TOP) = SE050C1 (nicht ATECC), **U11** (TOP) = W25Q256, **U35** (TOP) = ATGM336H GPS
- **U16** TP4056 = **DNP**, nicht entfernen aus PCB aber NICHT bestücken

---

## Current goal

- Single **Obsidian knowledge cluster** (this vault path only: `MyKnowledgeVault/` next to `.cursor/`) for **SubZero PCB**, **subzero-pcb-engine**, dashboard, prototypes, and workspace decisions.
- Code stays authoritative in git repos; **narrative + links** live here.

## Key insights

- Long-term memory lives in the vault; code repos stay authoritative for implementation.
- Default agent context: this file; then [[Summary]]; partial [[Notes]] when auditing.
- **Before any vault read/write:** `git pull origin main` → edit → `git add .` → `git commit` → `git push origin main`.
- **Remote:** [BusyJan/Knowledge-Cluster-Vault](https://github.com/BusyJan/Knowledge-Cluster-Vault) (`main`). **Do not** create a parallel `Vault/` or `ObsidianVault/` at workspace root for the same purpose.

## Other projects in this vault (for Graph + Dashboard)

- [[Graph Hub]] — links every project README (use for **global graph** connectivity)
- [[Projects/project-apex/README]] — KiCad files on disk
- [[Projects/subzero-pcb-engine/README]] — parser + dashboard repo
- [[Projects/nocturn/README]] — Nocturn firmware

## SubZero deep dives (read these)

- [[External-AI-Review-Package]] — AI-Review-Prompt + P3/P4 Ergebnisse + HackRF-Kalibrierung + Bias-Tabelle
- [[SubZero-PCB-Prototypes]] — P1–P5, components, power chain
- [[SubZero-Engine-and-Dashboard]] — parser modes, dashboard, KiCad CLI
- [[Workspace-Repo-Map]] — paths, remotes, filenames
- [[Tooling-and-Comparisons]] — Pineapple / HackRF / Flipper / P4 chip roles

## Meta (vault hygiene)

- [[Notes]] — append-only log
- [[Summary]] — compressed knowledge
- [[Decisions]] — durable decisions
- [[Tasks]] — actionable items
- [[Obsidian Setup]] — Plugins (Dataview), Graph (vault root)

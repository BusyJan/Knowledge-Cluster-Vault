# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM` (legacy `## [YYYY-MM-DD]` may exist).

## [2026-04-11]

- Insight: A single vault with per-project slugs scales better than unstructured notes.
- Decision: Use README → Summary → Notes (partial) as the default context stack for the agent.
- Problem: Full vault in context is expensive; compression and retrieval rules are mandatory.
- Next Step: Wire Cursor rules + `vaultctl.py` into daily workflow; commit vault to Git.

## 2026-04-11 22:25

- Insight: **`subzero-vault/`** (under `ESP Projects/subzero-vault/`) is the **SubZero technical Obsidian vault** — curated notes + `_mirror/` copies of repo READMEs (prototypes, pcb-engine, dashboard, Cursor skill/hooks). It is **separate** from this **MyKnowledgeVault** cluster but linked by the same workspace.
- Context: User requested a full knowledge dump of prototypes, READMEs, and tool comparisons into Obsidian for offline reading.
- Decision: Keep **canonical** files in git repos; **`subzero-vault/_mirror/`** is refreshed via `cp` (see `subzero-vault/_mirror/README.md`). Narrative notes: `00 - SubZero Home.md`, `SubZero — Full Project Overview (2026).md`, P4 chip reference, etc.
- Next step: Re-run mirror `cp` after README edits; optionally bump `Projects/esp-projects/README.md` `updated:` when major vault changes.

## 2026-04-11 23:50

- Insight: **Canonical cluster memory** for assistants is **`MyKnowledgeVault/`** only (next to `.cursor/`); remote **BusyJan/Knowledge-Cluster-Vault**.
- Context: User asked to store **all** workspace knowledge — prototypes P1–P5, engine + dashboard, repo map, tooling comparisons — **without** creating `Vault/` or extra root folders.
- Decision: Added `SubZero-PCB-Prototypes.md`, `SubZero-Engine-and-Dashboard.md`, `Workspace-Repo-Map.md`, `Tooling-and-Comparisons.md` under `Projects/esp-projects/`; updated [[README]] + [[Summary]].
- Next step: `git pull` → `commit` → `push` after review; keep `project-apex/prototypes/README.md` as source of truth and refresh vault notes when it changes.

## 2026-04-12 12:00

- Insight: Obsidian vault stays useful when **prototype README** and **SubZero-PCB-Prototypes** stay in sync; add **Obsidian Setup** for Dataview/Dashboard.
- Context: User asked to update the vault for Obsidian.
- Decision: Re-synced [[SubZero-PCB-Prototypes]] from `project-apex/prototypes/README.md` (TOP 117, P5 before P4 block order); added [[Obsidian Setup]]; linked from [[00 - Start here]].
- Next step: After each `prototypes/README.md` edit, mirror or run a one-liner reminder in Tasks.

## 2026-04-12 12:30

- Insight: **Graph view** defaults to **local** scope — looks empty unless you use **global graph** or a **hub** note with links to every project.
- Context: User wants all projects visible in graph.
- Decision: Added `Projects/project-apex`, `subzero-pcb-engine`, `nocturn` stubs + [[Graph Hub]]; documented global vs local in [[Obsidian Setup]].
- Next step: Add more slugs under `Projects/` as new repos get important.

## 2026-04-12 14:00

- Insight: External reviewers need **one bundle**: counts + full ref list + roadmap + questions.
- Context: User asked for stats, all components, and plan for other AIs to review.
- Decision: Added [[External-AI-Review-Package]] + `project-apex/EXTERNAL_AI_REVIEW_BUNDLE.md` pointer; flagged U38/U42 overlap and SE050 ref drift in text.
- Next step: Regenerate after major PCB edits; run DRC before sending to reviewers.

## 2026-04-12

- Context: PCB TOP — **U38** (BQ25798) and **U42** (STUSB4500) were separated in layout; docs had stale overlap flags and wrong **U35** vs **U42** for PD.
- Decision: [[External-AI-Review-Package]] + [[SubZero-PCB-Prototypes]] + `subzero-vault` notes updated — **TOP U42** = STUSB4500, **U35** = ATGM336H GPS, **U13** = SE050C1, **U11** = W25Q256 on TOP; cross-board **MAIN U42** = DS3231.
- Next step: Re-export component tables if `subzero-pcb-engine` regenerates from PCB.

## 2026-04-12 15:00

- Insight: User wants **hardware evaluation**, not just a checklist — external AIs must **score** the whole stack.
- Context: Reframed [[External-AI-Review-Package]] with sections A/B (mandatory deliverables + 10-dimension matrix) and C (evidence appendix).
- Decision: Document title and `project-apex/EXTERNAL_AI_REVIEW_BUNDLE.md` updated to match.
- Next step: Paste doc + optional `prototypes/README.md` into any LLM and ask for output per section A.

## 2026-04-11 12:00

- Insight: The vault is shared Git state across devices; sync before every memory read/write.
- Context: Cursor agent must run `git pull` then later `commit`/`push` when persisting knowledge.
- Problem: Conflicts must be resolved manually; no force-push or blind overwrites.
- Decision: Mandatory workflow pull → read/write minimal files → add → commit → push.
- Next step: Initialize/configure Git remote on `MyKnowledgeVault` and use `vault-sync.sh` before edits.
## 2026-04-12 20:12

- Insight: Review prompts work better when they explicitly ask for component-selection, architecture critique, and market comparison instead of only issue-spotting.
- Context: User wants a constructive chat prompt, not another README-style doc, for external AI review of SubZero hardware.
- Problem: Existing review package focuses on scoring and risk flags but not enough on why parts were chosen, whether the architecture is coherent, and how the device compares with known pentest tools.
- Decision: Use a copy-paste chat prompt that asks for architecture review, component-choice review, trade-off analysis, concrete improvement suggestions, and a short comparison against common pentest devices like Flipper Zero, HackRF One, WiFi Pineapple, Proxmark3, and Ubertooth.
- Next step: Provide the prompt in-chat and optionally offer a shorter variant for weaker models.

## 2026-04-12 22:30

- Context: HackRF-Kalibrierungsexperiment abgeschlossen — 6 KI-Modelle (Grok, ChatGPT, Gemini, Claude, VeniceAI, DeepSeek) haben den HackRF One reviewed.
- Insight: KI-Modelle tendieren zu Übertreibungen in beide Richtungen. Hauptprobleme: (1) Gemini/VeniceAI erfinden Probleme die nicht existieren (z.B. "fehlende Ground-Planes", falsche Stromwerte), (2) DeepSeek bewertet systematisch zu negativ (4.5/10 für ein Gerät das 6–7 verdient), (3) Grok und ChatGPT sind am zuverlässigsten aber leicht wohlwollend.
- Decision: Kalibrierte Korrekturtabelle erstellt — bei SubZero-Reviews: Grok/ChatGPT -0.5, Gemini -1.0, VeniceAI/DeepSeek Fakten doppelt prüfen, Claude am analytischsten aber konservativ.
- Decision: Neuer P4-Review-Prompt mit Anti-Halluzinations-Maßnahmen: [ANNAHME]-Pflicht, "erfinde keine Probleme"-Regel, mehr Fakten-Verankerung, Kontext "Prototyp nicht Serienprodukt", faire Vergleichsklasse ($200–500).
- Next step: P4-Prompt an alle 6 Modelle senden, Ergebnisse mit Korrekturtabelle interpretieren.

## 2026-04-12 23:45

- Context: P4-Reviews von allen 6 KI-Modellen eingesammelt und mit HackRF-Kalibrierung ausgewertet.
- Insight: Anti-Halluzinations-Prompt hat gewirkt — deutlich weniger erfundene Probleme als bei P3-Reviews. [ANNAHME]-Labels wurden von allen Modellen benutzt. Gemini war diesmal viel sauberer. DeepSeek und VeniceAI hatten trotzdem 2–3 Faktenfehler (AT86RF215 falsch beschrieben, CC1101-Dual als "redundant").
- Insight: Bereinigter Durchschnitt nach Korrektur: **6.8/10** — P4 ist ein solider Prototyp mit professioneller Power-Chain und klarer Architektur. Kein Blocker, aber RF-Layout und Thermik müssen gemessen werden.
- Decision: 8-Punkte-To-Do-Liste aus Konsens aller Reviews: RF-Koexistenz-Plan, DW3000-Layout, AT86RF215-Matching, BQ25798-Thermik, B2B-Netzliste, Shielding Cans, RP2040-SWD, 4-Layer-Stackup.
- Next step: To-Do-Punkte in KiCad-Layout umsetzen, mit DW3000 und AT86RF215 Placement beginnen.

## 2026-04-13 00:30

- Context: Alle 8 Review-Punkte als Engineering Specs in `prototypes/README.md` Abschnitt A–I dokumentiert.
- Decision: 4-Layer Stackup definiert (L1 Signal, L2 GND, L3 Power, L4 Signal, 0.20mm Prepreg, ~1.6mm total, JLCPCB JLC04161H-3313). Impedanz: 50Ω Microstrip 0.35mm, 50Ω GCPW für DW3000 0.25mm/0.15mm gap.
- Decision: B2B 30-Pin komplett durchgezählt — 5 GND + 3 VBAT + VBUS + V5V + USB D+/D- + I2C + FSPI (5 pins) + Display (CS/DC) + SD_CS + W25Q_TOP_CS + LED + AW9523_INT + RF_TX_ACTIVE + MAX3232 TX/RX + RP2040_RUN + 3 Spare. Budget passt, 3 Spare für P5.
- Decision: RF-Koexistenz als Firmware-Scheduling mit 6-stufiger Prioritätsmatrix + Hardware-Power-Gating + RF_TX_ACTIVE Coexistence-Signal auf B2B.
- Decision: DW3000 → Bottom-right corner MAIN (max. Distanz zu 2.4 GHz Antennen oben). AT86RF215 → Zone (55–70, 35–55), zuerst platzieren, 2× U.FL rechte Kante.
- Decision: 2 Shielding Cans — CAN_1 (AT86RF215+CC2400, 20×15mm), CAN_2 (DW3000, 12×12mm).
- Decision: BQ25798 Thermal Vias (3×3, 0.3mm, 1.0mm pitch) + NTC 10kΩ an TS-Pin + SW-Throttle >40°C.
- Decision: RP2040 Debug: 3× SWD Testpads + BOOTSEL 0402 + RUN via B2B Pin 27.
- Decision: Zweiter 74LVC125 (U44) nötig für P4 HSPI: AT86RF215 + CC2400 + DW3000 (3 neue Gates). DW3000 CS → GPIO45 (spare strapping, LOW at boot = safe).
- Next step: KiCad Layout — AT86RF215 platzieren, DW3000 in Ecke, Shielding-Can-Footprints anlegen, Stackup in Board Setup eintragen.

## 2026-04-12 13:00

- Context: P4 KiCad Layout in `generate_2board.py` implementiert und beide Boards erfolgreich generiert — ZERO Kollisionen.
- Insight: Board wächst auf 80×159mm wegen 3 neuer Interior-Blöcke (AT86RF215, CC2400, HSPI-Buffer). DW3000 als Fixed-Edge-Placement bottom-right (bw-12, bh-28) um max. Abstand zu 2.4 GHz Antennen zu gewährleisten.
- Decision: MAIN Board (155 Footprints): U44 74LVC125 #2, U45 AT86RF215 + U46 TPS22918, U47 CC2400 + U48 TPS22918, U49 DW3000 + U50 TPS22918, 3× U.FL (J18 Sub-GHz, J19 2.4GHz, J20 UWB) + 3× ESD, SH1 Shield_SDR_BTC (20×15mm), SH2 Shield_UWB (12×12mm).
- Decision: TOP Board (79 Footprints): U51 RP2040 + 4× Decoupling + R1008 10k RUN + R1009 BOOTSEL, U52 DS2482-100 + Decoupling, U53 MAX3232 + 4× Caps, TP1/TP2/TP3 SWD Testpads, 3×3 Thermal-Via-Grid unter BQ25798 (30.0, 108.31).
- Decision: Neue Netze: MAIN +6 (SDR/BTC/UWB CS + V3V3), TOP +4 (RP2040 USB, MAX232 TX/RX). 4-Layer Stackup (MAIN) und 2-Layer (TOP) Header korrekt.
- Next step: Trace-Routing in KiCad (manuell), DRC, RF-Matching-Netzwerke für AT86RF215/DW3000.

## 2026-04-12 14:00

- Context: Zweiter P4 AI-Review-Zyklus mit 8 Modellen (Claude, DeepSeek, Venice AI, Qwen, Kimi, ChatGPT, Gemini, Grok). Kalibrierung angewendet.
- Insight: Kalibrierter Durchschnitt **7.3/10** (+0.5 vs. letzter Zyklus). Engineering Specs haben messbar geholfen. Pentest-Abdeckung einstimmig 9/10 (8/8 Modelle). Power Management 8.4/10. Risiken 6.0/10 (niedrigste Kategorie).
- Insight: 3 Faktenfehler identifiziert — DeepSeek (MAX17048 braucht keinen Shunt, 9 U.FL passen auf 80×159mm), Kimi (TPS63020 ist nicht Overkill bei Li-Po 3.0V). Anti-Halluzinations-Prompt weiter wirksam.
- Decision: 8 Aktionspunkte priorisiert — HOCH: CC2400 Fallback, Firmware-Architektur, Bring-up-Plan. MITTEL: BOM, Power-Sequencing, Debug-Testpunkte. NIEDRIG: TOP 4-Layer evaluieren, RF-Koexistenz-Matrix.
- Next step: Firmware-Architektur skizzieren, CC2400-Alternative recherchieren, BOM mit MPNs erstellen.

## 2026-04-12 15:00

- Context: Alle 8 Review-Aktionspunkte in `prototypes/README.md` als Sections J–Q umgesetzt.
- Decision: CC2400 bleibt auf P4 Board mit DNP-Option. Fallback = BrakTooth auf ESP32-S3. 20× CC2400 auf Vorrat kaufen. Für P5 ESP32-S31 evaluieren.
- Decision: Firmware-Architektur definiert: S3 als Master, UART1→C6, UART2→nRF52, USB→RP2040. Binary packet protocol. RF Arbitration State Machine (IDLE→SCANNING→TX_ACTIVE→COOLDOWN).
- Decision: 10-Phasen Bring-up-Plan (Power→Charger→S3→Display→I2C→SPI→C6→nRF→RF einzeln→Koexistenz), ~12h über 2 Tage.
- Decision: Power-Sequencing: TPS63020 auto-start, S3 boots first, AW9523 default LOW = alle RF OFF, 10ms Sequenz zwischen Load Switches.
- Decision: 5 neue Testpads (TP4-TP8) für C6 UART + nRF52840 SWD auf MAIN rechter Rand. ZERO Kollisionen nach Regeneration.
- Decision: RF-Koexistenz-Matrix als 10×10-Tabelle formalisiert. Regel: max 1× 2.4GHz TX gleichzeitig, multiple RX OK mit ≤3dB Desense.
- Decision: TOP bleibt 2-Layer für P4. Upgrade-Trigger: BQ25798 Tj>100°C bei 3A oder EMI >-40dBm.
- Decision: BOM mit MPNs für 25 Schlüsselkomponenten erstellt, inkl. Alternativliste und Risiko-Rating (LOW/MED/HIGH).
- Next step: Neuen Review-Prompt mit Sections A–Q generieren und an 8 AI-Modelle senden.

## 2026-04-12 16:30

- Context: Dritter P4 AI-Review-Zyklus mit 8 Modellen nach allen 8 Fixes (Sections J–Q). Vollständiger Prompt mit Firmware-Arch, Bring-up, BOM, Power-Seq, Debug-TPs, RF-Matrix, CC2400-Mitigation, TOP-4L-Evaluation.
- Insight: Kalibrierter Durchschnitt **8.0/10** (+0.7 vs. Zyklus 2, +1.2 vs. Zyklus 1). Größte Verbesserung: Dokumentation +1.1 (Gemini gibt 10/10!), RF-Koexistenz +1.0, Risiken +0.9.
- Insight: F (Pentest) bleibt einstimmig 9+/10. E (Layout, 7.7) und H (Risiken, 6.9) sind die Kategorien die nur durch Routing + Bring-up + Firmware steigen können — nicht durch weitere Dokumentation.
- Insight: Chip-Upgrade-Konsens aus 8 Modellen: RP2350A (6/8), ST25R3916B (5/8), SE052 (5/8) sind P4 Drop-in-Upgrades. ESP32-S31 ist der P5 Game-Changer (4/8). AT86RF215 und BQ25798 haben keine Nachfolger.
- Decision: 9.5/10 ist durch Dokumentation allein nicht erreichbar. Nächster Score-Sprung kommt nur durch: fertiges Routing, erfolgreicher Bring-up, Firmware-MVP.
- Next step: KiCad Routing beginnen (RF-first: UWB GCPW → 2.4GHz → Sub-GHz → Digital), dann Gerber + Bestellung.

## 2026-04-12 17:45

- Context: P4 v3 Revision — 3 Drop-in-Chip-Upgrades + umfassende AI-Fehlerpunkt-Behebung.
- Decision: RP2040 → RP2350A (QFN-60, Pico SDK 2.x, HSTX, TrustZone). ST25R3916 → ST25R3916B (bessere ALM, gleicher Footprint). SE050C1 → SE052 (FIPS 140-3 L3, PQC-ready).
- Insight: README erweitert von 554 → 709 Zeilen. 9 neue Sections (R–Z): Mechanical Design (M2 Standoffs), UART Flow Control, SAW Filter Strategy (FL1 GPS DNP), ME6211 Current Budget (150mA/500mA = safe), DW01A/BQ25798 Threshold Coordination, B2B Current Validation (323mA cont / 905mA peak vs 900mA rated → OK), USB-C Host Expansion, TOP Copper Fill Rule, Validation Matrix.
- Insight: Guard-Time 1ms → 2ms (PLL settling), Phase 0 Dry-Test hinzugefügt, GPS SAW filter DNP pad im Generator, alle RP2040-Referenzen → RP2350A aktualisiert.
- Insight: Generator regeneriert — ZERO Kollisionen, TOP 80 FP, MAIN 160 FP.
- Next step: Neuer Review-Prompt mit Sections A–Z + gezielte Chip-Upgrade-Frage pro Komponente.

## 2026-04-12 19:00

- Context: P4v3 Review Zyklus 4 — 5 valide Reviews (Gemini 8.5, DeepSeek 8.4, Grok 8.9, Venice 8.0, Qwen 8.0). Kimi hat den Prompt nicht befolgt (kein Review).
- Insight: Kalibrierter Durchschnitt **8.06/10** (+0.06 vs Zyklus 3). Gesamtverbesserung seit Zyklus 1: **+1.26**. D (Komponentenauswahl) stieg am meisten (+0.4) dank RP2350A/SE052/ST25R3916B Upgrades.
- Insight: Dokumentation ist am Limit — Zyklus 3→4 brachte nur +0.06. F (Pentest) einstimmig 9.0, G (Doku) 8.8 (Gemini 10/10). E (Layout 7.6) und H (Risiken 7.2) steigen nur noch durch reale Hardware-Arbeit.
- Insight: Venice AI arbeitet mit veraltetem Kontext (gleiche Scores wie Zyklus 3). Kimi-Prompt muss expliziter sein. DeepSeek trackt Verbesserungen am besten.
- Decision: Dokumentation ist maxed out. Nächster Schritt ist KiCad Routing, dann Gerber + Bestellung.
- Next step: KiCad Routing beginnen (RF-first: UWB GCPW → 2.4GHz → Sub-GHz → Digital).

## 2026-04-14 12:00

- Context: Saubere programmatische Schematic-Verdrahtung statt nur PCB-Pad-Nets — `project-apex/wire_schematics.py`.
- Insight: Script parst KiCad-Libs (inkl. `extends` → Parent-Symbol), Fallback-Pins für fehlende Std-Symbole, platziert `global_label` an Pin-Endpunkten; NET_MAP deckt aktuell ~54% der Pins ab (wächst iterativ). AW9523B-Pinout aus offizieller Lib korrigiert (vorher falsch angenommen).
- Next step: Live-Lauf mit Backup (`.kicad_sch.bak`), ERC in KiCad, dann Coverage für verbleibende Passives/Interna erhöhen.

## 2026-04-14 12:30

- Context: User wollte P4-Backup, README P5/P6-Umnummerierung, 100% schematic pin coverage.
- Decision: **P5** = milestone „voll verdrahtete Netliste“ (`wire_schematics.py`: `global_label` + `no_connect` pro sichtbarem Pin, Marker `WIRE_SCHEMATICS_PY_V1`, idempotent). **P6** = früheres optionales Expansion/SDR-P5. Backup: `project-apex-backup-p4-unwired-20260414-1106.tar.gz` + 14× `sheets/*.kicad_sch.bak`.
- Insight: 895 nicht-versteckte Pins = 488 NET_MAP + 407 `no_connect`; 56 hidden Pins übersprungen.
- Next step: KiCad ERC, NET_MAP verfeinern wo `no_connect` falsch ist, dann Routing.

## 2026-04-14 13:00

- Insight: **100% coverage** jetzt wörtlich: **951/951** Pin-Endpunkte (inkl. library `hide`-Pins). Vorher wurden 56 Pins übersprungen → nur 895 gezählt.
- Decision: `infer_power_net()` nur für eindeutige Namen (`GND`/`VSS`/… und `+3V3`/`3V3`); Rest `no_connect`. `--strict` bricht ab, wenn noch `no_connect` nötig wäre (Ziel: volles NET_MAP ohne NC).
- Next step: Bei Bedarf NET_MAP erweitern + `--strict` bis Exit 0.

## 2026-04-27 22:15

- Insight: **Vault-Struktur** gewünscht wie **Baum + farbige Cluster**, wenig Graph-Spaghetti: `cluster-registry.json` (Projekt → Cluster), `scripts/refresh_cluster_tree.py` erzeugt **CLUSTER-TREE** (Mermaid-Subgraphen + `classDef`) und schreibt **Graph-Farben** (`showTags: false`). Neue Pfade **`Topics/<cluster>/`** (atomare Themen), **`Clusters/`** (sparsame MOCs), **`Vault-Leitfaden.md`**, CSS-Snippet **`cluster-tag-colors`** (Appearance aktivieren).
- Next step: Bei neuem Projekt-Slug Registry + Skript; losgelöste Themen als Topic-Datei statt Crosslink-Wolke; auf neuem Rechner `bash scripts/install_obsidian_assets.sh` (Snippet liegt unter `meta/obsidian/`).

## 2026-05-06 21:25

- Context: Neues **ESP32-WROOM-32U** (U.FL); User will **zuerst nur Wi-Fi** testen, Bluetooth/ESPNOW später.
- Insight: `esptool` aus Debian/Kali fehlt Stub-JSON → `pipx install esptool` (v5.x) löst Stub-Flash; **`pipx install --force platformio`** nach kaputtem Pipx-State; **pio** liegt unter `~/.local/bin/pio`.
- Insight: Bridge **CH343** (`usb-1a86_USB_Single_Serial_*`) → **`/dev/ttyACM0`**, Chip **ESP32-D0WD-V3**, Flash **4 MB** erkannt (`flash-id`).
- Decision: Repo **`wroom32u-playground/`** aktuell **nur** `wifi_scan` (Rolling-RSSI über Top-BSSIDs); ESP-NOW-Stub liegt unter **`later/espnow_tx.cpp`** bis Wi-Fi Phase abgeschlossen.
- Next step: Antenne Ein/Aus Vergleich auf gleichen BSSIDs (~10–20 dB Diff); danach separates BT-Classic-Skript.

## 2026-05-06 22:05

- Context: ESP32 soll auf **trusted laptop nicht angreifen**; Nocturn-Workflow parallel zu Leonardo bleiben.
- Decision: **Shared-secret serial handshake** `NOCTURN_SAFE_V1 <64-hex>` (115200 UART/CDC) vor jedem HID/Payload — Laptop-Tool `nocturn/mother_daemon.py watch` sendet Bursts bei neuer Bridge-Enumeration; Firmware in **`esp32-mother-safe/`** (`esp32_wroom_bridge` + `esp32_s3_hid`).
- Insight: **WROOM/WROVER + CH343** kann **kein USB-HID** zum Host; Gate per Serial ok, Typing-Payloads brauchen **ESP32-S3** (`esp32_s3_hid`) oder externen 32u4.
- Next step: User generiert `mother_token`, `emit-header` → flash; `mother_daemon watch` dauerhaft auf Dev-Maschine; Payloads später in `run_armed_behavior()`.

## 2026-05-06 23:55

- Context: **`esp32-s3-lab-diskhid`** MSC+HID authorized-lab scaffolding.
- Decision: **`tools/emit_stub_disk.py`** erweitert um **`--from-img`** → rohe FAT/FAT32-Images (nach `mkfs.vfat -F32`/`mcopy`) zu `src/disk_blob.cpp`; **`BUILD.md`** mit exakten Linux-Kommandos + **`msfconsole`** Handler One-liner.

## 2026-05-07 00:20

- Decision: **Codename `DiskHID`** — Nocturn-Integration **`nocturn diskhid`** → `scripts/diskhid-pipeline.sh` (msfvenom, FAT32+`mcopy`, `emit_stub_disk.py`, optional `pio --flash`); Default-Pfad Sibling **`esp32-s3-lab-diskhid/`**, Override **`NOCTURN_DISKHID_PRJ`**.


## 2026-05-07 01:05

- Decision: **`esp32-s3-lab-diskhid`** erhält **`NOCTURN_SAFE_V1`** CDC-Handshake (wie **`esp32-mother-safe`**): nach Enumeration ~**9 s** Fenster → Treffer = **HID aus**, MSC nutzbar; **`nocturn mother watch`** auf Trust-Host; ohne Token (Windows-Victim) = **ARMED**. Pipeline erfordert **`include/mother_token.h`** (gitignored).
## 2026-05-06 23:16

- Insight: ESP32 Arduino PROGMEM macro is empty; a large uint8_t disk_img_bin[] initializer goes to SRAM (.dram0.data) and fails link. extern const uint8_t places the blob in flash rodata.
- Context: esp32-s3-lab-diskhid / nocturn diskhid: build failed after embedding ~1.5 MiB FAT image.
- Problem: disk_blob.o overflowed dram0_0_seg by ~1.3 MiB.
- Decision: emit_stub_disk.py now emits extern const uint8_t disk_img_bin[N]; main.cpp uses disk_img_bin + pos; diskhid-pipeline default sectors 3072 to 512 (256 KiB); BUILD.md updated.
- Next step: Re-run nocturn diskhid; raise --sectors if m.exe+FAT grows (const keeps flash placement).
## 2026-05-06 23:19

- Insight: PIO auto-upload picks a serial device; mixed lab benches leave a classic ESP32 on ttyACM0 so esptool negotiates ESP32 while the ELF targets ESP32-S3.
- Context: DiskHID pipeline: pio upload after successful build.
- Problem: esptool: This chip is ESP32 not ESP32-S3 — /dev/ttyACM0 was WROOM/UART bridge, not S3 Native USB DevKit.
- Decision: User must flash only ESP32-S3 for esp32-s3-lab-diskhid; unplug classic ESP32 or pass nocturn diskhid --upload-port from pio device list. Scripts updated: diskhid-pipeline.sh --upload-port, NOCTURN_DISKHID_UPLOAD_PORT; BUILD.md and nocturn README note.
- Next step: Flash with DevKit connected; optionally install 99-platformio-udev rules for clearer multi-port labeling.
## 2026-05-06 23:24

- Insight: Docs used ttyACMx as shorthand for any ACM index; copying it literally yields ENOENT.
- Context: diskhid --upload-port
- Decision: diskhid-pipeline.sh now validates placeholder ttyACMx/ttyUSBx and missing paths before msf steps; BUILD.md/nocturn README clarify digit substitution.
## 2026-05-06 23:26

- Insight: In diskhid-pipeline.sh usage() heredoc, backticks around pio device list ran command substitution and corrupted --help output.
- Context: DiskHID
- Decision: Replaced with plain text (see: pio device list). Agent verified: --help, ttyACMx rejection, full pipeline without flash, pio run build.
## 2026-05-06 23:39

- Insight: DiskHID uploads failed from wrong autodetect (/dev/ttyS1) or classic ESP32 on ttyACM0 masquerading as the S3 target.
- Context: esp32-s3-lab-diskhid
- Decision: Added tools/verify_esp32s3_serial.py scan|check (esptool chip_id). diskhid-pipeline --flash runs probe before msfvenom; optional NOCTURN_DISKHID_SKIP_CHIP_CHECK. platformio.ini upload_port=/dev/ttyACM* to ignore ttyS*. Docs updated.
## 2026-05-06 23:41

- Context: DiskHID hardware
- Insight: Active lab UART is ESP32-WROVER/32U + CH343; esptool reports classic ESP32, not ESP32-S3 — expected for DiskHID preflight rejects.
- Decision: BUILD.md now names ESP32-WROVER and 32U explicitly as incompatible targets for DiskHID.
## 2026-05-06 23:47

- Insight: CH343 UART cannot back USB MSC to host; BLE transport is the honest classic-ESP32 lab substitute.
- Context: User S3 broken; WROVER 32U
- Decision: DiskHID adds esp32-wrover-ble-diskhid env + src/main_wrover_ble_diskhid.cpp; BLE HID + curl m.exe via HTTP; nocturn diskhid --classic-wrover [--http-artifact-port]; verify_esp32s3_serial.py --expect esp32-classic; BUILD/README/platformio.ini. USB MSC gadget remains S3-only.
## 2026-05-07 09:36

- Insight: Nocturn exposes ChromeOS-oriented BLE HID via `nocturn chrome-annoyer` → `scripts/chrome-annoyer.sh`; firmware `main_chrome_annoyer_ble.cpp` uses crosh (Ctrl+Alt+T) + shell + benign echo, no Win keys. Optional rotation-fix env sends Ctrl+Alt+Right once (pair name ChromeRotationTap).
- Context: esp32-s3-lab-diskhid PlatformIO envs esp32-wrover-chrome-annoyer-ble and esp32-wrover-chrome-rotation-fix-ble; docs in nocturn/README + esp32-s3-lab-diskhid/BUILD.md.
- Problem: Windows Run-box/HID sequences confuse ChromeOS display rotation.
- Decision: Document Chrome path separately; do not use macOS `open -a Terminal` on Chromebook.
- Next step: User: pair NocturnChromeAnnoyer on authorized lab Chromebook; customize post-shell command in source if needed.
## 2026-05-07 09:37

- Insight: Nocturn armoury Leonardo flash: avrdude init/leave-prog-mode errors often = wrong device on ttyACM (CH34x ESP32 vs ATmega32u4), ModemManager/brltty, or missed Caterina window.
- Context: armoury.py now warns on CH34x VID, retries upload.speed=19200, suggests flash-env.sh + upload-leonardo-waitport.sh, env NOCTURN_LEONARDO_FORCE_WAITPORT / NOCTURN_LEONARDO_UPLOAD_SPEED.
- Problem: User flash failed with "initialization failed" and protocol errors on /dev/ttyACM0.
- Decision: Keep Leonardo path separate from ESP32 PlatformIO; document recovery in CLI hints.
- Next step: On dev box: sudo bash nocturn/scripts/flash-env.sh then bash .../upload-leonardo-waitport.sh /dev/ttyACM0; confirm USB device is Leonardo.
## 2026-05-07 12:05

- Insight: BLE TwinStorm alternates Ctrl+Shift+F5 (ChromeOS Reload) and Ctrl+Search+H (~140 rounds); pair NocturnTwinStorm. CLI: nocturn chrome-annoyer --twinstorm; PIO esp32-wrover-chrome-twinstorm-ble.
- Context: Armoury hub: [1] Leonardo USB, [2] ESP32-S3 DiskHID wizard, [3] WROVER/BLE submenu; nocturn launcher dispatches diskhid.
- Problem: Non-crosh Chrome nuisance + clearer ESP32 UX in Nocturn.
- Decision: CHROME_BLE_TWINSTORM define + docs; armoury segmented by hardware.
- Next step: Verify Search key maps as HID LEFT_GUI on target Chromebooks.
## 2026-05-07 10:05

- Insight: Chrome rotation-fix BLE: old Ctrl+Alt+Right alone often ineffective; firmware now fires Ctrl+Shift+F5 bursts then Ctrl+Alt+all arrows. Some org policies still disable rotation shortcuts.
- Context: main_chrome_annoyer_ble.cpp CHROME_BLE_ROTATION_RELOAD_TAPS etc.
- Problem: User reported rotation did not work.
- Decision: Document official Reload-based rotation + arrow cycle in BUILD/README.
- Next step: If still no effect: manual Ctrl+Shift+Reload on device keyboard; confirm not enterprise-locked.
## 2026-05-07 10:07

- Insight: Chromebook onboard Reload (3rd top-row browser key) mapped in firmware as CHROME_RELOAD_HID default KEY_F3 not F5; TwinStorm + rotation use same define; F5 via -D CHROME_RELOAD_HID=0xC6 if host expects PC-style refresh.
- Context: main_chrome_annoyer_ble.cpp BUILD.md nocturn README
- Problem: Reload/rotation HID mismatch
- Decision: Central CHROME_RELOAD_HID
- Next step: .
## 2026-05-07 10:12

- Insight: Chrome BLE sketches now default advertise Logitech M650 L B + manufacturer Logitech via CHROME_BLE_KEYBOARD_NAME / MANUFACTURER in main_chrome_annoyer_ble.cpp.
- Context: Firmware + nocturn README/BUILD/armoury/chrome-annoyer sync.
- Problem: .
- Decision: .
- Next step: Forget old paired device on Chromebook after rename.

## 2026-05-06

- Insight: BLE **page spammer** build (`CHROME_BLE_PAGE_SPAM_ONLY`) floods **Ctrl+N** for new-tab flood; PIO env **`esp32-wrover-chrome-page-spam-ble`**, wrapper **`nocturn/scripts/page-spammer-ble.sh`** (chmod +x), **`chrome-annoyer.sh --page-spam`**, Armoury submenu **`[p]`**.
- Context: `esp32-s3-lab-diskhid/main_chrome_annoyer_ble.cpp` + BUILD/nocturn docs.
- Problem: TwinStorm-only flow had no lightweight tab-flood preset.
- Decision: Dedicated compile-time mode + mutually exclusive CLI flags with rotation-fix/twinstorm.
- Next step: Tune `CHROME_PAGE_SPAM_*` defines if Chrome OS drops keystrokes.

## 2026-05-07 10:17

- Insight: Page spammer (**`CHROME_BLE_PAGE_SPAM_ONLY`**) now sends **Ctrl+N forever** while paired (one post-connect settle, then **`loop`** spam; disconnect or power-cycle to stop); removed fixed **`CHROME_PAGE_SPAM_COUNT`**.
- Context: `main_chrome_annoyer_ble.cpp`, BUILD/chrome-annoyer/armoury copy.
- Problem: Earlier build stopped after N tabs.
- Decision: Dedicated **`loop`** path only for page-spam mode (**`tap_ctrl_new_tab` + yield**).
- Next step: Tune **`CHROME_PAGE_SPAM_CHORD_HOLD_MS`** / **`CHROME_PAGE_SPAM_GAP_MS`** only if keys drop.


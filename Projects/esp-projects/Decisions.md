# Decisions

### [2026-04-11] Centralize long-term memory in one Obsidian vault

- **Context:** Multiple ESP projects; need cross-project recall without loading entire histories into LLM context.
- **Decision:** One Git-backed vault (`MyKnowledgeVault`), one folder per `slug`, agent writes via rules + `vaultctl.py`.
- **Consequences:** Slug is mandatory before persistence; Dashboard aggregates project README frontmatter.

### [2026-04-11] SubZero narrative lives in MyKnowledgeVault only (no duplicate vault roots)

- **Context:** User requested a single place for prototypes, README-derived docs, and comparisons; remote **github.com/BusyJan/Knowledge-Cluster-Vault**.
- **Decision:** All structured SubZero narrative under `MyKnowledgeVault/Projects/esp-projects/` (linked notes); **do not** create `Vault/` or `ObsidianVault/` at workspace root for the same purpose. KiCad + parser truth remains in `project-apex/` and `subzero-pcb-engine/`.
- **Consequences:** Optional `subzero-vault/` elsewhere is supplementary; assistants default to this cluster paths in [[Workspace-Repo-Map]].

### [2026-04-12] USB3 → USB2 Downgrade for P4

- **Context:** VL822 USB3.2 Hub's SuperSpeed harmonics at 5 Gbps fall in the 2.4 GHz band, interfering with WiFi/BLE/GPS. 4 of 6 AI reviewers recommended downgrade.
- **Decision:** Replace VL822 USB3 with USB2.0 hub. USB3 deferred to P5 (SDR board with separate RF isolation).
- **Consequences:** Eliminates 2.4 GHz EMI, reduces heat, simplifies TOP routing (stays 2-layer). 480 Mbit/s sufficient for RP2040 HID, Logic Analyzer, SD card.

### [2026-04-12] MAIN upgraded to 4-Layer PCB

- **Context:** P4 adds AT86RF215 (dual-band SDR), CC2400 (2.4 GHz), DW3000 (6–8 GHz UWB) to MAIN. 2-layer inadequate for RF impedance control.
- **Decision:** 4-Layer: L1 Signal+RF, L2 solid GND, L3 Power zones, L4 Signal. 0.20mm prepreg, ~1.6mm total.
- **Consequences:** 50Ω microstrip achievable at 0.35mm trace width. GCPW for DW3000 at 0.25mm/0.15mm gap. JLCPCB stackup JLC04161H-3313.

### [2026-04-12] P4 IC distribution: RF-critical on MAIN, rest on TOP

- **Context:** P4 adds 6 new ICs. Need to decide where each goes.
- **Decision:** AT86RF215, CC2400, DW3000 → MAIN (latency-critical, RF). RP2040, DS2482-100, MAX3232 → TOP (non-latency-critical, USB/I2C/UART).
- **Consequences:** No extension board needed. B2B 30-pin sufficient (USB2 frees pins, RF ICs talk directly to MCUs on MAIN).

### [2026-04-12] TP4056 (U16) + R701 marked DNP

- **Context:** BQ25798 provides superior PD 3.0 charging at 5A. TP4056 creates competing charge path.
- **Decision:** Mark both as DNP (Do Not Place). Keep footprints for potential fallback.
- **Consequences:** Single charge path through BQ25798. Cleaner power tree.

### [2026-04-12] AI Review Calibration via HackRF Experiment

- **Context:** Need reliable AI reviews for SubZero hardware. AI models tend to hallucinate or over/under-rate.
- **Decision:** Had 6 AI models review HackRF One (known specs), compared against facts, built correction table. Applied to SubZero reviews.
- **Consequences:** Correction factors: Grok -0.5, ChatGPT -0.5, Gemini -1.0, Claude ±0, VeniceAI check facts, DeepSeek +0.5–1.0. Anti-hallucination prompt rules ([ANNAHME] labels, "don't invent problems") significantly reduced errors in P4 reviews.

### [2026-04-13] P4 Engineering Specs A–I (all 8 review action items)

- **Context:** Calibrated P4 reviews (6.8/10) identified 8 areas needing engineering specs before layout.
- **Decision:** Created detailed specs in `prototypes/README.md`:
  - A) 4-Layer stackup with impedance calculations
  - B) B2B 30-pin allocation (verified against netlist + pinmap)
  - C) RF coexistence plan (firmware scheduling + priority matrix)
  - D) DW3000 UWB layout rules (GCPW, keepout, corner placement)
  - E) AT86RF215 matching network (balun, placement, keepout)
  - F) BQ25798 thermal management (via array, NTC, SW throttle)
  - G) Shielding cans (2 zones on MAIN)
  - H) RP2040 debug (SWD testpads + BOOTSEL)
  - I) GPIO extensions (2nd 74LVC125, AW9523 spare pin assignments)
- **Consequences:** All review action items resolved. Ready for KiCad layout implementation.

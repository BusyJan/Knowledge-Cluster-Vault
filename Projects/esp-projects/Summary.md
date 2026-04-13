# Summary (compressed knowledge)

## Active themes

- **Vault architecture:** Single cluster, per-project slugs, append-only [[Notes]] with periodic roll-up into this file.
- **Token policy:** Agent loads [[README]] by default; [[Summary]] for depth; [[Notes]] only in slices.
- **SubZero (ESP Projects):** Hardware in `project-apex/`; **Prototype 4 current**; tooling in `subzero-pcb-engine/`; P5 = optional expansion + SDR; wired CAN **out of P4**.

## SubZero P4 — current state (2026-04-13)

### Architecture
- **MAIN** (4-Layer, F.Cu): ESP32-S3 + ESP32-C6 + nRF52840 + 2×CC1101 + SX1262 + nRF24 + AT86RF215 (SDR) + CC2400 (BT Classic) + DW3000 (UWB) + Flash/PSRAM/RTC/IMU + TPS63020/TPS61232/ME6211 + 4×TPS22918 Load Switches
- **TOP** (2-Layer, B.Cu): Display + Touch + USB2 Hub + 3 USB-Ports + BQ25798 5A Charger + STUSB4500 PD + Battery Protection + GPS + NFC/RFID + Audio + SE050C1 + RP2040 (BadUSB) + DS2482 (iButton) + MAX3232 (RS232)
- **B2B**: 30-pin Hirose DF12 — fully allocated (5 GND, 3 VBAT, VBUS, V5V, USB D+/D-, I2C, FSPI, Display, SD, LED, MAX3232 UART, RP2040 RUN, 3 spare)
- **USB3 → USB2 downgegradet** (EMI-Reduktion); **TP4056 (U16) + R701: DNP**

### Key decisions (P4)
- 4-Layer MAIN: Signal–GND–Power–Signal, 0.20mm prepreg, ~1.6mm, JLCPCB JLC04161H-3313
- DW3000 in bottom-right corner MAIN, GCPW 50Ω, 10mm keepout
- AT86RF215 zone (55–70, 35–55), placed first, 2× U.FL right edge, Microchip AN-00002
- 2 Shielding Cans: CAN_1 (AT86RF215+CC2400, 20×15mm), CAN_2 (DW3000, 12×12mm)
- BQ25798: 3×3 thermal-via array, NTC 10kΩ at TS pin, SW throttle >40°C
- RF coexistence: firmware scheduling with 6-level priority matrix, only 1× 2.4 GHz TX at a time
- Second 74LVC125 (U44) on MAIN for P4 HSPI devices; DW3000 CS on GPIO45
- RP2040: 3× SWD testpads + BOOTSEL 0402 + RUN via B2B pin 27

### AI review calibration (HackRF experiment)
6 KI models reviewed HackRF One → factual errors identified → correction table:
Grok -0.5 (wohlwollend), ChatGPT -0.5, Gemini -1.0 (erfindet Probleme), Claude ±0 (analytischstes), VeniceAI Fakten prüfen, DeepSeek +0.5–1.0 (zu negativ).
P4 calibrated average: **6.8/10** — all 8 action items resolved in `prototypes/README.md` specs A–I.

### Next steps
1. KiCad: place P4 components (AT86RF215 first → DW3000 → CC2400 → U44 buffer → shielding can footprints → stackup in Board Setup)
2. Optional: re-review P4 with updated specs → expected ~8/10
3. Firmware: RF scheduling layer (priority matrix from spec C)

## Compressed history

- **2026-04-11:** Vault established. README/Summary/Notes layering. Cursor rules + vaultctl.py.
- **2026-04-11 (late):** Full knowledge dump: SubZero-PCB-Prototypes, Engine-Dashboard, Workspace-Repo-Map, Tooling-Comparisons.
- **2026-04-12:** P3 reviewed by 6 AIs. U38/U42 layout collision fixed. TP4056 marked DNP. Documentation cleaned (U35/U42/U13/U11 designators). P4 architectural decisions made (USB2 downgrade, 4-layer MAIN, IC distribution). HackRF calibration experiment completed. P4 review prompt with anti-hallucination rules created.
- **2026-04-12/13:** P4 reviewed by 6 AIs (calibrated 6.8/10). All 8 action items from reviews solved as engineering specs A–I in prototypes/README.md. B2B 30-pin fully allocated. 4-layer stackup defined. RF coexistence plan with priority matrix. Shielding cans, thermal management, RP2040 debug, second 74LVC125 — all documented.

<!-- VAULTCTL:COMPRESSED_START -->
## Recent (from Notes, last 14 days)

See [[Notes]] for full chronological log. Key entries:
- 2026-04-12: PCB fixes, docs cleanup, P4 architecture, USB2 decision
- 2026-04-12 20:12: Review prompt created
- 2026-04-12 22:30: HackRF calibration completed
- 2026-04-12 23:45: P4 reviews analyzed
- 2026-04-13 00:30: All 8 action items completed as specs A–I

## Rolled up (older)

- 2026-04-11: Vault init, structure, rules

<!-- VAULTCTL:COMPRESSED_END -->

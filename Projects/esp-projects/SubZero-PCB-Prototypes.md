---
title: SubZero PCB Prototypes (P1–P5)
tags: [subzero, pcb, prototypes, project-apex]
updated: 2026-04-11
---

# SubZero PCB Prototypes

Canonical source in repo: `project-apex/prototypes/README.md`. This note mirrors it for Obsidian.

## Prototype 1 — Original Design

- **Board size:** 80 × 145 mm (both boards)
- **MAIN:** 127 components; all USB + SD on MAIN
- **TOP:** 62 components; display + UI + GPS + audio
- **B2B:** Single Hirose DF12 30-pin at bottom center
- **Notes:** First complete layout; user-optimized variant exists

## Prototype 2 — USB Migration + Battery Layout

- **Board size:** 80 × 140 mm (both boards, identical)
- **MAIN:** 100 components; RF + power + ESP32s
- **TOP:** 96 components; display + UI + USB hub + ESD + SD card
- **Changes from P1:**
  - Moved 27 USB/SD components from MAIN to TOP (B.Cu)
  - F.Cu = display/buttons/LEDs; B.Cu = electronics behind display
  - USB connectors J11–J13 at bottom edge, outward
  - SD slot J8 at right edge; rotation ~−90° (user may refine)
  - Both boards sized for ~60×140×4 mm Li-Po
  - B2B on side strips; **KiCad 10** stable format `(generator_version 10.0)` / file `v20260206`
- **Battery zone:** 60 mm wide centered, full length
- **Side strips:** ~10 mm each side for B2B

## Prototype 3 — High-End Upgrades (current layout)

- **MAIN:** 104 components
- **TOP:** 116 components (after duplicate U42/STUSB clone removed from TOP)
- **Power chain on TOP (B.Cu):** USB-C → **STUSB4500 U35** → **BQ25798 U38** (PD fast charge) → **DW01A U17** + **FS8205 U18** → **J10** battery → **MAX17048 U39** fuel gauge
- **TOP also:** TP4056 U16 (backup/reference; removable in P4), passives C1001–C1005, L703, R1001–R1002, R701, C961, R961, R962 — **SE050 U11** on TOP (from P1)
- **MAIN:** 32 MB flash **U40 W25Q256**, 8 MB PSRAM **U41 APS6404L**, RTC **U42 DS3231MZ+**, IMU **U43 ICM-20948** + passives C1006–C1011, R1003–R1004
- **Snapshot:** `project-apex/prototypes/prototype-3/` (MAIN + TOP copies)

**PCB filenames (typical):**

- `project-apex/subzero-main.kicad_pcb`
- `project-apex/subzero-top-fixed.kicad_pcb` (TOP; “fixed” name avoids editor cache issues)

## Prototype 4 — Pentesting Arsenal (planned)

- **Target:** TOP B.Cu free area (~5700 mm² behind display)
- **ICs (planned):** CC2400 (BT Classic sniff), RP2040 (BadUSB + LA), DS2482-100 (1-Wire/iButton), DW3000 (UWB), MAX3232 (RS232), AT86RF215 (SDR sub-GHz)
- **Removed from plan:** MCP2551 (wired CAN) — **wireless** auto attacks via CC1101 / UWB / BT preferred
- **Optional QoL sensors:** BMP390, BME680, VEML7700, VL53L1X, DRV2605L, MAX98357A

## Prototype 5 — Expansion + SDR (optional, future)

- **Expansion port:** header (e.g. 20-pin, 1.27 mm): SPI, I2C, UART, USB, 3.3 V / 5 V / GND
- **Optional module:** AD9361-class SDR + FPGA (e.g. iCE40/ECP5); **5.8 GHz** and wideband; RF isolation; separate board likely

## Related

- [[Workspace-Repo-Map]] — paths on disk
- [[SubZero-Engine-and-Dashboard]] — parser + LAN dashboard
- [[Tooling-and-Comparisons]] — Flipper / HackRF / Pineapple context

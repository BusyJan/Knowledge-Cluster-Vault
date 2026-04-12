---
title: SubZero PCB Prototypes (P1–P5)
tags: [subzero, pcb, prototypes, project-apex]
updated: 2026-04-12
synced_from: project-apex/prototypes/README.md
---

# SubZero PCB Prototypes

> **Mirror of** `project-apex/prototypes/README.md` — edit the repo file first, then re-sync this note.

## Prototype 1 — Original Design

- **Board size**: 80 x 145mm (both boards)
- **MAIN**: 127 components, all USB + SD card on MAIN
- **TOP**: 62 components, display + UI + GPS + audio
- **B2B**: Single Hirose DF12 30-pin at bottom center
- **Notes**: First complete layout. Includes user-optimized variant.

## Prototype 2 — USB Migration + Battery Layout

- **Board size**: 80 x 140mm (both boards, identical)
- **MAIN**: 100 components, RF + power + ESP32s
- **TOP**: 96 components, display + UI + USB hub + ESD + SD card
- **Changes from P1**:
  - Moved 27 USB/SD components from MAIN to TOP (B.Cu)
  - Clean side separation: F.Cu = display/buttons/LEDs, B.Cu = all electronics
  - USB connectors (J11-J13) oriented at bottom edge, facing outward
  - SD card slot (J8) at right edge, rotation -90°
  - Both boards same size for 60x140x4mm Li-Po battery
  - B2B connector moved to left side strip
  - File format upgraded to KiCad 10.0.0-1 stable (v20260206)
- **Battery zone**: 60mm wide centered, full board length
- **Side strips**: 10mm on each side for B2B connectors

## Prototype 3 — High-End Upgrades (Current)

- **MAIN**: 104 components
- **TOP**: 117 components
- **New components (now properly on TOP, B.Cu — behind display)**:
  - U38 BQ25798 — USB-C PD 3.0 Fast Charger (5A, replaces TP4056)
  - U39 MAX17048 — Battery Fuel Gauge (coulomb counter, I²C)
  - U16 TP4056 — kept for backup/reference (can be removed in P4)
  - U17 DW01A — Battery protection IC
  - U18 FS8205 — Battery protection dual-FET
  - J10 — JST battery connector
  - L703, C1001-C1005, R1001-R1002 — BQ25798 passives
  - R701, C961, R961, R962 — fuel gauge + battery divider passives
- **Power chain**: USB-C Port → STUSB4500 (TOP) → BQ25798 (TOP) → Battery (TOP)
- **New on MAIN**:
  - U40 W25Q256JVEIQ — 32MB SPI Flash
  - U41 APS6404L-3SQR — 8MB PSRAM
  - U42 DS3231MZ+ — RTC (±5ppm accuracy)
  - U43 ICM-20948 — 9-axis IMU (accel + gyro + magnetometer)
  - C1006-C1011, R1003-R1004 — support passives
- **Already on TOP (from P1)**: SE050C1 secure element (was ATECC)

## Prototype 5 — Expansion Port + SDR Module (OPTIONAL, FUTURE)

- **Expansion Port**: Female header (20-pin, 1.27mm) exposing SPI, I2C, UART, USB, 3.3V/5V/GND
- **SDR Module** (plugs into expansion port, optional):
  - AD9361 — 70MHz–6GHz full SDR (replaces HackRF RF section in one chip)
  - Lattice iCE40/ECP5 FPGA — real-time IQ processing
  - Covers: 315MHz, 433MHz, 868MHz, 1.09GHz (ADS-B), 1.5GHz (GPS), 2.4GHz, **5.8GHz**
  - Communication: SPI + USB (via VL822 hub, already on board)
- **Notes**: RF isolation required (separate board); 5.8GHz PCB design very complex

## Prototype 4 — Pentesting Arsenal (PLANNED)

- **Target board**: TOP B.Cu (behind display, ~5700mm² free)
- **New pentesting ICs**:
  - CC2400 — Bluetooth Classic Sniffing (Ubertooth functionality)
  - RP2040 — Dedicated BadUSB controller + Logic Analyzer (Sigrok)
  - DS2482-100 — iButton/1-Wire Master (physical access: doors, elevators)
  - DW3000 — Ultra-Wideband (relay attacks on car key fobs)
  - MAX3232 — RS232 Serial (router/switch console access)
  - AT86RF215 — Dual-Band SDR Transceiver (advanced RF analysis)
- **Rationale**: Completes the all-in-one pentesting device:
  Flipper Zero + Ubertooth + Proxmark + HackRF + Rubber Ducky (wireless automotive via RF/BT/UWB; wired CAN intentionally out of P4)
- **Optional QoL sensors** (if space permits after pentesting ICs):
  - BMP390 — Barometer/altimeter
  - BME680 — Environmental sensor
  - VEML7700 — Ambient light (auto-brightness)
  - VL53L1X — ToF laser distance
  - DRV2605L — Haptic motor driver
  - MAX98357A — I2S audio DAC/amp

## Related

- [[Workspace-Repo-Map]]
- [[SubZero-Engine-and-Dashboard]]
- [[Tooling-and-Comparisons]]

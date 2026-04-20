---
type: project
title: "atopile-parts Library (reusable atomic components)"
slug: "atopile-parts"
status: active
created: "2026-04-20"
updated: "2026-04-20"
repo: "https://github.com/BusyJan/atopile-parts"
tags: [project, atopile, library, hardware-as-code, reusable]
---

# atopile-parts Library

## Current goal

Wiederverwendbare atomic-Component-Library für atopile-Projekte. Enthält geprüfte LCSC-Parts mit auto-generated KiCad-Symbolen, Footprints und 3D-STEP-Modellen, plus High-Level-Wrapper-Module mit sauberen ElectricPower/ElectricLogic Interfaces.

## Key insights

- `ato create part --search <LCSC-ID> --accept-single` lädt aus EasyEDA: KiCad-Symbol + Footprint + 3D-STEP + Datasheet-URL + komplettes Pin-Mapping. ~2-3 Sekunden pro Part.
- Pattern: 2-Schicht-Architektur — `parts/` enthält raw atomic components mit RAW-Pinmaps, `modules/` enthält High-Level-Wrapper mit sauberen Interfaces (ElectricPower, ElectricLogic, DifferentialPair).
- atopile fängt ECHTE Schaltungs-Bugs zur Compile-Zeit: z.B. wenn ein Resistor versehentlich kurzgeschlossen wird (beide Pins auf gleichem Net), erscheint `Ercfault Shorted Interfaces` mit klarer Fehlermeldung.
- Local-File-Dependencies (`file://path`) müssen mit `ato sync --force` aktualisiert werden wenn die Source-Library geändert wird; atopile cached sonst die alte Version in `.ato/modules/<owner>/<package>/`.

## Current state

5 Atomic Components + 5 Wrapper-Module fertig:

| Atomic | LCSC | Wrapper Module |
|---|---|---|
| MICRONE_ME6211C33M5G_N | C82942 | LDO_3V3_ME6211, LDO_3V3_ME6211_Switchable |
| TOPPOWER_TP4056_42_ESOP8 | C16581 | LipoCharger_TP4056 (incl. status LEDs) |
| PUOLOP_DW01A | C351410 | LipoProtection_DW01A |
| Korean_Hroparts_Elec_TYPE_C_31_M_12 | C165948 | USB_C_Sink_2_0 |
| Espressif_Systems_ESP32_S3_WROOM_1_N8R8 | C2913201 | ESP32_S3_WROOM_1 |

Verifiziert im `lipo-devboard`: Build successful in 12.46s, 22 Footprints im KiCad-PCB, BOM mit echten LCSC-Parts, Datasheets auto-downloaded.

## Quick links

- [[Notes]] — append-only log
- [[Decisions]] — durable decisions
- [[Tasks]] — actionable items

## Next-up parts (Priority for next batch)

- ESP32-C6-MINI-1U
- nRF52840 Module
- CC1101 sub-GHz transceiver
- SX1262 LoRa transceiver
- BME280 environmental sensor
- LSM6DSO IMU
- W25Q256 SPI Flash
- BMI160 IMU
- ATGM336H GPS Module
- AW9523B I2C IO expander
- TSOP38238 IR receiver
- SK6812MINI-E NeoPixel

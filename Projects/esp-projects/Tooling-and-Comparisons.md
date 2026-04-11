---
title: Pentest tooling + comparisons (context)
tags: [subzero, comparison, rf, wifi]
updated: 2026-04-11
---

# Tooling comparisons (context for SubZero)

Not a shopping list — **design rationale** for what SubZero does vs commercial gear.

## WiFi Pineapple

- **What:** Linux + OpenWrt-class stack; **Mediatek** radios (e.g. MT7601U / MT7610U class); PineAP workflow (rogue AP, portals, modules).
- **vs ESP32:** Pineapple = **full Linux hostapd** + often **5 GHz**; ESP32 on SubZero = **2.4 GHz** (S3/C6) and strong for **portable** WiFi attacks but not a drop-in Pineapple clone.
- **Optional path:** **Linux WiFi module** (USB/UART to ESP32) or expansion board — see P5 in [[SubZero-PCB-Prototypes]].

## HackRF / SDR

- **What:** Wideband SDR (e.g. ~1 MHz–6 GHz class devices); **IQ** on host; GNU Radio.
- **vs SubZero:** AT86RF215 (P4) = **narrower bands**; **AD9361-class** (P5) = closer to “HackRF RF section” but still needs FPGA + power budget.
- **Honest:** HackRF remains reference for **wideband lab SDR**; SubZero aims **integrated** multi-tool handheld.

## Flipper Zero

- **What:** STM32 + CC1101 + NFC + IR + GPIO; portable “many protocols.”
- **vs SubZero:** More **MCU performance** (ESP32 + PSRAM + flash), **more radios** (WiFi 6, planned P4 RF), **bigger UI**; Flipper wins on **size** and **mature app store**.

## Alfa / USB WiFi (Kali)

- **What:** Linux driver + **RTL8812AU‑class** etc.; monitor mode on **PC**.
- **Module idea:** Same chipset on a **small Linux co‑module** talking UART/USB to SubZero — not “RTL chip next to ESP32 without Linux.”

## Automotive wireless (no wired CAN)

- **SubZero stance:** **MCP2551 / wired OBD** removed from P4 plan; **wireless** focus: **CC1101**‑class keyfob/TPMS, **DW3000** UWB relay research, **BT** attacks, **OBD Bluetooth dongles** via ESP32 stack.

## P4 chips (short)

| Chip | Role |
| --- | --- |
| CC2400 | BT Classic sniff (Ubertooth-style) |
| RP2040 | BadUSB + logic analyzer (Sigrok) |
| DS2482-100 | 1-Wire / iButton master |
| DW3000 | UWB (modern keyless / ranging) |
| MAX3232 | RS232 console (routers, industrial) |
| AT86RF215 | Sub-GHz SDR (IQ) complement to CC1101 |

## Related

- [[SubZero-PCB-Prototypes]]

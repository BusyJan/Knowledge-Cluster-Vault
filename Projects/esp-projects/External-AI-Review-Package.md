---
title: SubZero — Hardware-Bewertung durch externe KI
tags: [subzero, review, export, stats, hardware-evaluation]
updated: 2026-04-12
---

# SubZero — gesamte Hardware von anderen KIs bewerten lassen

**Zweck dieses Dokuments:** Du kannst es **vollständig** (plus optional `project-apex/prototypes/README.md`) an **beliebige andere KI-Modelle** schicken. Sie sollen **nicht nur Listen lesen**, sondern die **gesamte SubZero-Hardware** (zwei Platinen, **221 Footprints**) **bewerten**: Architektur, Risiken, Strompfad, RF, USB3, Sicherheit, Fertigung, Roadmap — mit **Noten** und **klarer Empfehlung**.

**Faktenbasis:** geparste KiCad-PCBs (`subzero-main.kicad_pcb`, `subzero-top-fixed.kicad_pcb`) + Prototyp-Roadmap.

---

## A) An die bewertende KI — verbindlicher Auftrag

**Deine Aufgabe:** Führe eine **unabhängige Hardware-Bewertung** der SubZero-Plattform durch. Du hast **keinen vollständigen Schaltplan** — arbeite mit den Footprint-Listen, Werten, Layern und Positionen unten sowie der Roadmap. **Markiere Unsicherheiten** explizit als Annahme.

**Du musst liefern (Ausgabeformat):**

| # | Lieferung |
|---|-----------|
| 1 | **Gesamtnote** 1–10 (10 = für Serie ohne offene Blocker) + **ein Satz** Begründung |
| 2 | Für **jede Zeile** der Matrix in **Abschnitt B**: Teilnote **1–10** + **2–4 Sätze** Begründung |
| 3 | **Top 5 Stärken** der aktuellen Hardware (Bullets) |
| 4 | **Top 5 Risiken** mit Schweregrad (niedrig / mittel / hoch / kritisch) |
| 5 | **Blocker:** Ja/Nein — wenn ja: konkrete Voraussetzungen vor Layout/Prototyp |
| 6 | **Empfehlung:** z. B. „P3 erst stabilisieren“, „P4 machbar“, „Mechanik/Stack prüfen“, „EMI-Vormessung“ |

**Ethik:** Geplante P4-Funktionen nur im Kontext **autorisierte Sicherheitsforschung / Labor** diskutieren.

---

## B) Bewertungsmatrix — jede Zeile mit 1–10 bewerten

| # | Dimension | Was du bewertest (Leitfragen) |
|---|-------------|------------------------------|
| 1 | **System-Architektur** | Sinniger Split MAIN (RF/MCU/Rechen) vs TOP (Anzeige, USB, Ladekette)? B2B-Zuführung? |
| 2 | **Stromversorgung & Akku** | Kette USB-C → PD → Charger → Schutz → Batterie → B2B → Verbraucher plausibel? SPoF? |
| 3 | **RF & Koexistenz** | Viele Funk-Interfaces/Antennen — Interferenz, Keepouts, GPS vs USB3 vs NFC? |
| 4 | **USB / Hochgeschwindigkeit** | Hub VL822, Kristall, ESD, mehrere Ports — Platz, EMI, Signalintegrität (qualitativ)? |
| 5 | **Mixed-Signal & Peripherie** | Audio, Tasten, NFC/RFID-Teil — Übersprechen / Masseführung (qualitativ)? |
| 6 | **Sicherheit (HW)** | Secure Element, Flash — Anbindung sinnvoll platziert? (ohne Netzliste nur grob) |
| 7 | **Thermik & Mechanik** | 80×140 mm, Doppelboard, Montage — realistisch? Hot spots? |
| 8 | **Fertigung & Testbarkeit** | DFM, Footprint-Mix, In-Circuit-Test / Debug erreichbar? |
| 9 | **Roadmap P4/P5** | Passt geplanter Pentest-/SDR-Block zu freiem TOP-B.Cu und Gesamtkonzept? |
|10 | **Datenkonsistenz** | Abgleich README vs Footprint-Export — siehe Abschnitt „Datenabgleich“ unten |

**Skala:** 1 = schwere Lücken oder Blocker · 5 = machbar mit klaren Nacharbeiten · 8–9 = stark · 10 = serienreif (selten ohne Messung).

---

## C) Fakten-Anhang — Zahlen & Listen (für deine Bewertung)

### 1) High-level stats (parsed PCB, current files)

| Metric | MAIN (`subzero-main.kicad_pcb`) | TOP (`subzero-top-fixed.kicad_pcb`) |
|--------|--------------------------------|-------------------------------------|
| **Total footprints** | 104 | 117 |
| **Stack total** | **221** (two physical PCBs) | |
| **MAIN copper side** | F.Cu only (104) | — |
| **TOP split** | — | F.Cu 15 (UI/LEDs/mounting), **B.Cu 102** (electronics) |

### Cross-board reference overlap (same designator string on both files)

Both boards intentionally reuse **MH1–MH4** (mounting holes).  
**U42** is reused by designator on **two different parts**: **MAIN** `U42` = **DS3231** (RTC); **TOP** `U42` = **STUSB4500** (USB PD). Each `.kicad_pcb` is independent — fine for Gerber/BOM per board; when writing docs or BOMs, prefix with **MAIN** / **TOP** or use the value field to avoid confusion.

### Datenabgleich README ↔ PCB (aktueller Stand)

1. **U38 vs U42 (TOP):** Getrennt platziert — **U42** STUSB4500 **(14.00, 109.50)** mm, **U38** BQ25798 **(30.00, 108.31)** mm, beide **B.Cu** (`subzero-top-fixed.kicad_pcb`).
2. **U35 (TOP):** **ATGM336H** (GPS) **(64.00, 25.00)** — nicht verwechseln mit PD: **USB PD = TOP U42** (STUSB4500).
3. **SE050 / Flash (TOP):** **U13** = **SE050C1**; **U11** = **W25Q256** (SPI Flash auf TOP) — so in README/BOM führen.

---

### 2) Prototype roadmap (from README)

| Proto | Summary |
|-------|---------|
| **P1** | 80×145 mm; USB/SD on MAIN |
| **P2** | 80×140 mm; USB/SD → TOP B.Cu; B2B side strips |
| **P3 (current)** | MAIN 104 / TOP 117; power chain on TOP; flash/PSRAM/RTC/IMU on MAIN |
| **P4 (planned)** | Pentest ICs on TOP B.Cu (CC2400, RP2040, DS2482, DW3000, MAX3232, AT86RF215) + optional sensors |
| **P5 (optional)** | Expansion header + AD9361-class SDR module |

---

### 3) Counts by designator prefix (approximate)

#### MAIN

| Prefix | Count |
|--------|------:|
| C | 36 |
| U | 19 |
| R | 14 |
| Q | 10 |
| J | 8 |
| D | 7 |
| MH | 4 |
| SW | 3 |
| L | 2 |
| (+ J_IB_M, etc.) | |

#### TOP

| Prefix | Count |
|--------|------:|
| C | 35 |
| U | 25 |
| R | 25 |
| D | 8 |
| J | 6 |
| SW | 5 |
| MH | 4 |
| Q | 2 |
| L | 2 |
| FB | 2 |
| (+ BZ, Y1, …) | |

---

### 4) Full component tables (ref, value, layer, position mm)

### MAIN — 104 components

| Ref | Value | Layer | Position (mm) |
|-----|-------|-------|----------------|
| C1006 | 100nF_FL | F.Cu | (24.00, 125.00) |
| C1007 | 100nF_PS | F.Cu | (44.00, 125.00) |
| C1008 | 100nF_RTC | F.Cu | (44.00, 115.00) |
| C1009 | 47uF_VBAT | F.Cu | (56.00, 115.00) |
| C101 | 100nF | F.Cu | (67.05, 15.00) |
| C1010 | 100nF_IMU | F.Cu | (44.00, 130.00) |
| C1011 | 10nF_IMU | F.Cu | (56.00, 130.00) |
| C102 | 10uF | F.Cu | (67.05, 18.00) |
| C103 | 100uF | F.Cu | (67.05, 22.00) |
| C201 | 100nF | F.Cu | (38.68, 91.69) |
| C202 | 10uF | F.Cu | (38.68, 94.69) |
| C203 | 1uF_GPIO9 | F.Cu | (39.31, 105.59) |
| C204 | 1uF_EN_RC | F.Cu | (19.89, 106.64) |
| C301 | 100nF | F.Cu | (55.91, 93.94) |
| C302 | 10uF | F.Cu | (55.91, 96.94) |
| C401 | 100nF | F.Cu | (37.00, 81.23) |
| C402 | 47uF_BULK | F.Cu | (37.00, 84.23) |
| C411 | 100nF | F.Cu | (60.30, 81.23) |
| C412 | 47uF_BULK | F.Cu | (60.30, 84.23) |
| C421 | 100nF | F.Cu | (66.67, 60.71) |
| C422 | 47uF_BULK | F.Cu | (66.67, 64.21) |
| C431 | 100nF | F.Cu | (39.25, 26.75) |
| C432 | 47uF_BULK | F.Cu | (39.25, 30.75) |
| C440 | 100nF_LS_A | F.Cu | (37.00, 87.23) |
| C442 | 100nF_LS_B | F.Cu | (60.30, 87.23) |
| C444 | 100nF_LS_N | F.Cu | (39.25, 34.75) |
| C446 | 100nF_LS_L | F.Cu | (66.67, 46.21) |
| C450 | 100nF_TX | F.Cu | (39.25, 38.75) |
| C621 | 1uF_LDO | F.Cu | (41.21, 64.45) |
| C701 | 10uF_TP_IN | F.Cu | (23.21, 50.45) |
| C702 | 10uF_TP_OUT | F.Cu | (23.21, 53.45) |
| C721 | 10uF_BB_IN | F.Cu | (23.21, 56.45) |
| C723 | 47uF_POSCAP1 | F.Cu | (20.21, 47.45) |
| C724 | 47uF_POSCAP2 | F.Cu | (41.21, 56.45) |
| C725 | 10uF_HF1 | F.Cu | (41.21, 47.45) |
| C731 | 10uF_BST | F.Cu | (24.21, 64.45) |
| D10 | ESD742 | F.Cu | (10.00, 7.00) |
| D11 | ESD742 | F.Cu | (22.00, 7.00) |
| D12 | ESD742 | F.Cu | (34.00, 7.00) |
| D13 | ESD742 | F.Cu | (46.00, 7.00) |
| D14 | ESD742 | F.Cu | (58.00, 7.00) |
| D15 | ESD742 | F.Cu | (70.00, 7.00) |
| D5 | IR_LED_940nm | F.Cu | (75.00, 94.20) |
| J1 | CC1101_A_ANT | F.Cu | (10.00, 3.00) |
| J15 | UART_HDR | F.Cu | (3.00, 104.40) |
| J17 | SWD_HDR | F.Cu | (71.30, 126.00) |
| J2 | CC1101_B_ANT | F.Cu | (22.00, 3.00) |
| J3 | LoRa_ANT | F.Cu | (34.00, 3.00) |
| J4 | nRF24_ANT | F.Cu | (46.00, 3.00) |
| J5 | S3_WiFi_ANT | F.Cu | (58.00, 3.00) |
| J6 | C6_WiFi_ANT | F.Cu | (70.00, 3.00) |
| J_IB_M | B2B_Header_30p | F.Cu | (5.00, 70.00) |
| L701 | 2u2_BB_IND | F.Cu | (21.21, 60.45) |
| L702 | 4u7_BST | F.Cu | (29.21, 64.45) |
| MH1 | M2 | F.Cu | (4.00, 4.00) |
| MH2 | M2 | F.Cu | (76.00, 4.00) |
| MH3 | M2 | F.Cu | (4.00, 136.00) |
| MH4 | M2 | F.Cu | (76.00, 136.00) |
| Q1 | DMP1045U_A | F.Cu | (37.00, 69.73) |
| Q12 | 2N7002_SPU | F.Cu | (75.00, 79.80) |
| Q2 | DMP1045U_B | F.Cu | (60.30, 69.73) |
| Q3 | DMP1045U_L | F.Cu | (66.67, 49.21) |
| Q4 | 2N7002_TXA | F.Cu | (36.43, 65.75) |
| Q5 | 2N7002_TXB | F.Cu | (60.30, 73.73) |
| Q6 | 2N7002_TXL | F.Cu | (66.67, 53.21) |
| Q7 | DMP1045U_N | F.Cu | (39.25, 14.75) |
| Q8 | 2N7002_TXN | F.Cu | (39.25, 18.75) |
| Q9 | Si2312DS | F.Cu | (41.21, 51.45) |
| R1003 | 4k7_SDA | F.Cu | (44.00, 112.00) |
| R1004 | 4k7_SCL | F.Cu | (56.00, 112.00) |
| R101 | 10k_GPIO0 | F.Cu | (64.05, 26.00) |
| R102 | 10k_GPIO3 | F.Cu | (64.05, 28.00) |
| R103 | 10k_GPIO46 | F.Cu | (64.05, 30.00) |
| R104 | 33R_FSPI_CLK | F.Cu | (64.05, 32.00) |
| R105 | 33R_FSPI_MOSI | F.Cu | (64.05, 34.00) |
| R201 | 10k_GPIO9 | F.Cu | (39.51, 106.85) |
| R202 | 10k_GPIO8 | F.Cu | (39.95, 108.17) |
| R203 | 10k_EN | F.Cu | (19.62, 105.40) |
| R301 | 0R_UART_TX | F.Cu | (55.91, 99.94) |
| R302 | 0R_UART_RX | F.Cu | (55.91, 102.94) |
| R440 | 4k7_TX_PU | F.Cu | (39.25, 41.75) |
| R981 | 4k7_1W_PU | F.Cu | (75.00, 75.40) |
| SW6 | PWR_Switch | F.Cu | (0.00, 75.40) |
| SW7 | BOOT | F.Cu | (0.00, 84.10) |
| SW8 | RESET | F.Cu | (0.00, 91.30) |
| U1 | E07-433M20S_A | F.Cu | (26.00, 77.73) |
| U19 | TPS63020 | F.Cu | (29.21, 60.45) |
| U2 | E07-433M20S_B | F.Cu | (49.30, 77.73) |
| U20 | TPS61232 | F.Cu | (36.21, 60.45) |
| U21 | ME6211 | F.Cu | (41.21, 60.45) |
| U22 | TPS22918_A | F.Cu | (36.14, 51.75) |
| U23 | TPS22918_B | F.Cu | (60.30, 77.73) |
| U24 | TPS22918_N | F.Cu | (39.25, 22.75) |
| U25 | TPS22918_L | F.Cu | (66.67, 57.21) |
| U3 | Ra-01SC_SX1262 | F.Cu | (54.67, 57.21) |
| U37 | TSOP38238 | F.Cu | (73.52, 86.39) |
| U4 | E01-2G4M27SX | F.Cu | (27.25, 27.75) |
| U40 | W25Q256JVEIQ | F.Cu | (30.00, 125.00) |
| U41 | APS6404L-3SQR | F.Cu | (50.00, 125.00) |
| U42 | DS3231MZ+ | F.Cu | (50.00, 115.00) |
| U43 | ICM-20948 | F.Cu | (50.00, 130.00) |
| U5 | ESP32-S3-WROOM-1U-N16R8 | F.Cu | (53.05, 25.00) |
| U6 | ESP32-C6-MINI-1U | F.Cu | (28.68, 98.69) |
| U7 | MDBT50Q-nRF52840 | F.Cu | (63.50, 97.33) |

### TOP — 117 components

| Ref | Value | Layer | Position (mm) |
|-----|-------|-------|----------------|
| BZ1 | Buzzer | B.Cu | (40.00, 60.00) |
| C1001 | 10uF_IN | B.Cu | (8.00, 108.00) |
| C1002 | 10uF_OUT | B.Cu | (20.00, 108.00) |
| C1003 | 1uF_BST | B.Cu | (8.00, 105.00) |
| C1004 | 100nF_BYP | B.Cu | (20.00, 105.00) |
| C1005 | 100nF_FG | B.Cu | (8.00, 112.00) |
| C1012 | 100nF_USB3_AVDD | B.Cu | (34.00, 118.00) |
| C1013 | 10uF_USB3_VDD33 | B.Cu | (46.00, 118.00) |
| C1014 | 100nF_USB3_DVDD | B.Cu | (38.00, 118.00) |
| C448 | 100nF_LS_NFC | B.Cu | (69.00, 39.00) |
| C501 | 100nF | B.Cu | (22.00, 23.00) |
| C511 | 100nF | B.Cu | (70.00, 62.00) |
| C512 | 100nF | B.Cu | (22.00, 36.00) |
| C521 | 100nF | B.Cu | (28.00, 42.00) |
| C531 | 100nF | B.Cu | (46.50, 38.00) |
| C532 | 1uF | B.Cu | (46.50, 42.00) |
| C541 | 100nF | B.Cu | (16.00, 37.00) |
| C601 | 100nF | B.Cu | (59.00, 39.00) |
| C602 | 10uF | B.Cu | (59.00, 45.00) |
| C611 | 1nF_TUNE | B.Cu | (71.00, 53.00) |
| C781 | 1uF_VDD | B.Cu | (10.00, 105.00) |
| C782 | 100nF_VSYS | B.Cu | (10.00, 108.00) |
| C783 | 4.7uF_VBUS | B.Cu | (10.00, 111.00) |
| C784 | 100nF_DEC | B.Cu | (18.00, 105.00) |
| C801 | 100nF_MUX | B.Cu | (34.00, 116.00) |
| C811 | 100nF_HUB | B.Cu | (36.00, 124.00) |
| C813 | 22pF_X1 | B.Cu | (44.00, 124.00) |
| C814 | 22pF_X2 | B.Cu | (46.00, 116.00) |
| C901 | 10uF_EN | B.Cu | (20.00, 62.00) |
| C951 | 100nF_GPS | B.Cu | (73.00, 25.00) |
| C952 | 0.1F_SC | B.Cu | (73.00, 29.00) |
| C961 | 100nF_BAT | B.Cu | (20.00, 112.00) |
| C971 | 100nF | B.Cu | (22.00, 115.00) |
| C972 | 100nF | B.Cu | (58.00, 115.00) |
| C973 | 100nF | B.Cu | (22.00, 135.00) |
| C974 | 100nF | B.Cu | (64.77, 122.00) |
| D1 | SK6812_1 | F.Cu | (16.00, 115.00) |
| D2 | SK6812_2 | F.Cu | (64.00, 115.00) |
| D20 | 1N4148_BZ | B.Cu | (26.00, 65.00) |
| D21 | 1N4148_VIB | B.Cu | (54.00, 56.00) |
| D3 | SK6812_3 | F.Cu | (16.00, 135.00) |
| D4 | SK6812_4 | F.Cu | (64.00, 135.00) |
| D6 | LED_TX_Red | F.Cu | (64.00, 140.00) |
| D7 | LED_RX_Grn | F.Cu | (68.00, 140.00) |
| FB601 | 600R@100M | B.Cu | (69.00, 47.00) |
| FB901 | Ferrite_GPS | B.Cu | (73.00, 22.00) |
| J10 | JST_Battery | B.Cu | (4.25, 120.50) |
| J11 | USB-C_Port_1 | B.Cu | (20.00, 138.00) |
| J12 | USB-C_Port_2 | B.Cu | (36.85, 138.00) |
| J13 | USB-A_Port_3 | B.Cu | (66.30, 137.65) |
| J7 | FPC_Display_40p | B.Cu | (40.00, 12.00) |
| J8 | MicroSD_Card_Slot | B.Cu | (78.00, 100.00) |
| J_IB_T | B2B_Receptacle_30p | B.Cu | (5.00, 70.00) |
| L601 | 1.5mH_RFID | B.Cu | (71.00, 57.00) |
| L703 | 2u2_SW | B.Cu | (14.00, 105.00) |
| MH1 | M2 | F.Cu | (4.00, 4.00) |
| MH2 | M2 | F.Cu | (76.00, 4.00) |
| MH3 | M2 | F.Cu | (4.00, 136.00) |
| MH4 | M2 | F.Cu | (76.00, 136.00) |
| Q10 | 2N7002_Vibro | B.Cu | (54.00, 60.00) |
| Q11 | 2N7002_Buzz | B.Cu | (26.00, 55.00) |
| R1001 | 100k_ILIM | B.Cu | (8.00, 111.00) |
| R1002 | 10k_PROG | B.Cu | (20.00, 111.00) |
| R501 | 4k7_OE1 | B.Cu | (10.00, 23.00) |
| R502 | 4k7_OE2 | B.Cu | (10.00, 29.00) |
| R503 | 4k7_OE3 | B.Cu | (13.00, 29.00) |
| R504 | 4k7_OE4 | B.Cu | (22.00, 29.00) |
| R510 | 1k2_SDA | B.Cu | (34.50, 47.00) |
| R511 | 1k2_SCL | B.Cu | (34.50, 51.00) |
| R701 | 1k65_PROG | B.Cu | (14.00, 120.00) |
| R781 | 1k_ADDR | B.Cu | (18.00, 111.00) |
| R782 | 100k_RESET | B.Cu | (20.00, 105.00) |
| R811 | 27R_DP | B.Cu | (34.00, 112.00) |
| R812 | 27R_DN | B.Cu | (46.00, 112.00) |
| R851 | 5k1_CC1_M | B.Cu | (16.00, 132.00) |
| R852 | 5k1_CC2_M | B.Cu | (28.00, 132.00) |
| R853 | 5k1_CC1_D | B.Cu | (44.00, 132.00) |
| R854 | 5k1_CC2_D | B.Cu | (57.74, 121.00) |
| R861 | 22R_USB_DP | B.Cu | (16.00, 128.00) |
| R862 | 22R_USB_DN | B.Cu | (28.00, 128.00) |
| R871 | 10k_VBUS_H | B.Cu | (57.74, 122.75) |
| R872 | 47k_VBUS_L | B.Cu | (67.00, 122.00) |
| R901 | 100k_EN | B.Cu | (20.00, 58.00) |
| R961 | 470k_BAT_H | B.Cu | (26.00, 112.00) |
| R962 | 470k_BAT_L | B.Cu | (26.00, 115.00) |
| R971 | 220R | B.Cu | (10.99, 115.00) |
| SW1 | BTN_UP | F.Cu | (40.00, 119.00) |
| SW2 | BTN_LEFT | F.Cu | (31.50, 125.00) |
| SW3 | BTN_OK | F.Cu | (40.00, 125.00) |
| SW4 | BTN_RIGHT | F.Cu | (48.50, 125.00) |
| SW5 | BTN_DOWN | F.Cu | (40.00, 131.00) |
| U10 | AW9523_2 | B.Cu | (16.00, 33.00) |
| U11 | W25Q256 | B.Cu | (22.00, 42.00) |
| U12 | FT6236 | B.Cu | (40.00, 40.00) |
| U13 | SE050C1 | B.Cu | (10.00, 42.00) |
| U14 | ST25R3916 | B.Cu | (64.00, 42.00) |
| U15 | EM4095 | B.Cu | (64.00, 55.00) |
| U16 | TP4056 | B.Cu | (20.00, 120.00) |
| U17 | DW01A | B.Cu | (20.00, 115.00) |
| U18 | FS8205 | B.Cu | (14.00, 115.00) |
| U26 | TPS22918_NFC | B.Cu | (64.00, 36.00) |
| U27 | USB_Upstream_ESD | B.Cu | (30.00, 120.00) |
| U28 | USB3.2_Gen1_Hub_VL822 | B.Cu | (40.00, 120.00) |
| U29 | USB_Port1_ESD | B.Cu | (24.00, 132.00) |
| U30 | USB_Port2_ESD | B.Cu | (36.00, 132.00) |
| U31 | USB_Port1_ESD_B | B.Cu | (20.00, 128.00) |
| U32 | USB_Port2_ESD_B | B.Cu | (40.00, 128.00) |
| U33 | USB_Port3_ESD | B.Cu | (61.61, 121.95) |
| U34 | SD_Card_ESD | B.Cu | (70.00, 122.00) |
| U35 | ATGM336H | B.Cu | (64.00, 25.00) |
| U36 | PAM8302 | B.Cu | (26.00, 60.00) |
| U38 | BQ25798 | B.Cu | (30.00, 108.31) |
| U39 | MAX17048 | B.Cu | (8.00, 115.00) |
| U42 | STUSB4500 | B.Cu | (14.00, 109.50) |
| U8 | 74LVC125 | B.Cu | (16.00, 25.00) |
| U9 | AW9523_1 | B.Cu | (64.00, 64.00) |
| Y1 | 25MHz_USB_Crystal | B.Cu | (48.00, 120.00) |

---

### 5) Optional: automatische Checks (für Menschen / CI)

- `subzero-pcb-engine`: `pcb_parser` im Modus `full` mit `kicad-cli` (DRC + Courtyard).
- KiCad 10: SVG/GLB-Export für Mechanik/Review.

Die **Bewertung durch andere KIs** läuft über **Abschnitte A + B**; dieser Anhang liefert nur die **Faktenbasis**.

---

## D) Ergebnisse externer Reviews (2026-04-12)

Sechs Modelle haben den konstruktiven Review-Prompt bearbeitet (Architektur, Komponentenwahl, Risiken, Pentest-Vergleich).

### Gesamtnoten

| Modell | Note | Kernaussage (1 Satz) |
|--------|-----:|----------------------|
| ChatGPT (o3) | **7.0** | Architektonisch stark, aber Power-Pfad, RF-Koexistenz und Datenkonsistenz vor P4 klären |
| Gemini | **7.0** | Professionelles Power-Gating und DFM, aber VL822 USB3 ist EMI-Risiko → USB2-Hub erwägen |
| DeepSeek | **6.0** | Solides Fundament, TOP aber überladen; BQ25798 vs TP4056 bereinigen, 4 Layer evaluieren |
| Claude | **5.5** | Architektur-Split überzeugend, Feature-Dichte aber zu hoch; P4-Scope halbieren |
| VeniceAI | **6.0** | RF-Dichte auf 3–4 Module reduzieren, USB3→USB2 downgraden, thermische Planung fehlt |
| Grok | **7.6** | Stärkste Bewertung; MAIN/TOP-Split „einer der saubersten Dual-Board-Ansätze", P4 aber Platz-/EMI-kritisch |
| **Ø** | **6.5** | |

### Einstimmige Stärken (alle 6 Modelle)

1. **MAIN/TOP-Split** ist architektonisch sauber und produktreif
2. **Power-Chain** BQ25798 + STUSB4500 + MAX17048 ist professionell
3. **SE050C1** als echtes Secure Element differenziert von fast allen Mitbewerbern
4. **ESD-Schutz** auf allen Ports ist vollständig
5. **Power-Gating** via TPS22918 zeigt Systemverständnis

### Einstimmige Risiken / Kritik (alle 6 Modelle)

1. **TP4056 parallel zu BQ25798** — redundant/gefährlich; entfernen oder DNP
2. **P4 passt nicht auf aktuelles TOP B.Cu** — separates Board oder Scope reduzieren
3. **RF-Koexistenz** (6+ Module + USB3 auf 80×140 mm) ist das größte Langfrist-Risiko
4. **USB3-Harmonische vs GPS/NFC** — Abschirmung, Ferrite oder USB2-Downgrade nötig
5. **4-Layer-PCB für TOP** sollte vor P4 evaluiert werden

### Strittige Punkte (Modelle uneinig)

| Thema | Pro | Contra |
|-------|-----|--------|
| **VL822 USB3-Hub** | Grok, Claude: USP (Bandbreite für Capture/Replay) | Gemini, VeniceAI: EMI-Overkill → USB2 |
| **nRF24 + CC1101** | Grok: nötig für Kompatibilität | DeepSeek: Altlasten, modernisieren |
| **AW9523 ×2** | Grok: entlastet B2B clever | DeepSeek: Overkill, GPIOs reichen |
| **AT86RF215 in P4** | Grok: passt thematisch | Claude, DeepSeek: auf P5 verschieben |

### Konsens-Empfehlung (destilliert)

> **P3 stabilisieren:** TP4056 raus, Thermik prüfen, DRC sauber, Doku synchron.  
> **P4 reduzieren:** RP2040 + DS2482 + CC2400 + MAX3232 realistisch; DW3000 + AT86RF215 → P5 oder Mezzanine.  
> **TOP auf 4 Layer** evaluieren, bevor P4 dazukommt.  
> **USB3-Hub-Entscheidung** treffen: entweder Abschirmung + Ferrite **oder** Downgrade auf USB2-Hub.

## Related

- [[SubZero-PCB-Prototypes]]
- [[SubZero-Engine-and-Dashboard]]
- [[Workspace-Repo-Map]]

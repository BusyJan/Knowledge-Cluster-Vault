---
type: project
title: "ESP32 LiPo Devboard (atopile trial)"
slug: "lipo-devboard"
status: active
created: "2026-04-20 10:33:22"
updated: "2026-04-20 10:35:00"
repo: ""
tags: [project, atopile, hardware-as-code, trial]
---

# ESP32 LiPo Devboard (atopile trial)

## Current goal

Trial atopile (Hardware-as-Code) parallel zu SubZero, um zu evaluieren ob neue Hardware-Projekte in atopile statt KiCad-direct entwickelt werden sollten.

## Key insights

- atopile generiert KiCad-PCB aus 273 Lines `.ato` Code in 14 Sekunden mit echten JLCPCB Part-Numbers im BOM (auto-pickr) und automatischen Datasheet-Downloads.
- Standard Library deckt 90% der Generic-Components ab (Resistor, Capacitor, LED, USB_C, FixedLDO, I2C, ElectricPower).
- Für konkrete LCSC-Parts mit speziellen Pinmaps (USB-C-Connector, LDO IC) muss `ato create part` verwendet werden — einmal pro Part-Typ, dann reusable.
- Module-Komposition (DecouplingTriple, BootResetCircuit, StatusLED) macht Reuse trivial — gleicher Code wiederverwendet in jedem Projekt.

## Current state

- 4 Module (power, mcu, peripherals, main) erstellt und gebaut.
- `ato build` erfolgreich, 14 Komponenten im BOM mit echten JLCPCB-Parts.
- KiCad-PCB generiert in `layouts/default/default.kicad_pcb`, Footprints alle vorhanden, Layout/Routing fehlt (das ist atopile's Default — User macht layout in KiCad GUI).
- Nächster Schritt: User entscheidet ob neue Hardware-Projekte in atopile gestartet werden, ob TP4056 Charger ergänzt wird, oder ob SubZero v2 Migration in atopile passieren soll.

## Quick links

- [[Notes]] — append-only log
- [[Summary]] — compressed knowledge
- [[Decisions]] — durable decisions
- [[Tasks]] — actionable items

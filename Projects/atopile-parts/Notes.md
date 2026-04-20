# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM`.

## 2026-04-20 11:35

- Insight: `ato create part --search <LCSC> --accept-single` lädt EasyEDA-Parts in 2-3s mit kompletter Toolchain (KiCad-Symbol + Footprint + 3D-STEP + Datasheet-URL + Pin-Mapping). Eine atomic component reusable in jedem zukünftigen Projekt.
- Context: Library `atopile-parts` als atopile-Package erstellt, enthält 5 atomic components (ME6211C33, TP4056, DW01A, Hroparts USB-C, ESP32-S3-WROOM-1-N8R8) plus 5 Wrapper-Module die clean ElectricPower/ElectricLogic Interfaces exposen. Architektur 2-Layer: `parts/` raw atomic components mit Hersteller-Pin-Namen, `modules/` saubere Wrapper für Endusers. Test im lipo-devboard erfolgreich: `ato build` in 12.46s erzeugt 22 echte Footprints im KiCad-PCB, BOM mit Real LCSC-Parts, alle Datasheets auto-downloaded.
- Problem: 3 Friction-Punkte: (1) DW01A LCSC-Code muss C351410 sein (nicht C82198 wie ich initial geraten); (2) FS8205A (Dual MOSFET für Battery Protection) hat keinen direkten LCSC-Code mit unseren Suchen — muss separat hinzugefügt werden; (3) Local-file deps werden gecached, brauchen `rm -rf .ato && ato sync --force` nach Library-Änderungen. Bonus: atopile fing einen ECHTEN Schaltungsbug (kurzgeschlossener Resistor in DW01A-Wrapper) zur Compile-Zeit mit klarer `Ercfault Shorted Interfaces` Fehlermeldung — das wäre in KiCad erst beim ERC oder schlimmstenfalls beim Test des Boards aufgefallen.
- Decision: Library-Pattern mit `parts/` + `modules/` als Standard für atopile-Projekte etabliert. Neue Parts werden mit `ato create part --search <LCSC> --accept-single` erstellt, dann ein Wrapper-Modul in `modules/` hinzugefügt. Library wird in jedem zukünftigen atopile-Projekt via `ato add file:///path/to/atopile-parts` (oder später via Git-Repository) eingebunden.
- Next step: Mehr Parts hinzufügen (ESP32-C6-MINI-1U, nRF52840, CC1101, SX1262, BME280, LSM6DSO, W25Q256, ATGM336H GPS, AW9523B IO-Expander, TSOP38238 IR, SK6812MINI-E NeoPixel) — die meisten SubZero-relevanten ICs. Nach kompletter Library: SubZero v2 in atopile bauen und gegen v1 (KiCad) vergleichen.

# Notes (append-only)

## 2026-04-14 14:30

- Insight: KiCad failed to load hierarchical sheets because `wire_schematics.py` inserted the generated block **after** `(sheet_instances)` / `(embedded_fonts)`; the parser then hit extra siblings and reported “Expecting ')'” and related errors. `strip_generated_block` using `rfind("\\n)")` was also unsafe.
- Decision: Strip/remove the marker block by cutting to `(sheet_instances` when present, else legacy close before `)`. Insert the generated block **immediately before** `(sheet_instances`. Drop `Intersheetrefs` from generated `global_label` (KiCad fills refs). Removed a few hand-placed UART labels with invalid `(at input|output …)` coords; re-ran live `wire_schematics.py` on all 14 sheets.
- Next step: Open `project-apex.kicad_pro` in KiCad 10 and run **Inspect → Electrical Rules Checker** on the root schematic.

## 2026-04-12 12:00

- Project stub created so **Graph Hub** and Dataview can list `project-apex`.

# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM` (legacy `## [YYYY-MM-DD]` may exist).

## 2026-04-14 19:58

- Insight: `project-apex` hierarchical schematics are treated as unreliable; a separate tree avoids inheriting that baggage.
- Context: Workspace path `ESP Projects/subzero-next/` with `subzero-next.kicad_pro` + minimal `subzero-next.kicad_sch` (KiCad 10).
- Problem: Need a clean schematic project without importing `project-apex/sheets/`.
- Decision: Greenfield project lives next to `project-apex/`; copy or symlink `project-apex/libs` only when libraries are needed.
- Next step: Open `subzero-next.kicad_pro` in KiCad, confirm ERC runs, then add sheets or symbols incrementally.

## 2026-04-14 21:30

- Insight: `subzero-next` can reuse Apex custom libs via `sym-lib-table` / `fp-lib-table` URIs `${KIPRJMOD}/../project-apex/libs/...` without copying files.
- Context: `project-apex/subzero-main.kicad_pro` and `subzero-top-fixed.kicad_pro` referenced missing `.kicad_sch` files.
- Decision: Added minimal stub `subzero-main.kicad_sch` and `subzero-top-fixed.kicad_sch` next to those projects so KiCad opens; replace with real schematics later.
- Next step: Choose whether new system design lives in `subzero-next` only, or flesh out the board-specific stub sheets and sync PCBs.

## 2026-04-14 22:00

- Problem: Symbol/footprint chooser empty — project only listed `project-apex`; standard libs came from **Global** table which was disabled.
- Decision: Replaced `subzero-next/sym-lib-table` and `fp-lib-table` with **merged upstream KiCad master tables** (same `${KICAD10_*_DIR}` layout as KiCad 10) plus `project-apex` at the end.
- Next step: Restart KiCad or reopen project; Place symbol should list Device, power, Connector, etc.

## 2026-04-14 14:30
- Insight: Three bugs in wire_schematics.py caused "wires not connected" ERC errors despite wires appearing on screen.
- Problem 1: Hidden pins were being wired. KiCad treats hidden pin positions as non-electrical endpoints; wires placed there create dangling wire endpoints (ERC errors). Fix: skip all pins where `pin["hide"] == True`.
- Problem 2: Multi-unit symbols stacked at the same position (74LVC125 U32 in rf-subghz) generated duplicate overlapping wires — 4 wires at identical coordinates, risking net shorts. Fix: deduplicate by tracking `seen_positions: set[tuple[float, float]]` and skipping already-processed world coords.
- Problem 3: `_label_rotation()` used x-position heuristic (left/right only), generating rot=0 for top/bottom pins. Fix: use `int((pin["rot"] + 180) % 360)` so GND→rot=270, VCC→rot=90, left→rot=180, right→rot=0.
- Decision: 74LVC125 overlapping units is a design issue (units should be placed separately as U32A–D); script now skips duplicates to avoid shorts, but physical separation still needed for correct ERC.
- Next step: Open subzero-next in KiCad, annotate, run ERC — expect significantly fewer errors.

## 2026-04-15 12:00
- Problem: After running wire_schematics.py, ERC showed 1630 warnings (GUI) / 2338 violations (CLI) with all wires and labels "unconnected". Root cause identified: (lib_symbols) section was EMPTY in all schematic sheets (version 20250901/kicad_symdir format). KiCad's ERC connectivity graph uses ONLY lib_symbols for pin positions — disk library is used for pin_not_connected but NOT for netlist-level connectivity. Empty lib_symbols → all labels appear "dangling", all wires appear with unconnected endpoints.
- Discovery: `label_dangling` in KiCad ERC means the entire NET has no component pins (semantic check), not just a positional check. Confirmed by minimal test schematic (wire + label: label_dangling even when wire endpoint touches it, until a component pin joins the net).
- Fix 1: Added `populate_lib_symbols()` function to wire_schematics.py that reads each used symbol from disk library and embeds its full definition in (lib_symbols). Handles extends (merges with parent), power symbols (reads actual library file, not stub). Result: 2338 → 171 violations.
- Fix 2: Wire format was wrong — (xy X1 Y1) and (xy X2 Y2) were on SEPARATE lines. KiCad 10 canonical format has BOTH on SAME line: `(xy X1 Y1) (xy X2 Y2)`. Fixed make_wire().
- Fix 3: Removed incorrect fallback pin for Device:C_Variable (had y=5.08, actual library has y=3.81). Removed fallback so library is read from disk.
- Fix 4: global_label format updated to match KiCad 10 native: added `(fields_autoplaced yes)`, `(property "Intersheetrefs" ...)`, proper `justify left/right` based on rotation.
- Final state: 11/14 sub-sheets completely clean (0 ERC violations). Remaining 171 violations: 124 endpoint_off_grid (cosmetic — pins at non-50mil grid), 35 label_dangling (hand-placed floating labels in original design), 3 isolated_pin_label (debug pins with no 2nd connection), 6 pin_not_connected + 3 power_pin_not_driven (floating power flag symbols in original design). All legitimate net connections are correctly established.
- Next step: Open subzero-next in KiCad, run ERC (expect ~170 warnings, 0 real connectivity errors), then proceed to netlist + PCB update.

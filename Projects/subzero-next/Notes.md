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

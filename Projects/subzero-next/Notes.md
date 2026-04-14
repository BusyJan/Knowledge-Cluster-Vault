# Notes (append-only)

Do not rewrite history. New entries use headings `## YYYY-MM-DD HH:MM` (legacy `## [YYYY-MM-DD]` may exist).

## 2026-04-14 19:58

- Insight: `project-apex` hierarchical schematics are treated as unreliable; a separate tree avoids inheriting that baggage.
- Context: Workspace path `ESP Projects/subzero-next/` with `subzero-next.kicad_pro` + minimal `subzero-next.kicad_sch` (KiCad 10).
- Problem: Need a clean schematic project without importing `project-apex/sheets/`.
- Decision: Greenfield project lives next to `project-apex/`; copy or symlink `project-apex/libs` only when libraries are needed.
- Next step: Open `subzero-next.kicad_pro` in KiCad, confirm ERC runs, then add sheets or symbols incrementally.

# Tasks

## Definition of done (schematic) — assistant-led

We treat **`subzero-next` schematic capture as finished** only when all of the following are true. Copy also lives at `ESP Projects/subzero-next/SCHEMATIC-FINISH-LINE.md`.

### Phase 1 — Integrity

- [ ] Project and every `sheets/*.kicad_sch` opens cleanly in KiCad.
- [ ] Flat merge includes every in-scope sheet, or exclusions are documented with a fix plan.

### Phase 2 — Electrical

- [ ] ERC **errors** resolved honestly (fix, waive in ERC with comment, or rule change with reason).
- [ ] Power strategy clear; undriven power inputs explained.
- [ ] Pin-to-pin / pin-type issues fixed or waived (not silently `ignore` without review).

### Phase 3 — Parts

- [ ] Symbols resolve; footprints assigned or explicitly DNP/TBD in a list.

### Phase 4 — Warnings

- [ ] ERC warnings triaged (fix, accept with note, or defer with note).

### Phase 5 — Handoff

- [ ] BOM export OK; critical nets sanity-checked; short design summary written.

**Status:** not finished until all phases complete (or user explicitly accepts “schematic beta” scope).

---

## Inbox

- [ ] Work through `SCHEMATIC-FINISH-LINE.md` in order; ask the assistant when a phase is unclear.

## Doing

- [ ]

## Done

- [x] Initialized project scaffold (2026-04-14)
- [x] Defined assistant-led schematic finish line (2026-04-16)

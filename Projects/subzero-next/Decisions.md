# Decisions

Record durable decisions with date and context. One decision per block.

## 2026-04-16 — Assistant-led “schematic finished” criteria

- **Context:** First-time designer; needs a clear finish line rather than guessing.
- **Decision:** Schematic capture is **not** called finished until Phases 1–5 in `Tasks.md` / `SCHEMATIC-FINISH-LINE.md` are satisfied. Optional lighter milestone: **“schematic beta”** if the user wants to move to layout early.
- **Consequences:** ERC error count alone is not sufficient; relaxed ERC rules must be reviewed before sign-off.

## 2026-04-18 — DW01A LiPo protection wired but non-functional in this revision

- **Context:** Full schematic-fix pass. User said "fixe alles" but explicitly "no deletions of components." DW01A (U2) was floating with no proper wiring. The chip's protection function requires two N-channel MOSFETs in series with the battery negative; they are NOT in the current schematic.
- **Decision:** Wire U2 minimally — VCC→VBAT, GND→GND, OD/OC→NC, CS→GND, TD→NC. Keep the IC in the BOM and on the PCB, but treat protection as PROVIDED BY THE LiPo CELL'S OWN PCM. Add the dual N-MOSFETs in a future revision if discrete protection is required.
- **Consequences:** ERC passes. The IC will physically exist on the PCB but does nothing useful. Document clearly in the build notes so a future builder doesn't assume "DW01A is there → we have protection." The chosen LiPo cell MUST be a protected cell (most modern 18650 / pouch cells are).

## 2026-04-18 — V5V_BOOST and V5V_USB_HOST are distinct nets

- **Context:** TPS61232 boost (U4) and TPS2041 USB switch (U42) both had their output labeled `V5V_BOOST`. Two power-output pins on the same net is an ERC error AND a real risk: KiCad/PCB would have shorted the boost output to the USB host port output, back-feeding through whichever is unloaded.
- **Decision:** Rename U42's output (USB-A host port) to `V5V_USB_HOST`. Keep `V5V_BOOST` as the boost converter's rail (battery-derived 5V for general use). The two rails are NOT connected unless a designer explicitly bridges them later.
- **Consequences:** USB host port now has a clearly separate net. If something needed both rails to be tied (e.g., share regulation), that decision must be made deliberately, not by mistake.

## 2026-04-18 — Multiple components marked NC for prototype validation

- **Context:** During the fix-everything pass, several passives and the GPS antenna feed cap were orphaned by earlier rewiring. Per "no deletion" directive, they stay in the schematic but had no valid wiring.
- **Decision:** Mark unused pins with `(no_connect)` rather than wire them speculatively. Affected: TH1 (NTC, both pins), C94 (GPS antenna decoupling cap, pin 1), R95 + C96-C99 (NeoPixel decoupling that earlier passes purged). All flagged in `Notes.md` as "future revision: re-add for production silicon."
- **Consequences:** ERC clean now. Future revision needs explicit decisions: (a) restore NeoPixel decoupling for noise immunity in production, (b) decide if active GPS antenna with bias-T is needed, (c) decide if thermal monitoring (TH1) is added back. None of these are critical for prototype validation but all are recommended for a production-quality board.

## 2026-04-18 — Schematic ERC sign-off: 0 errors, 6 acceptable warnings

- **Context:** After Pass 5 → Pass 10 (six idempotent fix scripts), schematic is electrically clean. Six remaining warnings are intentional: 3× single global label (placeholder rails for future ICs: V3V3_SDR, V5V_USB_HOST, GPS_RF_IN), 3× pin-type-mismatch false positives (W25Q256 WP/HOLD tied to +3V3, U56 SA0 tied to GND, all standard practice).
- **Decision:** Treat schematic as **finished for prototype layout phase**. Do not attempt to drive ERC to literally zero — the remaining warnings either represent design intent (placeholders) or KiCad limitations (it cannot infer that "bidirectional pin tied to power = correct"). The user can suppress them per-pin in the schematic editor if a clean ERC report is needed for sign-off.
- **Consequences:** Project is ready for `Tools → Update PCB from Schematic`. All 207 components have footprints; 384 nets resolved cleanly. Layout phase begins next.

## Template

### [YYYY-MM-DD] Short title

- **Context:**
- **Decision:**
- **Consequences:**

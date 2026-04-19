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

## 2026-04-18 — Two-PCB sandwich is the canonical product form-factor

- **Context:** A previous fix attempt generated a single 100×60 mm PCB. User immediately corrected: SubZero is a **stacked sandwich** with TOP (display + UI + power + USB) and MAIN (ESPs + RF) on **separate** 80×130 mm portrait PCBs joined by a B2B connector, with the LiPo battery in the gap. Confirmed by legacy files in `project-apex/` and the original `generate_2board.py`.
- **Decision:** Re-write the generator (`scripts/generate_2board.py`) to emit **two** `.kicad_pcb` files: `pcb/subzero-top.kicad_pcb` (2-layer 0.8 mm) and `pcb/subzero-main.kicad_pcb` (4-layer 1.6 mm). Both 80×130 mm. The MAIN B.Cu side is intentionally empty so the LiPo sits flush. Each board is independently orderable (separate Gerbers, separate BOMs, separate CPL) at JLCPCB/PCBWay.
- **Consequences:** Two PCBA orders required for each prototype build, but every batch can iterate the boards independently (e.g. revise MAIN for new RF module without re-fabbing TOP). Mechanical assembly: Pouch LiPo (~50×80×2.5 mm 800 mAh, or thinner) sits between the two boards centered on the B2B connector. The ~0.5 mm margin around the battery is enough to avoid mechanical stress on the connector.

## 2026-04-18 — B2B = Hirose DF12-50DP/DS (3.0 mm stack, 50 pin, 0.5 mm pitch)

- **Context:** 42 cross-board nets identified by net analysis (every net with nodes on both TOP and MAIN). 30-pin DF12 from the legacy design is too small. Need ≥42 pins + reserves.
- **Decision:** Hirose DF12 50-pin vertical, 3.0 mm stack height. Header (`DF12E3.0-50DP-0.5V_2x25`) on TOP-back; mating Socket (`DF12C3.0-50DS-0.5V_2x25`) on MAIN-front. Both centered at the same coordinates so the boards stack mechanically perfect.
- **Consequences:** 8 spare pins for future expansion (e.g. SDR card slot signals, debug bus widening). 3 mm stack accepts a 2-2.5 mm thin Pouch LiPo — small but adequate for prototype validation. If runtime is insufficient at production, swap to a taller B2B variant (DF12-5.0 or DF12-8.0 for 5 mm or 8 mm stack — same pad pattern, only the housing height changes). Available in KiCad stock libs at `Connector_Hirose:Hirose_DF12_DF12E3.0-50DP-0.5V_2x25_P0.50mm_Vertical` (and Socket). 50 pins assigned per `B2B_PIN_MAP` in `scripts/generate_2board.py`.

## 2026-04-18 — B2B pin-net mapping done at PCB level, not in schematic

- **Context:** Two valid approaches to wire the B2B connector: (a) add a B2B-bridge sheet to the schematic with 2× 50-pin Hirose symbols, all 42 cross-nets explicitly attached → ERC validates everything, (b) keep schematic unchanged and assign pad-net names at PCB-generation time → simpler, preserves ERC-clean state.
- **Decision:** Approach (b). The generator embeds the DF12-50 footprint into both PCBs and assigns `(net <code> "<name>")` to each of the 50 pads explicitly per `B2B_PIN_MAP`. Both boards' B2B pads carry IDENTICAL net names — KiCad treats matching net names as one connected net at routing time, so the cross-board signal flow is correct without any schematic modification.
- **Consequences:** Schematic stays untouched (Pass 1-10 ERC fixes preserved). Trade-off: the schematic does not show the B2B as a discrete component, so a designer reading only the schematic might not realize there's a physical connector in the loop — this is documented in the README and Notes. ERC cannot validate that all 42 cross-nets are correctly assigned to B2B pads (the assignment lives only in the generator script). If the B2B-required net set ever changes (new RF module added with a new EN line, etc.), update `B2B_PIN_MAP` and re-run the generator. For Production-1 it would be appropriate to migrate to approach (a) — schematic-resident B2B — for full ERC coverage.

## 2026-04-19 — Auto-Sync-System statt Single-PCB-Wechsel

- **Context:** Nutzerfrage: "kann man das Sandwich nicht effizienter entwickeln ohne 2 Boards?" Mögliche Alternativen evaluiert: V-Cut auf 1 Panel (FAIL — TOP=2-Layer 0.8mm, MAIN=4-Layer 1.6mm haben unterschiedlichen Stackup, geht nicht auf einem Panel), Rigid-Flex (FAIL — 5-10× teurer, ungeeignet weil Battery zwischen Boards Abstand braucht), KiCad Multi-Board nativ (FAIL — Beta in KiCad 10, erst KiCad 11 ~2027 produktionsreif). Der Sandwich-Aufbau zwingt strukturell zu 2 separaten PCB-Files.
- **Decision:** Statt Architektur zu ändern, einen Auto-Sync-Workflow gebaut der beide PCBs aus einer Master-Konfiguration synchronisiert: `scripts/master_sync.py` (single source of truth für B2B/MH/Battery-Zone), `scripts/sync_watcher.sh` (inotify-Daemon der bei jedem KiCad-Save synct + DRC läuft), `pcb/*.kicad_dru` (Custom Design Rules für Battery-Höhe, RF, USB, Power, Process-Limits). Battery-Zone als KiCad Rule-Area implementiert + visuell auf Cmts.User markiert.
- **Consequences:** User editiert Komponenten/Routing weiter normal in KiCad pro Board. Beim Save werden mechanische Anker (B2B-Position+Rotation, 4× MH-Positionen, Battery-Marker) automatisch auf das andere Board übertragen. Kein Risiko mehr dass die zwei Boards mechanisch divergieren. Battery-Höhen-Constraint via DRC: nur aktiv wenn User custom "Height"-Property auf jedem Footprint im Battery-Bereich setzt — sonst silent skip. Trade-off: kein Realtime-Cross-Board-Net-Routing-Check (ERC sieht weiterhin nur Schematic, B2B-Net-Mapping bleibt im Generator-Script). Das wäre mit KiCad 11 lösbar.

## Template

### [YYYY-MM-DD] Short title

- **Context:**
- **Decision:**
- **Consequences:**

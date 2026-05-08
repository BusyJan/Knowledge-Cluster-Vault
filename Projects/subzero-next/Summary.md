# Summary (compressed knowledge)

This file is the **compression layer**: distilled from [[Notes]], not a second log.

## How this stays small

- Recent work: summarized as bullets
- Older work: rolled into thematic bullets or pointers to [[Decisions]]

## Active themes

- **PCB → assembly:** personal rules file in repo `subzero-next/docs/PERSONAL-DESIGN-RULES.md`; SMA grid + silk DRC + roadmap in `docs/ASSEMBLY-READINESS.md`. Placement scripts: `fix_placement_sma_main.py` (uuid-safe `at` patch), `bump_f_silk_gr_text_sizes.py`, existing v4/v5.
- **Antennas (ship bundle):** **v1:** **TE Linx CW‑HWR `‑SMA`** (**433**, **868** on **LoRa/J13** CH default **ANT‑868**, **2.4** — three frequency SKUs, six antennas); **`ANTENNA-BOM-BASELINE.md`** §§0.3–1 + **§4** checklist (`answered` vs **`C6` 5‑6 GHz**, **Mechanik Ø**, **Compliance**); prefs `PLACEMENT-INTENT.md`.
- **Battery / power macro:** schematic snapshot (**TP4056**, **DW01A**, **LM66100**, **MAX17048**, **J2** pouch intent) documented in **`PLACEMENT-INTENT.md`**; **no user locks yet** — cell size, NTC, charge current vs thermal, lite SKU.

## Compressed history

- (Script or agent merges older [[Notes]] sections here during periodic compression.)

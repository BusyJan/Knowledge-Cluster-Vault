# Notes (append-only)

## 2026-04-14 14:30

- Insight: KiCad failed to load hierarchical sheets because `wire_schematics.py` inserted the generated block **after** `(sheet_instances)` / `(embedded_fonts)`; the parser then hit extra siblings and reported “Expecting ')'” and related errors. `strip_generated_block` using `rfind("\\n)")` was also unsafe.
- Decision: Strip/remove the marker block by cutting to `(sheet_instances` when present, else legacy close before `)`. Insert the generated block **immediately before** `(sheet_instances`. Drop `Intersheetrefs` from generated `global_label` (KiCad fills refs). Removed a few hand-placed UART labels with invalid `(at input|output …)` coords; re-ran live `wire_schematics.py` on all 14 sheets.
- Next step: Open `project-apex.kicad_pro` in KiCad 10 and run **Inspect → Electrical Rules Checker** on the root schematic.

## 2026-04-12 12:00

- Project stub created so **Graph Hub** and Dataview can list `project-apex`.
## 2026-04-15 16:16

- Insight: Established a reusable product-context brief for the public website and marketing copy: embedded/RF/security-research hardware with a light, friendly, Flipper-inspired site style and slightly technical monospace/spec-sheet accents.
- Context: Website direction discussed in chat. Device is matte black; site should stay light so product photos and 3D renders contrast well. Headless commerce structure remains in scope with marketing-focused home page and Shopify routes; hero copy uses NEXT_PUBLIC_PRODUCT_TAGLINE and NEXT_PUBLIC_PRODUCT_HERO_HEADLINE.
- Problem: Need a single prompt that gives AI collaborators and designers enough product, visual, legal, and website-structure context without inventing certifications or unsafe claims.
- Decision: Use an explicit fill-in template covering brand, hardware, firmware, audience, visuals, site structure, legal/ethics, and open questions. Keep authorized-testing language and avoid unverified compliance claims.
- Next step: When ready, fill the bracketed fields with final product name, tagline, hardware specs, legal entity/contact info, and any public-site exclusions before using the brief for copy or design work.
## 2026-04-15 16:20

- Insight: Created a filled SubZero product-context brief at project-apex/subzero-product-context.txt that combines hardware facts from the KiCad/prototype files with the current subzero-website frontend conventions.
- Context: The brief now captures proposed public naming/copy, supported hardware details, website route/env structure, legal/ethics constraints, and explicitly marks unknown business fields as TBD instead of inventing them.
- Problem: Website and copy work needed a single reusable prompt with enough context for AI collaborators or designers, but the source details were split across project-apex hardware docs and the separate subzero-website repo.
- Decision: Use the saved text brief as the master context document for future website tasks, with repo-backed technical facts preserved and marketing-only fields clearly labeled as proposed.
- Next step: Fill in the remaining business/public fields (domain, legal entity, contact info, launch constraints) and then use the brief to replace homepage placeholder copy/specs or generate docs/legal pages.
## 2026-04-15 20:45

- Insight: Estimated SubZero hardware cost ranges from the current BOM plus P3/P4 additions: roughly USD 180-260 in electronics/major accessories for the end-state unit, before labor/overhead; one-off assembled prototype likely lands around USD 320-550+ depending on sourcing and rework.
- Context: Estimate based on project-apex/bom/bom-lcsc.csv (107 line items, 202 total quantity) plus prototype README additions like STUSB4500, BQ25798, MAX17048, APS6404, DS3231, ICM-20948, RP2350A, DS2482, MAX3232, AT86RF215, CC2400, DW3000, display, battery, and 6 antenna pigtails.
- Problem: User asked for an end-cost calculation, but current repo BOM reflects an earlier/current hardware snapshot and does not include unit prices or all later prototype additions.
- Decision: Use a range-based estimate with clear buckets: electronics BOM, fab/assembly, and prototype-vs-batch differences; exclude certification, tooling, and development time from per-unit hardware COGS.
- Next step: Create a proper cost spreadsheet by assigning live supplier prices to each BOM line and adding missing P3/P4 parts, then split into one-off prototype, 10-unit pilot, and 100-unit batch scenarios.


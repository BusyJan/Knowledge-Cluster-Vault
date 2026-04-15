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
## 2026-04-15 20:48

- Insight: Product-line strategy should be flagship-first: launch SubZero as the halo product, then consider a SubZero Lite later as a deliberate second SKU once demand, cost drivers, and support burden are understood. A Nano only makes sense after a clear single-purpose use case emerges.
- Context: User asked whether it would be tactically smart to release a Lite/Mini later when hype fades or sales drop. Current hardware is feature-dense and expensive, so a lower-cost derivative could widen the funnel, but too-early SKU expansion would increase manufacturing, firmware, and support complexity.
- Problem: Need a commercialization strategy that extends product life without fragmenting the roadmap or turning the launch into three unfinished products.
- Decision: Do not plan Lite/Mini as a desperation reaction to falling sales; treat it as a pre-planned phase-two product. Use the flagship to build brand and validate which features users actually value, then remove the most expensive subsystems for Lite while keeping the same ecosystem/software feel.
- Next step: When hardware architecture stabilizes, define which modules are core vs optional so a future Lite SKU can drop costly radios/secure/peripheral blocks cleanly without rewriting the whole platform.
## 2026-04-15 20:50

- Insight: Product-line strategy: a later 'SubZero Lite' could be smart, but it should be planned as a deliberate second-tier product rather than a desperate reaction after hype fully collapses.
- Context: User asked whether launching a lighter/cheaper variant near the end of the hype or once sales drop would be tactically good. Strategic recommendation: use Lite to broaden the funnel, reduce BOM/cost barriers, and preserve the flagship's premium positioning.
- Problem: A flagship-only product can hit a ceiling on price and complexity; waiting too long to introduce a cheaper variant risks making it feel like a downgrade instead of a planned lineup expansion.
- Decision: Prefer a staged roadmap: flagship first for attention and brand identity, then Lite once the flagship is established and real usage data shows which features most users do not need.
- Next step: When product scope is clearer, define which modules/features are core vs premium so a future Lite can remove expensive radios, secure hardware, or peripherals without killing the main value proposition.
## 2026-04-15 20:55

- Insight: Pricing opinion: USD 399 is defensible for SubZero only if it ships as a clearly premium, polished flagship with strong perceived value beyond lower-cost handhelds like Flipper, Cardputer, or single-function RFID tools.
- Context: Compared against current market anchors: Flipper Zero around USD 199, HackRF/PortaPack class roughly USD 200-300+, Cardputer class around USD 20-30 dev-kit pricing, and cheaper RFID tools often under USD 100-170. SubZero aims to combine multiple functions, but USD 399 sits above impulse-buy territory and will require better industrial design, docs, UX, and clear feature justification.
- Problem: User asked whether 399 is too much relative to other handhelds.
- Decision: Treat 399 as a flagship price ceiling that can work for a niche enthusiast/professional audience, but expect it to feel too high for mainstream curiosity buyers unless the product looks and feels finished, differentiated, and trustworthy.
- Next step: Refine a pricing ladder: flagship around 349-399 if polished, with a future Lite target nearer the sub-200/sub-250 band if broader accessibility becomes important.
## 2026-04-15 21:14

- Insight: Clarified that USD 399 was not an internally derived requirement; it came from the user's hypothetical flagship price point. Production cost should be discussed separately as COGS, not inferred from target retail.
- Context: User asked why 399 was assumed and what the exact production costs would be. Current project data supports only estimate ranges because BOM export lacks live part prices, assembly quotes, freight, yield loss, enclosure/accessory quotes, and certification overhead.
- Problem: Retail price and unit production cost were being blended together in discussion, which can mislead pricing decisions.
- Decision: Treat 399 only as a candidate MSRP anchor. For now, present production cost as a range: rough assembled COGS likely around USD 220-300 for a polished batch unit, with exact figures unavailable until supplier and assembly quotes are collected.
- Next step: Build a proper cost model with line-item prices, PCB fab/assembly, display/battery/antenna/external parts, packaging, freight, and expected scrap/yield to determine true COGS and required MSRP.
## 2026-04-15 21:22

- Insight: Brand positioning should avoid 'best penetration testing tool' or 'better Flipper' framing. Stronger positioning is a premium handheld research platform / multi-radio field lab for authorized testing and hardware workflows.
- Context: User asked how SubZero should promote itself: best pentesting tool, or a more expensive/better Flipper. Recommended strategy is to avoid direct superiority claims and avoid language that sounds illegal, immature, or hype-driven. The product likely wins on integration, portability, workflow breadth, and premium execution rather than on a single benchmark.
- Problem: Aggressive positioning like 'best pentesting tool' invites legal/reputation risk and direct comparison traps against Flipper, HackRF, Proxmark, and SDR gear where expectations may not match the actual product story.
- Decision: Position SubZero as a serious handheld research platform for RF, embedded, and hardware-security workflows; emphasize authorized testing, field portability, multi-radio integration, and engineering quality. Treat Flipper comparison as an external reference point, not the core brand identity.
- Next step: Develop message pillars and tagline options centered on 'portable lab', 'multi-radio workflow', and 'research platform' rather than 'ultimate hacking device'.
## 2026-04-15 21:24

- Insight: A polished premium website and first-party webshop can be a meaningful differentiator for SubZero, but they are not by themselves enough to justify premium pricing; they need to reinforce a stronger product story and trust signal.
- Context: User asked whether being the only gadget with its own premium website and webshop would be a major differentiator. Strategic answer: strong DTC presentation helps credibility, conversion, and brand perception, but does not replace product-market fit or unique hardware value.
- Problem: There is a risk of overestimating the value of presentation alone versus the underlying product capability and positioning.
- Decision: Treat the premium website/webshop as an amplifier of premium positioning, not the core reason to buy. Use it to make the product feel trustworthy, polished, and worth understanding, while the hardware itself remains the main value driver.
- Next step: When website work resumes, make the site communicate seriousness, clarity, and trust rather than just looking expensive; tie visuals and copy directly to what SubZero actually enables.
## 2026-04-15 21:25

- Insight: Core product assessment: SubZero's idea is strong and genuinely differentiated, but the current hardware ambition is probably too broad for a first product if the goal is a polished, shippable flagship rather than an impressive engineering exercise.
- Context: User asked for an honest opinion on the hardware and core idea. The concept of a premium handheld multi-radio research platform is compelling, but the present scope combines too many subsystems, radios, MCUs, and supporting features at once.
- Problem: Over-scope risks delaying launch, inflating cost, hurting reliability, complicating firmware, and weakening the product story because the device tries to do too many things before proving one sharp value proposition.
- Decision: Treat the core idea as good, but narrow the first release to a smaller, more coherent feature set that feels excellent. Preserve the bigger vision for later revisions, modules, or higher-tier variants.
- Next step: Identify the 3-5 capabilities that define SubZero's identity and aggressively move the rest to later milestones or expansion products.
## 2026-04-15 21:31

- Insight: Base BOM review from bom-lcsc.csv suggests the current core hardware (without display, battery, antenna pigtails, later P3/P4 additions, PCB fab, or assembly) is roughly USD 76 in parts using rough small-batch pricing. The major real cost/complexity drivers are the RF stack, extra MCUs, advanced power chain, and later P4 expansion radios.
- Context: User asked for a grouped hardware list with price/functionality and which parts look overkill. Reviewed all BOM line items by class and compared them with planned P3/P4 additions from prototypes/README.md.
- Problem: The BOM export reflects an earlier/current snapshot and under-represents the eventual flagship cost because several expensive later-stage parts are not in the CSV.
- Decision: Treat core BOM as affordable on paper, but recognize the expensive scope creeps in through added radios, coprocessors, premium charging, secure parts, display/battery/antenna accessories, and manufacturing complexity. Overkill candidates for a first product include multiple overlapping radios, RP2350A, DS2482, MAX3232, secure-element upgrades, and SDR/UWB-class additions.
- Next step: If product scope is reduced, start cuts with P4 expansion radios and secondary peripherals before touching the core S3 + one companion radio + one or two strongest identity features.
## 2026-04-15 21:40

- Insight: Saved the recent product evaluation as durable guidance: the SubZero concept is strong and differentiated, but the current hardware scope likely exceeds what a first polished product should carry. Extra radios, extra MCUs, and premium subsystems are the main over-scope drivers; the path forward is to reduce scope without abandoning the larger vision.
- Context: User said this evaluation is very important but does not want to act on it immediately. They next asked whether the board design and code should be open source, noting strong SWE experience and AI-assisted development capacity.
- Problem: Need to preserve the strategic evaluation while the team continues exploring both hardware and software direction.
- Decision: Keep the evaluation as a reference point for future scope and roadmap discussions. Treat open-source strategy as a separate product/business decision rather than a direct consequence of the current over-scope assessment.
- Next step: When software architecture is clearer, decide separately which layers could be open (firmware, SDK, docs, hardware files) and which, if any, should remain proprietary for launch or commercialization.
## 2026-04-15 21:42

- Insight: Open-sourcing firmware does not automatically eliminate the need for secure hardware. Secure elements are still useful when the device must store secrets, protect identity, support attestation/pairing, or isolate sensitive credentials from extracted firmware and flash contents.
- Context: User agreed software can be public and asked whether that means security chips are unnecessary. Clarification: code visibility and secret storage are different concerns.
- Problem: There is a risk of conflating 'public source code' with 'no device secrets to protect', which could lead to removing hardware security that still supports trust and product integrity.
- Decision: Do not keep a secure element just because it sounds premium. Keep it only if SubZero truly needs on-device secret storage, signing identity, secure pairing, or credential isolation. If the product can function without device-held secrets, the security chip may be removable in v1.
- Next step: List all actual secret-bearing use cases (keys, pairing, encrypted storage, attestation, anti-clone, update trust) and decide whether each is real for v1 before keeping or cutting the secure hardware.
## 2026-04-15 21:46

- Insight: A dedicated USB coprocessor can still be justified even with open firmware, but for architectural reasons like concurrency, isolation, timing reliability, and recovery boundaries rather than for secret 'attack logic'.
- Context: User asked whether an extra BadUSB-oriented chip is beneficial because a single main MCU may only handle one action well at a time, while a secondary processor could manage USB interaction alongside wireless/control tasks. Discussion kept at high level for authorized testing context.
- Problem: Main MCU consolidation can create scheduling, latency, and reliability bottlenecks when one subsystem needs deterministic USB behavior while another handles UI, radio, storage, or orchestration.
- Decision: Evaluate extra coprocessors based on clear technical roles: deterministic IO timing, subsystem isolation, independent reset/recovery, and reduced firmware complexity. Avoid adding dedicated chips purely for vague capability stacking without a defined product need.
- Next step: Map each proposed coprocessor to a concrete systems role (USB device/host handling, radio offload, UI isolation, capture timing) and verify whether that role cannot be met acceptably on the primary MCU before keeping it in v1.


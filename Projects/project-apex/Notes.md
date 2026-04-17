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
## 2026-04-15 21:52

- Insight: Roadmap idea discussed: ship SubZero Main first, then likely introduce a cheaper Lite later; a broader family of specialized handhelds or a modular 'SubZero Stack' could be explored afterward, but modular stacking should not replace proving the flagship first.
- Context: User described a phased plan: release the flagship despite high price, maybe follow with Lite/Nano, and later possibly create either multiple purpose-built handhelds (sub-GHz, WiFi, Bluetooth, NFC, etc.) or a stackable modular platform using a more modern interconnect than simple exposed pin headers.
- Problem: There is a risk of turning one ambitious flagship into an even more complex platform strategy before the first product, pricing, audience, and strongest use cases are validated.
- Decision: Best near-term path is flagship first, likely Lite second, and only then evaluate whether the winning direction is specialized single-purpose handhelds or a modular stack ecosystem. A stack platform is strategically interesting but should be treated as a later ecosystem play, not a requirement for v1.
- Next step: After flagship validation, decide whether user demand points toward lower-cost derivatives, specialized vertical devices, or a shared modular platform with reused design language and common software/UI.
## 2026-04-15 21:56

- Insight: Strategic direction refined: Main and Lite are considered fixed releases; the real long-term branch point is now specialized single-purpose handhelds versus a stackable modular ecosystem. Recommendation leans toward the stack concept as the stronger differentiator, but only if v1 products are designed to be 'stack-ready' rather than forcing the full platform to exist immediately.
- Context: User clarified they definitely want SubZero Main and likely Lite. Their actual decision is between releasing many small specialized devices or building a true multi-module stack system where users can combine multiple modules at once behind a main display/control unit.
- Problem: A full modular stack is more differentiated than isolated handhelds, but it is also much harder mechanically, electrically, and operationally. Building it too early could turn product development into platform development.
- Decision: Prefer a staged approach: ship Main first, Lite optional/soon after, and architect both around a future stack bus/mechanical interface. Do not build many separate niche devices first unless the stack concept proves impossible or unnecessary.
- Next step: Define a future-proof stack interface spec early (power, data, alignment, module identity, physical envelope), but postpone the full ecosystem rollout until the flagship validates demand and UX.
## 2026-04-15 22:01

- Insight: Saved as high-priority long-term vision: after SubZero Main and likely a later Lite, build toward a genuinely stackable modular SubZero ecosystem with a shared software platform across devices/modules. User sees this as potentially even more brilliant than the flagship itself, but clearly as a future company phase rather than a present implementation target.
- Context: User stressed that the stacking concept is a future continuation of the company story, not the current focus. The long-term idea is a modular hardware ecosystem where a main handheld can accept multiple stackable modules, paired with a common modular software layer reused across products. Current reality: near-zero capital, highly founder-driven execution, and immediate focus on shipping SubZero Main first.
- Problem: Important strategic ideas can get lost while day-to-day focus stays on the flagship. This one matters because it defines a possible long-term moat and ecosystem direction, but it would be dangerous to pursue too early.
- Decision: Preserve the stack ecosystem and shared-software vision as a durable north star, while keeping present execution strictly focused on SubZero Main and later Lite if traction appears. Treat the stack platform as a phase unlocked only after flagship validation, funding, and operational maturity.
- Next step: When SubZero Main is more concrete, keep future stack-readiness in mind where cheap to do so (software architecture, branding, interface philosophy), but avoid forcing full modular-platform requirements into v1.
## 2026-04-15 22:03

- Insight: Release cadence preference clarified: full focus stays on SubZero Main first, but SubZero Lite should already be in development before Main launches so Lite can follow only a few months later rather than years later.
- Context: User wants Main to be the immediate focus, yet does not want a long gap before Lite. Desired strategy is effectively a staged rollout where Main launches first and Lite drops shortly after, with Lite already partially developed by the time Main releases.
- Problem: If Lite starts only after Main ships, the gap could become too long and momentum could die; but if Lite competes for too much attention too early, Main execution may suffer.
- Decision: Treat Lite as a shadow roadmap item during Main development: enough parallel planning/development to enable a fast follow-up launch, but not enough to dilute Main as the primary shipping target.
- Next step: When scope is clearer, define which hardware/software pieces are shared between Main and Lite so Main development naturally de-risks Lite and shortens the post-launch gap.
## 2026-04-15 22:06

- Insight: Lite strategy sharpened: SubZero Lite should be treated primarily as a cost- and scope-reduced derivative of Main, not as a separate invention. Main's shipped hardware/software/docs become the base; Lite mainly removes expensive or non-essential components and may downgrade selected peripherals like the display based on real user feedback and price targets.
- Context: User agreed that feedback from Main should flow into Lite and highlighted that the heavy lifting (files, architecture, core software base) already exists once Main is built. The main Lite work is selecting which components/features to remove or downgrade to hit a better price point.
- Problem: Without this framing, Lite could accidentally become a second large project instead of a fast-follow product derived from the flagship.
- Decision: Model Lite as a derivative SKU: reuse as much PCB logic, firmware, UI, docs, website, and manufacturing flow as possible; concentrate engineering on component selection, BOM reduction, and value-preserving simplification.
- Next step: When Main scope is more stable, explicitly tag every subsystem as core, optional, premium, or removable so Lite can be assembled as a disciplined subtraction exercise rather than a redesign.
## 2026-04-15 22:09

- Insight: Documentation principle elevated to a core rule: progress, milestones, iterations, decisions, setbacks, prototype evolution, and development story should be captured continuously, not reconstructed later. The value is not just engineering traceability but future storytelling, credibility, historical context, and publishable behind-the-scenes material that cannot be authentically recreated afterward.
- Context: User said this is incredibly important: document everything important about progress, not only code comments or formal technical docs, but the real development journey so it can later support public storytelling, internet sharing, company history, and unique non-reproducible knowledge artifacts.
- Problem: If progress is not captured in the moment, the most valuable narrative and process details are lost permanently and cannot be recreated accurately after the fact.
- Decision: Treat progress documentation as a first-class part of the project, not optional overhead. Preserve prototype evolution, rationale, milestones, and notable moments continuously because these records may later become strategic assets for branding, trust, and storytelling.
- Next step: Keep appending durable progress notes during project work and, when useful, maintain richer milestone logs or media-ready summaries that can later be adapted into public devlogs, launch storytelling, or company history.
## 2026-04-15 22:15

- Insight: Early brand/privacy direction matters alongside hardware: user wants strong anonymity, company-style 'we' voice without exposing the solo founder, a cryo-themed brand, a separate GitHub identity, early domain decisions, and a logo system built around an ice-crystal form.
- Context: Discussion covered privacy-first public positioning, naming, domains, GitHub, and logo strategy while website work is already underway. Key cautions: avoid fake team bios, treat 'we' as brand voice rather than fabricated staff narratives, keep product and company naming legally checkable, and note that 'SubZero' and 'Frostbite' may carry trademark risk in some contexts.
- Problem: Brand, naming, and identity choices made too late can create inconsistency, privacy leaks, domain loss, and weak marketing foundations while hardware/software are already progressing.
- Decision: Use a company/studio voice without personal exposure; prefer a unique company brand (e.g. KR1O/Cryo-derived) separate from product naming; secure a brandable domain early after a basic trademark/domain sanity check; create a separate GitHub org/account under the brand; and keep the current complex snowflake as a secondary emblem while developing a simpler primary mark for favicon, silkscreen, packaging, and recognition.
- Next step: Before locking the website, shortlist 3-5 company names and 3-5 domains, run basic availability/trademark checks, and define a simple brand system: company name, product name, org handle, primary logo, secondary emblem, and public voice guidelines.
## 2026-04-15 22:22

- Insight: Naming preference clarified: user strongly wants to keep 'SubZero' (or stylized variants like sub0/sub-zero) as the product name because it feels right and has already become central in thinking/talking about the device. Software naming could potentially follow a related pattern such as 'SubZero Frostbite' or a similar family convention.
- Context: User emphasized that despite earlier brand-structure discussion, the product name itself is something they would very much like to retain. This should be treated as an important identity preference, even though legal/trademark checks may still be necessary.
- Problem: Strong emotional/product identity around a name can conflict with later brand architecture or legal availability if not acknowledged early.
- Decision: Preserve SubZero as the preferred product-name direction for now, while still separating product naming from company/studio naming and flagging trademark/domain checks as necessary before final lock-in.
- Next step: Keep exploring company/brand names separately from the product name, and later verify whether 'SubZero' or a stylized variant is legally/practically safe to use in the intended markets.
## 2026-04-15 22:24

- Insight: Company naming question narrowed: strongest direction is to keep 'SubZero' as product line and choose a separate company/studio name built around KR1O/Cryo. Current recommendation favors a clean, privacy-friendly, extensible parent brand such as 'KR1O Labs'.
- Context: User asked directly what to call the company after affirming they want to preserve SubZero as the product name. Advice should keep product and company naming separate for flexibility, privacy, and future ecosystem growth.
- Problem: Using the product name as the company name risks legal/name conflicts and limits future expansion beyond a single device family.
- Decision: Recommend a short parent brand with cryo/KR1O DNA, with 'KR1O Labs' as the leading option and a few backup candidates in the same style.
- Next step: Shortlist 3-5 final company names, then check domain, GitHub org, and basic trademark availability before locking the website branding.
## 2026-04-15 22:25

- Insight: Company-name variation considered: 'KR1OTECH' / 'KR1O Tech' is viable and fits the alias, but it feels more generic and slightly less premium/distinctive than 'KR1O Labs'.
- Context: User asked specifically about KR1OTECH as the company name. This is relevant to upcoming website, GitHub, and domain choices.
- Problem: Need to distinguish between names that are technically usable and names that create the strongest brand impression.
- Decision: Treat KR1OTECH as a solid backup option, especially if domain/handle availability is better, but keep KR1O Labs as the stronger creative recommendation unless practical constraints force otherwise.
- Next step: Compare KR1O Labs vs KR1OTECH on domain availability, GitHub handle availability, and visual brand feel before locking the company identity.
## 2026-04-15 22:26

- Insight: Naming readability point: KR1O is stronger than KR10 for branding because the intended reading ('Krio' / 'Cryo'-adjacent alias) is clearer and feels more deliberate, while KR10 is more likely to be read literally as 'K-R-ten'.
- Context: User asked whether the brand should use KR10 or KR1O. This affects pronunciation, memorability, logo design, and handle/domain clarity.
- Problem: Numeric substitutions can either create a distinctive identity or make the name harder to parse and remember.
- Decision: Prefer KR1O over KR10 for company/brand naming unless practical availability constraints force otherwise.
- Next step: When checking domains/handles, prioritize KR1O-based variants first and only fall back to KR10 if availability or legal issues make KR1O unusable.
## 2026-04-15 22:30

- Insight: Brand direction now has a concrete preferred structure: company/studio name 'KR1O Labs' and product presentation along the lines of 'SubZero by KR1O Labs'.
- Context: User said KR1O Labs feels right and explicitly liked the framing 'SubZero by KR1O Labs'. This is a meaningful naming decision for website copy, GitHub org, domain selection, and public brand voice.
- Problem: Brand choices can drift if they are not recorded as soon as they start feeling 'real' to the founder.
- Decision: Use KR1O Labs as the leading company/studio name direction for now, while keeping SubZero as the preferred product name and 'SubZero by KR1O Labs' as a strong presentation pattern.
- Next step: Carry this naming structure into future website, GitHub, and domain decisions, then later validate availability and legal/trademark constraints before final lock-in.
## 2026-04-16 07:20

- Insight: Current snowflake/ice-crystal logo direction is visually strong, memorable in mood, and highly on-theme for SubZero/KR1O Labs, but the mark is probably too detailed/complex to serve as the only primary logo across favicon, PCB silkscreen, small packaging, and rapid recognition contexts.
- Context: User asked for an opinion on the provided cyan crystal logo. Assessment: strong secondary emblem / hero mark, but likely needs a simplified primary mark or reduced-detail variant for practical brand use.
- Problem: Highly intricate symbols can look impressive at large size yet become hard to distinguish, remember, or reproduce cleanly at small sizes.
- Decision: Keep the current crystal as an important visual asset and stylistic reference, but plan a simpler primary logo derived from it for small-scale and high-recognition use cases.
- Next step: When branding work resumes, create at least two variants: a simplified master mark and the existing detailed emblem for hero/marketing art.
## 2026-04-16 07:24

- Insight: Logo refinement guidance: the crystal mark becomes even more sensitive to over-detail in black-on-white usage. The core shape is strong, but simplification should preserve the six-point crystal silhouette while reducing interior cuts, micro-spikes, and visual noise so the mark stays recognizable in small monochrome contexts.
- Context: User said the logo will likely end up black on white and also feels somewhat too complex. Practical branding implication: monochrome use cases will expose complexity more harshly than the current cyan-on-black presentation.
- Problem: Detailed marks can feel impressive in a hero treatment but lose clarity and distinctiveness once converted to flat monochrome, favicon, silkscreen, packaging, or tiny UI contexts.
- Decision: Keep the current emblem as the expressive/high-detail version, but derive a simpler primary mark optimized for black-on-white use with stronger negative space, fewer internal cuts, and cleaner geometry.
- Next step: When logo work resumes, create a 3-tier system: hero emblem, primary simplified mark, and tiny icon/favicon variant.
## 2026-04-16 15:39

- Insight: Display direction recommendation: for SubZero Main, prefer a high-quality modern screen over a deliberately pixel-like display. The product is being positioned as premium, technical, and more serious than toy-like handhelds; a good screen supports that identity much better.
- Context: User asked whether the device should use a high-quality screen or a pixel-like screen. This is both a hardware and brand decision because the screen strongly influences perceived quality, UI clarity, and differentiation from retro-gadget aesthetics.
- Problem: A pixel-style display may be charming and cheaper, but it risks making the device feel more novelty/retro/toy-like, which clashes with the desired premium research-tool positioning.
- Decision: Recommend a high-quality screen for Main. A lower-cost or more playful display style could be considered for Lite/Nano later if needed, but the flagship should feel crisp, modern, and premium.
- Next step: Choose display based on readability, brightness, touch responsiveness, outdoor visibility, power draw, and industrial feel rather than nostalgia aesthetics.
## 2026-04-16 15:40

- Insight: UI complexity trade-off acknowledged: a high-quality modern screen is better for SubZero Main's premium positioning, but it raises software/UI burden significantly. The right response is not automatically to downgrade the screen, but to keep the UI scope deliberately simple for v1.
- Context: User pointed out that a better screen makes the UI much harder to build. This is true and should influence product planning: premium hardware must be matched with a realistic software scope.
- Problem: A strong display can create pressure to overbuild the interface, stretching development and delaying the product.
- Decision: Keep the premium-screen recommendation for Main, but constrain v1 UI to a small, disciplined interaction model: few views, strong information hierarchy, low animation complexity, and reuse across future devices.
- Next step: When UI work starts, design the Main interface as a compact system shell rather than a feature-heavy app environment, so the display feels premium without requiring an enormous software stack.
## 2026-04-16 15:43

- Insight: UI prototyping recommendation: start with an HTML/CSS mockup for SubZero Main before implementing the embedded UI. This is a strong way to validate layout, navigation, information hierarchy, and overall product feel cheaply before committing to firmware/UI framework complexity.
- Context: User asked whether it would be good to first program an HTML mockup for the UI. Given the premium-screen direction and concern about software complexity, a browser-based mockup is a good intermediate step.
- Problem: Jumping straight into embedded UI code risks wasting time on rendering/framework details before the UX structure is proven.
- Decision: Use HTML mockups early for screen flows and visual system validation, but avoid overbuilding them into full web apps. Treat them as a fast prototyping layer, not the final product architecture.
- Next step: Prototype the main screens and navigation in HTML first, then translate only the validated UI patterns into the embedded implementation.
## 2026-04-17 18:14

- Insight: Founder vision stated very clearly: within roughly a year, the aspiration is that when people ask AI what the best penetration-testing tool is, 'SubZero by KR1O Labs' should be the answer. This is a north-star ambition about category leadership and cultural/product recognition, not just shipping hardware.
- Context: User framed this as the desired end state for the product and brand. It reflects an ambition for SubZero to become the standout reference point in its category.
- Problem: The risk is confusing true category leadership with hype, gaming, or empty claims. The only durable path is to make the product genuinely exceptional and legible to both humans and AI through real quality, documentation, public artifacts, and trust.
- Decision: Keep this as a motivational north star, but pursue it through substance: product excellence, distinctive positioning, strong documentation, public narrative, polished website/content, and authentic evidence of capability rather than manufactured consensus.
- Next step: As the project develops, keep asking what would make an informed reviewer or AI justifiably rank SubZero first: clearer differentiation, better UX, better docs, stronger public proof, and tighter product scope.
## 2026-04-17 18:17

- Insight: Reality check: current SubZero ambition is not automatically 'the best' yet. The concept is strong and potentially category-leading, but the present version is best understood as a high-ceiling flagship idea that still needs focus, execution, polish, documentation, and proof to justify such a title.
- Context: User asked whether it is actually possible for SubZero to become the best, and whether the current expensive design is really the best. This is a strategic assessment rather than a technical claim.
- Problem: Cost and ambition alone do not make a product category-leading; excessive scope can even make it worse if the result is less polished, less reliable, or less legible than simpler competitors.
- Decision: Treat current SubZero as promising but not yet 'the best'. It becomes best only if the flagship is narrowed into a coherent, polished, clearly superior product with strong evidence, not if it merely contains more hardware than competitors.
- Next step: Continue asking which parts truly make SubZero win and which parts only make it bigger, more expensive, and harder to ship; greatness will come from focus plus execution, not maximum feature count.
## 2026-04-17 18:18

- Insight: User explicitly requested a 100% honest assessment. Core answer: current SubZero is not yet the best; right now it is an ambitious, high-potential concept that could become exceptional, but only if scope is reduced and execution quality becomes the real differentiator.
- Context: This was a direct ask for brutal honesty after discussing whether SubZero could become the answer to 'best penetration testing tool'.
- Problem: There is a danger of letting ambition be mistaken for achieved product quality.
- Decision: Keep giving reality-based guidance: treat current SubZero as promising but over-scoped, and define 'best' by focus, polish, trust, and usability rather than by maximum feature count.
- Next step: Continue evaluating every hardware/software choice against one question: does this make Main more recommendable, or just bigger and harder to ship?
## 2026-04-17 18:19

- Insight: Important product distinction: wanting a 'Swiss army knife that can do anything' is not inherently wrong; the over-scope problem appears when too many capabilities must all be excellent, affordable, reliable, and shippable in the first release. Vision breadth is fine, but v1 execution still needs a narrower success condition.
- Context: User asked why the product is considered over-scoped if the goal is explicitly a Swiss-army-knife device. This clarifies that multifunction ambition and over-scope are related but not identical.
- Problem: A multifunction product can fail if the first release tries to make every blade equally mature at once, creating cost, complexity, and polish issues that weaken the overall experience.
- Decision: Keep the Swiss-army-knife vision as the right long-term identity, but define a smaller v1 set of blades that are truly excellent; the rest can exist in reduced form, experimental form, or later revisions.
- Next step: For Main, rank every subsystem by whether it is core to the 'Swiss army knife' identity or just expanding scope, then focus the first release on a smaller number of standout capabilities.


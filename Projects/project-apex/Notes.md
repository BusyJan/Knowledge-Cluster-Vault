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
## 2026-04-18 11:46

- Insight: Display-selection context consolidated: the strongest current mechanical baseline for SubZero is the 2-board stacked format with identical TOP and MAIN boards at 80 x 140 mm, centered around a 60 x 140 x 4 mm Li-Po battery zone. Earlier assembly notes still mention ~120 x 80 mm as an adjustable board outline, but the prototype series and current product context consistently point to the 80 x 140 family as the active direction.
- Context: User asked for the whole project context plus the current size so a display can be selected. Relevant files: prototypes/README.md, subzero-product-context.txt, and assembly-notes.md.
- Problem: Display choice depends on the real active board family, and older notes contain at least one outline figure that could confuse selection.
- Decision: Treat 80 x 140 mm portrait-oriented TOP/MAIN boards as the current primary size baseline for display search, while noting that final visible display window and keepout still depend on top-board layout and UI/button placement.
- Next step: When display sourcing starts, evaluate portrait-friendly modules against the 80 x 140 TOP board, central battery/mechanical constraints, touch controller compatibility, FPC routing, brightness, and bezel footprint rather than relying on the older 120 x 80 placeholder note.
## 2026-04-18 13:24

- Insight: Target-audience and ethics framing clarified: SubZero should be positioned for authorized testing, research, protocol analysis, hardware labs, and advanced learning, while openly acknowledging that dual-use tools can be misused. The right response to critics is not denial but a serious stance on lawful, consent-based use, documentation, and responsible positioning.
- Context: User asked who the target audience is and how to explain the product to critics, noting that the device still has unethical potential. This is a durable messaging question for the website and brand voice.
- Problem: Dual-use hardware invites criticism if marketed carelessly or framed as a novelty 'hacking' tool. Pretending misuse is impossible destroys credibility; glorifying misuse destroys trust.
- Decision: Use a sober dual-use narrative: the device is built for researchers, labs, educators, and authorized assessments; like many security and RF tools, it can be abused, which is why the brand must emphasize consent, lawfulness, and serious documentation rather than edgy marketing.
- Next step: Turn this into a public-facing ethics block, FAQ language, and tone guidelines for the website so the product is explained consistently and credibly.
## 2026-04-18 18:33

- Insight: Confirmed the current six external antenna connectors in prototype-5: CC1101_A, CC1101_B, ESP32-S3 WiFi/BLE, nRF24, ESP32-C6 WiFi/BLE/802.15.4, and LoRa. GPS is not one of the six; it uses a separate 25x25 patch antenna on the TOP board. nRF52840 (MDBT50Q) uses its module antenna, and NFC uses an external coil rather than one of the six RF connectors.
- Context: User asked which six antennas the device currently has. Cross-checked bom-lcsc.csv with prototype-5 PCB outputs.
- Problem: Older BOM language mentions six u.FL antenna connectors generically, but the active prototype-5 PCB now names the actual RF assignments explicitly and uses edge-mount coax connectors in the layout.
- Decision: Use the prototype-5 mapping as the current authoritative answer for the six external antennas/connectors.
- Next step: When finalizing mechanicals, decide whether those six stay as SMA, revert to u.FL+pigtail, or mix connector types by radio class.
## 2026-04-27 11:24

- Insight: Industrial-design control discussion: a flatter all-metal input cluster with directional arrows, OK, and Back may be the better near-term choice than centering the hardware around a complex Adafruit-style rotary encoder, especially if the encoder mechanism is hard to engineer reliably. The encoder concept is attractive, but manufacturability and mechanical simplicity may matter more for v1.
- Context: User shared a render showing a handheld with a central ANO-style control cluster and asked whether to use an Adafruit-style rotary encoder or instead a flatter rotary wheel / arrow buttons / OK / back arrangement. The concern is that the more complex encoder may be difficult to engineer and manufacture.
- Problem: A signature input device can improve identity, but if it adds too much mechanical complexity, tolerance risk, cost, or assembly pain, it can damage the first product more than it helps.
- Decision: Favor the simpler, flatter, more manufacturable control solution for v1 unless the rotary encoder is truly core to the product feel and can be implemented robustly without becoming a major mechanical bottleneck.
- Next step: When UI/input design is narrowed, choose the control scheme that minimizes mechanical risk while still feeling premium: likely either a flat metal wheel plus separate buttons, or a simpler directional-pad style cluster with excellent tactile quality.
## 2026-04-27 11:26

- Insight: Input-control decision under consideration: either keep the older Adafruit-style rotary encoder approach or move to a flatter metal control system combining a rotary wheel/encoder with directional arrows, OK, and Back. Initial product judgment: the flatter metal concept can look more premium and manufacturable if executed cleanly, but the older simpler control may still be more efficient and lower-risk for v1.
- Context: User shared a SubZero vision render showing a 3.5 inch TFT with a central rotary/4-way/OK control and separate back button, and asked whether a flatter all-metal control scheme would be better given that the Adafruit rotary encoder may be harder to engineer and manufacture.
- Problem: Input hardware is both a UX-defining choice and a mechanical/manufacturing risk. A more premium-looking control can also introduce precision, feel, tolerance, durability, and firmware complexity challenges.
- Decision: Do not switch purely for appearance. Judge the flatter metal control by whether it preserves fast one-handed navigation and can be built reliably. For Main, the safer choice is whichever control system gives strong tactile feel, easy manufacturing, and low risk; the flatter concept is promising if it does not compromise usability.
- Next step: Before locking the design, compare both input systems on one-handed use, glove use, accidental presses, tactile clarity, assembly complexity, enclosure tolerances, and perceived premium feel.
## 2026-04-27 11:38

- Insight: Input-design alternative on the table: flat all-metal control cluster (flush brushed-metal rotary wheel + 4 flat arrow keys + flat OK in the wheel center + separate flat BACK button) instead of the Adafruit-style raised rotary encoder.
- Context: User likes the all-metal premium look and is worried the Adafruit-style encoder is harder to engineer/source/integrate cleanly into the matte black aluminum body. Flat metal cluster matches the same aesthetic family as the SubZero vision render and is closer to mass-manufacturable button stacks.
- Problem: Flat metal wheel without a real shaft encoder is hard to make feel as good as a true rotary encoder; capacitive/optical/magnetic flat wheels are doable but add BOM and tuning cost. Pure dome-switch arrows lose the fast-scroll feel that the rotary gives for spectrum browsing, file lists, frequency tuning.
- Decision: Do NOT decide on aesthetics alone. Keep the Adafruit-style rotary as the current favorite for SubZero Main v1 because tactile feel + reliable scroll matter for the core RF/pentest UX. Treat the flat all-metal cluster as a strong candidate for SubZero Lite/Nano (cheaper, easier to manufacture) and as a possible v2 of Main if a flat magnetic/optical encoder can be qualified.
- Next step: Build two cheap physical mockups (one with a real rotary, one with a flat wheel + arrow keys) and dry-run the actual UI flows: spectrum scan, frequency tuning, file browser, menu nav. Pick based on hands-on feel, not renders.
## 2026-04-27 11:41

- Insight: Input-design path lockdown: keep Adafruit ANO (Product 5001) as the mechanism for SubZero Main v1, but replace the visible plastic parts (outer ring, 4 directional pads, center cap) with custom CNC-machined anodized aluminum parts.
- Context: User wants the all-metal premium feel of the flat-cluster concept but does NOT want to lose the rotary encoder UX of the ANO. The ANO is internally a standard rotary encoder + 5-way switch, so only the visible plastic needs swapping.
- Problem: A fully custom rotary+nav module (Option B: EC11/EC12 + 4 tactile + center tact + custom metal ring on a sub-PCB) or an OEM custom build at ALPS/Bourns (Option C, MOQ 5k-10k, NRE 5-30k CHF) is over-scope for v1.
- Decision: v1 = Option A: source Adafruit ANO, measure with caliper, 3D-model custom aluminum caps + ring in Fusion 360, fab via PCBWay CNC / JLCCNC / Xometry in 6061 aluminum, anodized matte black with brushed finish to match the SubZero body. Treat Option B as v2 escape hatch if ANO ever becomes a supply risk.
- Next step: Buy 1-2 ANO units for measurement. Confirm finish choice (matte black anodized vs brushed gunmetal vs natural). Define unit-cost target so we can pick CNC supplier. Generate CAD pass-fit prototypes with 2-3 tolerance variants (0.05/0.075/0.1 mm clearance) and order a single test batch.
## 2026-04-27 11:48

- Insight: Created project-apex/docs/input-design-metal-nav.md - full brainstorm/design doc for the custom metal ANO encoder, including 3 design paths (A/B/C), Apple-Watch reference, CNC supplier shortlist, RFQ template, finish options, test plan, market price benchmarks, and verified ANO facts (8.95 USD, 7 GPIOs, iPod click-wheel inspired).
- Context: User wants a high-end all-metal ANO-style nav wheel, manufactured custom because no off-the-shelf metal version exists. Asked for productive brainstorming during a 10-minute break.
- Problem: Critical finding while cross-checking the design against project-apex/docs/pinmap.md: the ESP32-S3 has all 31 assignable GPIOs already allocated. Adding the ANO requires either reassigning IR/buzzer/SK6812 pins (regression risk), or routing the rotary encoder pins (ENCA/ENCB) through the ESP32-C6 over UART, or adding an I2C encoder coprocessor (Seesaw-style).
- Decision: Path A (CNC aluminum cap-set on stock ANO mechanism, Type III hard anodize matte black on 6061 aluminum) is locked as the v1 manufacturing approach. For GPIO integration, default plan is 13.2 = route ENCA/ENCB to the ESP32-C6 (which already has UART to S3) and add ANO Left/Right buttons on AW9523 #1 free pins. Updates required in pinmap.md, schematic, and C6 firmware design.
- Next step: Buy 1-2 ANO units for measurement, prototype the metal cap set in Fusion 360 with 3 tolerance variants (0.05/0.075/0.1mm clearance), update pinmap.md to reflect ANO + C6 routing, then prepare RFQ to PCBWay CNC / JLCCNC / Xometry using the template in section 9 of the doc.
## 2026-04-27 12:13

- Insight: Execution playbook for the custom metal ANO caps is now defined: 6 steps (order ANO -> measure -> CAD -> 3D-print prototype -> CNC prototype -> production), realistic 8-10 week timeline, total cost to first qualified set ~300-700 CHF.
- Context: User asked the practical 'how do we get the metal caps' question after agreeing on Path A (CNC alu over stock ANO). Created two new operational docs to enable parallel work without blocking other SubZero tracks.
- Problem: The user does not necessarily have CAD skill. Choosing between DIY in Fusion 360, hiring an Upwork freelancer (~150-400 CHF), or hiring a local CH/DE engineer (~300-800 CHF) is the next decision before week 3 of the timeline.
- Decision: Recommended freelancer route via Upwork to keep KR1O focused on hardware/firmware/website tracks in parallel. Created project-apex/docs/metal-caps-measurement-checklist.md and project-apex/docs/metal-caps-freelancer-brief.md so the moment the physical ANO arrives the user has a turnkey path. Suppliers ranked by CH delivery speed: Mouser CH > Digi-Key CH > Anodas (LT) > Pimoroni (UK) > Adafruit direct (US).
- Next step: User to order 2x Adafruit ANO 5001 (and optional breakout 5221) from Mouser CH today. While waiting for delivery, KR1O to decide CAD path (DIY vs Upwork freelancer vs local engineer) so the brief can be posted the day the parts arrive.
## 2026-04-27 15:43

- Insight: Major shortcut: Adafruit publishes a real engineering STEP file of the ANO encoder on GitHub (Adafruit_CAD_Parts/5221 ANO Rotary Encoder). 6234 lines, 1411 geometric primitives, full B-rep solid model originally exported via ST-Developer. Mirrored locally to project-apex/mechanical/ano-reference/.
- Context: User clarified they want OUTSOURCED production, not self-production, and pointed out that ANO dimensions are publicly available. The published STEP is even better than dimensions on paper — it gives the CNC vendor or freelancer the exact geometry to mate against, eliminating the physical-measurement step entirely.
- Problem: Original 8-10 week timeline assumed a measurement step (1-2 weeks for ANO shipping + reverse engineering). With the STEP file, that step disappears.
- Decision: Pivot to Modell 2 turnkey RFQ: send Adafruit STEP + a single design+machining brief to PCBWay or Xometry, they handle CAD AND CNC. Created project-apex/docs/metal-caps-turnkey-rfq.md as the ready-to-send RFQ. Buying physical ANOs is now optional and parallel-tracked (only needed for fit-testing prototype caps once they arrive).
- Next step: User to pick 2-3 turnkey suppliers (recommend PCBWay + Xometry CH/DE), upload the local STEP file plus the RFQ template, and request quotes. Compare quotes on cost AND on quality of clarifying questions from each supplier.
## 2026-04-27 16:02

- Insight: Brand-mark exploration session (logo design, Cursor/OpenAI level of simplicity). KR1O LABS company mark is locked at concept level: a vertical "ice crystal column" silhouette (solid black, single horizontal negative-space slit through the upper third) paired with a clean geometric sans-serif wordmark "KR1O LABS" — wordmark MUST use a typographic numeral "1" (not letter I, not crystal glyph) to preserve the deliberate KR1O reading (per 2026-04-15 22:26 decision). Vertical lockup + horizontal lockup both validated. Asset: assets/kr1o-labs-logo-v2.png (KR1O typography correct); v1 assets/kr1o-labs-logo-concept.png mis-rendered "1" as a crystal glyph (rejected, but kept as reference for the "crystal-as-1" creative variant).
- Context: User wanted simultaneous primary marks for both SubZero (product) and KR1O Labs (parent studio), explicitly at the simplicity level of Cursor / OpenAI / Linear / Vercel logos. Vibe brief: "extrem simpel, einfach identifizierbar". Existing detailed cyan-crystal mark and the user-supplied black six-point snowflake (assets/fr0stb1te-logo-8eab79e3-...png) remain as hero/marketing emblems only; both are still too detailed for primary-mark roles (favicon, PCB silkscreen, alu engraving) per the 2026-04-16 07:20 decision.
- Problem: SubZero primary mark is NOT yet locked. Multiple iterations explored and rejected: (a) simplified six-point sparkle starburst (read too "Christmas/sparkle emoji"), (b) chunky cut-crystal obelisk (too massive, slight Mercedes-Y risk on the internal facets), (c) thin-stroke variants — slim crystal / hex top-view / thin snowflake (too anemic, too line-art), (d) solid balanced variants — solid snowflake with hex core / solid hex with negative facets (user feedback: "zu komisch"). Six fresh concept pitches generated (assets/subzero-six-pitches.png): 01 "<0" math glyph, 02 angular S in hexagon, 03 frozen drop (came out football-shaped, not drop-shaped), 04 iceberg wedge with waterline, 05 pure hexagon, 06 thermometer. Strongest candidates: 04 (iceberg, narrative-loaded, premium, distinct), 01 (<0 glyph, intellectual, owns the brand name literally), 02 (S-hex, conventional badge, scales perfectly). Weakest: 05 (too generic), 06 (too consumer-tech), 03 (didn't render as drop). User skipped final selection — paused for thinking time.
- Decision: KR1O LABS mark direction (crystal column + wordmark with explicit "1") = locked at concept level, ready for vector recreation in Figma/Illustrator when finalization happens. SubZero primary mark = open, narrowed to top-3 candidates (iceberg / <0 / S-hex). Hero/marketing snowflake mark unchanged.
- Next step: User to choose between iceberg / <0 / S-hex (or pitch new direction) before any vector recreation. Workflow validated: generate visual mock first → critique honestly → iterate on user feedback → never finalize on AI-rendered raster (always recreate as proper vector once concept locked).
## 2026-04-28 10:15

- Insight: User-defined SubZero snowflake construction: one sharp faceted "arm" (arrow/spike + jagged side lightning) duplicated six times at 60° rotation around a center — mathematically clean radial symmetry, reproducible in any vector tool. Files: `assets/image-ca21f71e-03fc-41f1-8b1a-6188c74ae755.png` (single arm), `assets/image-d2b0f131-ecdb-4e37-8995-aa16f4c730aa.png` (four full marks differing only in center treatment).
- Context: User asked whether this modular approach is sound and how it reads for CRYO/SubZero vs earlier pitched concepts.
- Problem: At favicon/silkscreen sizes, interior white gaps and micro-spikes may merge or buzz; "tribal"/gaming sharpness may read edgier than "lab premium" unless tuned.
- Decision: None (design direction); construction method is valid. Center variants trade readability vs weight: small six-point star (lightest), larger star (unified), hex core (clearest "crystal lattice", scales well), diamond-petal hub (most ornamental BUSY in the middle).
- Next step: Pick one center + vectorize; optionally define a "simple" master (fewer jags or merged fills) for ≤24 px use while keeping the full detail for hero/packaging.
## 2026-04-27 21:37

- Insight: ANO STEP extraction: file is a 2-part assembly named Board:1 (breakout PCB) and Encoder:1 (encoder module). Hide Board, isolate Encoder, then use body browser or section views to recover plastic underside bore/boss mating for metal caps.
- Context: User asked how to extract only plastic parts, understand underside, replace plastic with metal, and whether proof exists.
- Problem: Plastic may be one fused body in CAD; underside must be read via section view + inner faces; physical ANO still needed to confirm snaps/removability.
- Decision: Documented workflow in project-apex/mechanical/ano-reference/README.md: Board vs Encoder isolation, underside inspection steps, fab print tsw.pdf cross-check, prototype as proof.
- Next step: When CAD starts: hide Board:1, section Encoder:1 axially, measure bore/boss; order 1 physical ANO to verify plastic removal and switch travel after metal swap.
## 2026-04-27 22:20

- Insight: Ordered 3× Adafruit ANO 5001 from pi-shop.ch for hands-on evaluation, spare, and potential teardown / metal-cap fit testing.
- Context: User proceeding with hardware purchase after discussion of feel matching and STEP reference.
- Problem: (none)
- Decision: 3 units: use split as test / experiment / backup.
- Next step: On arrival: verify rotation + all 5 directions + center; optionally compare to STEP; start tact-switch feel matrix vs ANO if breakout or temp wiring available.
## 2026-04-28 18:30

- Insight: Assistant-rendered recommendation mock for modular SubZero snowflake: same construction idea as user (one arm × 6 at 60°) but center locked to solid flat-top hexagon core for crystal-lattice reading and better small-size robustness; arm kept aggressive but slightly restrained jags. Raster reference only — vector rebuild from user master arm preferred. Asset: `assets/subzero-recommended-hex-core-snowflake.png`.
- Context: User asked for one image of what the assistant would pick vs their four center variants.
- Problem: AI render may not perfectly match user arm geometry; use as direction only.
- Decision: Favored hex-core variant over star-connected and diamond-petal hub for this recommendation pass.
- Next step: User compares mock to their vector builds; align or reject; then lock primary vs simplified tier.
## 2026-04-28 19:05

- Insight: Alternate SubZero snowflake arm explored: vertically symmetric faceted diamond/rhombus (white horizontal “fracture” band between taller upward triangle and shorter downward triangle; interior white facet lines for cut-gem / ice-shard read). File: `assets/image-55226c49-8d8d-4771-a42b-d143e36f7083.png`. Assessment: much cleaner and more “premium lab / jewel” than the jagged lightning-arm; scales better at small sizes; aligns visually with KR1O crystal-column DNA (facets, fracture); slight risk of reading as generic gem if the single arm is shown without the 6×60° snowflake context — full mark fixes that; loses a bit of aggressive “bite” vs the tribal arm (not necessarily bad for research-tool positioning).
- Context: User asked for opinion on this arm direction vs prior jagged modular arm.
- Decision: None — user chooses arm family; this variant is a strong candidate for primary mark + simplified tier with one fewer facet line if needed.
- Next step: Compose 6×60° + pick center (hex core vs star merge); compare full marks at 16 px and 8 mm silkscreen.

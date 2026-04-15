## 2026-04-15 12:00
- **Context:** User wanted to drop Tailwind and use another styling approach.
- **Decision:** Replaced `tailwindcss` + `@tailwindcss/typography` with **UnoCSS** (`unocss`, `@unocss/postcss`), `presetWind3` for Tailwind v3–compatible utilities, `presetTypography` for `prose`. PostCSS uses `@unocss/postcss`; `styles/globals.css` starts with `@unocss` instead of `@tailwind`. Removed `tailwind.config.ts`, added `uno.config.ts` (theme colors from former Tailwind extend). CMS page (`app/pages/[handle]/page.tsx`) no longer uses Tailwind Typography element modifiers (`prose-headings:*`, etc.); those rules live under `.shopify-page-body.prose` in `globals.css`.
- **Next step:** Run `npm install` in the repo to refresh `package-lock.json` (sandbox had no `npm`); then `npm run build` to verify.

## 2026-04-15 14:00
- **Context:** User wanted an empty storefront shell: remove dither background, hamburger menu, marquee banner, and see a blank site.
- **Decision:** Removed `DitherBackground` from `app/layout.tsx` and deleted `components/atoms/dither/*`. Removed `SmartHeader` (and `HamburgerMenu`) from `providers.tsx`; deleted `smart-header.tsx`, `hamburger-menu.tsx`, `marquee-banner.tsx`. Dropped `hooks/use-device-performance.ts` and `detect-gpu` dependency (only used by dither). Home `app/page.tsx` now returns `null`; removed `Footer` from root layout; deleted `home-cinematic-section.tsx` and `collection-showcase.tsx` (only used by home). Body background is solid black in `globals.css`. Cart drawer remains mounted but no header trigger until a new one is added.
- **Next step:** `npm install` (lockfile may need refresh after removing `detect-gpu`); `npm run dev` locally.

## 2026-04-15 16:00
- **Problem:** Runtime crash when `SHOPIFY_*` env vars missing — `lib/shopify/config.ts` threw at import time, which ran in the browser via `CartProvider` → cart → client → config.
- **Decision:** Export `isShopifyConfigured`; no throw at module load. `shopifyRequest` throws only when a GraphQL call runs without config. `CartProvider` skips cart bootstrap when not configured. `/api/health` reports Shopify unhealthy if not configured.

## 2026-04-15 18:00
- **Context:** Remove all references to the former brand name across the repo.
- **Decision:** Added `lib/site.ts` (`SITE_URL`, `SITE_NAME`, `LOGO_SRC`, `CROSS_SRC`) with `NEXT_PUBLIC_SITE_URL` / `NEXT_PUBLIC_SITE_NAME`. Updated metadata, JSON-LD, breadcrumbs, footer, CI/deploy workflows, `package.json` name, cookie event `store:show-cookie-banner`, password key `store_access_granted`. Public assets referenced as `/pictures/logo.svg` and `/pictures/cross.svg`. Removed legacy product redirect from `next.config.mjs`. Workflows use deploy dir `shopify-storefront-web` and PM2 `storefront-web` (server must match).

## 2026-04-15 20:00
- **Context:** User asked for a near 1:1 replica of `mortonslight.com` homepage (placeholder images), using Playwright screenshots to compare reference vs local.
- **Decision:** Added `@playwright/test` and `scripts/screenshot-pages.mjs` (`reference` / `local`, sets `shopify_analytics_consent` before navigation so the cookie modal does not block captures). `.gitignore` includes `.screenshots/`. Home is `components/mortons/mortons-landing.tsx` + `mortons-header.tsx` (Manrope + IBM Plex Mono, teal glow bands, alternating image/text blocks, white statement strip, ruled designer grid, large wordmark footer). Removed `IntroOverlay` from `providers.tsx` so the hero is visible on load. `package.json` scripts: `screenshot:reference`, `screenshot:local`.
- **Next step:** Run `npm run screenshot:reference` after design tweaks; local dev may bind to `3001` if `3000` is taken—set `PLAYWRIGHT_BASE_URL` accordingly.

## 2026-04-15 21:00
- **Context:** User asked to remove Mortons-specific branding and footer copy after the replica pass.
- **Decision:** Replaced `components/mortons/*` with `components/marketing/home-landing.tsx` + `home-header.tsx` (`HomeLanding`, `HomeHeader`). Header/footer wordmark uses `SITE_NAME` from `lib/site.ts`. Added `CONTACT_EMAIL` / `CONTACT_PHONE` (optional) with defaults in `lib/site.ts` and `.env.example`. Body copy, collaborator grid, and hero subline are generic placeholders. Screenshot reference output file renamed to `reference-external-home-full.png`. Privacy footer link points to `/pages/privacy-policy` to match cookie banner.

## 2026-04-15 22:00
- **Context:** User wanted a light, Flipper-like technical hardware site (black device on light canvas), monospace/ASCII accents, plus a reusable AI context prompt.
- **Decision:** Root layout and `globals.css` default to light (`#fafafa`). Marketing home uses **Plus Jakarta Sans** + **JetBrains Mono**; hero ASCII block, dark device placeholder, spec terminal band (`#specs`), spec grid, ethics block. `lib/site.ts` adds `PRODUCT_TAGLINE` and `PRODUCT_HERO_HEADLINE` (env). Cookie consent panel restyled for light. `docs/PRODUCT_AI_CONTEXT_PROMPT.md` is the fill-in prompt for AI sessions. Layout metadata keywords updated toward hardware/research.

## 2026-04-15 23:30
- **Context:** Extend the light zinc/stone hardware UI (Roboto + Roboto Mono baseline) across shop routes, CMS pages, checkout review, errors, footer, and split-section.
- **Decision:** Replaced remaining dark-era Tailwind classes with zinc borders/text (`app/products`, `collections`, PDP/collection detail breadcrumbs, `checkout/review`, `error.tsx`, `not-found.tsx`, `global-error.tsx`). `globals.css` `.shopify-page-body.prose` colors updated for light prose (no `prose-invert` on CMS). `split-section` right column: `bg-zinc-50`, light form controls; left hero stays cinematic on photos. `IntroOverlay` shell uses `bg-zinc-100` if re-enabled. Footer cross uses black asset without `invert` on light.
- **Next step:** Visual QA on catalog, PDP, cart, checkout, legal pages, and 404/500.

## 2026-04-15 24:00
- **Context:** User supplied a filled SubZero product brief (project-apex + subzero-website); hero/specs/ethics + `/docs` skeleton.
- **Decision:** `lib/site.ts` defaults: `SITE_NAME` SubZero, tagline/headline per brief. `home-landing.tsx` rewritten with repo-backed spec band + grid, elevator pitch, RF/spectrum ethics (EU EIRP example, no CE/FCC claims), hero `data-product-hero` + note for future GLB. `app/docs/page.tsx` skeleton (overview, bring-up, firmware, safety). Header `Docs` → `/docs`. `.env.example` and `PRODUCT_AI_CONTEXT_PROMPT.md` blurb updated.
- **Next step:** Wire interactive 3D when GLB exists; replace TBD footer/domain when known.

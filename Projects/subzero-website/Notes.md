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

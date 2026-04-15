## 2026-04-15 12:00
- **Context:** User wanted to drop Tailwind and use another styling approach.
- **Decision:** Replaced `tailwindcss` + `@tailwindcss/typography` with **UnoCSS** (`unocss`, `@unocss/postcss`), `presetWind3` for Tailwind v3–compatible utilities, `presetTypography` for `prose`. PostCSS uses `@unocss/postcss`; `styles/globals.css` starts with `@unocss` instead of `@tailwind`. Removed `tailwind.config.ts`, added `uno.config.ts` (theme colors from former Tailwind extend). CMS page (`app/pages/[handle]/page.tsx`) no longer uses Tailwind Typography element modifiers (`prose-headings:*`, etc.); those rules live under `.shopify-page-body.prose` in `globals.css`.
- **Next step:** Run `npm install` in the repo to refresh `package-lock.json` (sandbox had no `npm`); then `npm run build` to verify.

## 2026-04-15 14:00
- **Context:** User wanted an empty storefront shell: remove dither background, hamburger menu, marquee banner, and see a blank site.
- **Decision:** Removed `DitherBackground` from `app/layout.tsx` and deleted `components/atoms/dither/*`. Removed `SmartHeader` (and `HamburgerMenu`) from `providers.tsx`; deleted `smart-header.tsx`, `hamburger-menu.tsx`, `marquee-banner.tsx`. Dropped `hooks/use-device-performance.ts` and `detect-gpu` dependency (only used by dither). Home `app/page.tsx` now returns `null`; removed `Footer` from root layout; deleted `home-cinematic-section.tsx` and `collection-showcase.tsx` (only used by home). Body background is solid black in `globals.css`. Cart drawer remains mounted but no header trigger until a new one is added.
- **Next step:** `npm install` (lockfile may need refresh after removing `detect-gpu`); `npm run dev` locally.

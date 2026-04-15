## 2026-04-15 12:00
- Insight: New project directory `ESP Projects/neutral-shopify-shell` implements the neutral shell plan: commerce logic under `core/shopify`, UI under `features/` and `shared/`, env-driven site URL/name, featured collection handle, free-shipping threshold, and featured GraphQL search queries.
- Context: `subzero-website` repo was left unchanged; new codebase is a sibling folder for a fresh git remote.
- Decision: No brand strings in runtime paths; SEO/JSON-LD use `getSiteUrl()` / `getSiteName()` from `core/config/storefront.ts`.
- Next step: Run `npm install`, `npm run build`, `npm run test:run`, and `npm run lint` locally (sandbox had no `npm`).

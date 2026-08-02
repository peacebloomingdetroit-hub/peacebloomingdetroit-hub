# Changelog — Peace Blooming Visual Redesign

## Overview
Applied a complete visual and layout redesign to the existing 38-page static site through the existing Python generator (`build_site.py`). No pages, routes, schema, or Netlify config were changed. All placeholders (`[PHONE]`, `[EMAIL]`, `[COVERAGE AMOUNT]`, `[RESPONSE TIME]`, `[PHOTOS]`) remain intact.

---

## Phase 1 — Color & Typography

### What changed
- Replaced the generic sage/gray palette with the design-spec palette:
  - `--green-dark: #2c3e32` — headings, primary buttons, nav hover, footer
  - `--cream: #f6f4ed` — page/section backgrounds
  - `--gold: #c9a86c` — secondary buttons, hover, seasonal highlights
  - `--sage-soft: #dce8e0` — trust band, FAQ blocks, quote blocks
  - `--text: #3d3d3d` — body text
  - `--muted: #6b6b6b` — captions
  - `--white: #ffffff` — cards, nav, contrast
  - `--border: #e8e4d9` — borders/dividers
- Swapped typography to Google Fonts: `Fraunces` (warm serif headings) + `Inter` (clean sans body).
- Added `preconnect` to Google Fonts for performance.
- Updated type scale: H1 36/48px, H2 28/36px, H3 20/24px, body 16px/1.7.
- Removed all-caps headings; now sentence case everywhere.

### Why
The new palette matches the emerging category standard for modern grave-care sites (Tending, Gravesite Cleanup) while feeling warmer and more personal. Fraunces adds human warmth without the coldness of a traditional funeral-home serif.

---

## Phase 2 — Layout, Header, Navigation, & Conversion

### What changed
- **Sticky top nav** with a visible "Call [PHONE]" button on desktop and tablet.
- **Mobile hamburger menu** with accessible toggle (`aria-expanded`, `aria-controls`, `aria-label`).
- **Sticky bottom CTA bar** on mobile with Call + Request Service buttons; hides when footer scrolls into view.
- **Homepage rhythm rebuilt**:
  - Hero with tagline, value prop, and phone-first CTAs.
  - Trust band on `--sage-soft`.
  - Story block with owner photo beside personal story.
  - Service cards with simple line icons.
  - How It Works steps.
  - Service area preview.
  - New **Clear, Upfront Pricing** preview section with three cards.
  - FAQ preview.
  - Closing holiday CTA.
- Added small `js/site.js` file for mobile nav toggle and sticky CTA visibility logic.
- CTA copy standardized: "Call [PHONE]", "Request Service Online", "See Pricing", "See Services & Pricing", "See Full Pricing", "Request Service". Removed vague "Submit Request" / "Learn More" / "Schedule a Visit".
- Page heroes now use solid `--green-dark` background for strong visual hierarchy.

### Why
Mobile-first local-service visitors need the phone number within one tap. The sticky bottom CTA and header Call button remove friction. The homepage now follows a proven conversion funnel: problem → trust → story → services → process → pricing → FAQ → CTA.

---

## Phase 3 — Transitions, Lazy Loading, & Accessibility

### What changed
- Added `loading="lazy"` to below-the-fold images (story photo, about page owner photo). Hero image stays `loading="eager"`.
- Added hover transitions to cards, buttons, and interactive elements.
- Added visible `:focus-visible` and `:focus` states for buttons, links, and form inputs using gold outline.
- Added a **skip-to-content link** for keyboard navigation.
- Ensured all buttons and tap targets meet a minimum of 44px height (most are 48px+).
- Preserved all existing JSON-LD schema, meta tags, page URLs, and the Netlify form (`data-netlify="true"` + honeypot field).
- Added `aria-label` to navigation and sticky CTA for screen readers.

### Why
Accessibility and performance are ranking/UX factors for local search. Smooth transitions make the site feel intentional, and visible focus states keep it usable for keyboard users.

---

## Files Changed

- `build_site.py` — updated templates, CSS string, homepage content, added JS generation.
- `site/css/style.css` — regenerated with new design system.
- `site/js/site.js` — new minimal vanilla JS file.
- All 38 HTML files — regenerated consistently from the updated templates.

## Files NOT Changed

- `website-copy.md` — content source unchanged; placeholders intact.
- `seo-aio-strategy.md` — strategy unchanged.
- `visual-design-plan.md` — design spec unchanged.
- `robots.txt`, `sitemap.xml`, `netlify.toml` — regenerated with identical content/structure.

## Verification

- `python3 build_site.py` completed successfully with 38 pages.
- Local preview on `http://localhost:8765` returned `200` for homepage, CSS, JS, contact page, and cemetery page.
- All 38 HTML files contain the new sticky CTA and navigation template.
- Contact form retains `data-netlify="true"` and honeypot field.
- All JSON-LD schema blocks remain present.

## Next Steps for Launch

1. Replace `[PHONE]`, `[EMAIL]`, `[COVERAGE AMOUNT]`, and `[RESPONSE TIME]` with real values.
2. Replace placeholder images with real photos per `photo-shot-list.md`.
3. Create or source a real bloom-mark logo to replace the placeholder text logo.
4. Purchase and connect `peaceblooming.com` in Netlify.
5. Set up Google Business Profile.

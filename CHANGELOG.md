# Changelog — Peace Blooming Visual Redesign

## Overview
Applied a complete visual and layout redesign to the existing 38-page static site through the existing Python generator (`build_site.py`). Added social tags, legal/utility pages, analytics hooks, conversion improvements, breadcrumbs, image optimization, and a pre-launch verification script. All placeholders (`[PHONE]`, `[EMAIL]`, `[COVERAGE AMOUNT]`, `[RESPONSE TIME]`, `[PHOTOS]`) remain intact until real business details are confirmed.

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

## Phase 4 — Open Graph & Twitter Card Social Tags

### What changed
- Added complete Open Graph meta tags to every page: `og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:site_name`, `og:locale`.
- Added Twitter Card meta tags to every page: `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`.
- Added `<link rel="canonical">` to every page for SEO.
- Updated `wrap_in_template()` to accept `canonical_url`, `og_image`, and `og_type` parameters.
- All page generator functions now pass their canonical URL.
- Default `og:image` falls back to `/images/social/default.jpg` (1200x630 placeholder on dark green background).
- Social placeholder image is generated automatically during build alongside other placeholder images.

### Why
Without social tags, shared links on Facebook, LinkedIn, X/Twitter, and messaging apps show no preview image, title, or description. Adding OG and Twitter Card tags ensures rich previews with the page title, description, and a branded image whenever anyone shares a Peace Blooming URL.

---

## Phase 5 — Quick Wins: 404, Privacy, Analytics, Newsletter, Validation, Hreflang

### What changed
- **Custom 404 page** (`/404.html`) with friendly messaging and links back to Home, Contact, and Service Area. Wired to Netlify via `[[redirects]] from="/*" to="/404.html" status=404`.
- **Privacy Policy page** (`/privacy-policy.html`) covering data collection, usage, protection, cookies, and contact information. Added to footer links and sitemap.
- **Analytics hooks** in `BASE_TEMPLATE`: `GA_MEASUREMENT_ID` and `GOOGLE_SEARCH_CONSOLE_TAG` placeholders near the top of `build_site.py`. Filling either injects the GA4 gtag or Search Console verification meta tag automatically on every page.
- **Hreflang tags** added to every page: `hreflang="en-us"` for the current canonical URL plus `hreflang="x-default"` pointing to the homepage.
- **Newsletter / seasonal reminder signup** in the footer, implemented as a Netlify form with honeypot, email validation, and a Privacy Policy link.
- **Contact form validation improvements**: HTML5 `pattern` and title on the phone/email field, visual invalid state via CSS, and a JS helper that checks for at least a phone number or valid email format before submission.
- Site page count updated to 40 pages (11 core + 9 cemetery + 20 city).

### Why
These are small, launch-ready details that improve SEO, compliance, trust, and conversion without blocking on photos or business setup. A custom 404 and privacy policy are expected by search engines and visitors; analytics and hreflang make the site easier to index; the newsletter captures interested visitors before they leave; and better form validation reduces failed submissions.

---

## Phase 6 — Pre-Launch Verification & Runbook

### What changed
- Added `pre_launch_check.py` script that verifies:
  - No remaining placeholders in generated HTML.
  - Required images exist (`logo.png`, `favicon.png`, `apple-touch-icon.png`, `social/default.jpg`).
  - Open Graph and Twitter Card tags are present on every public page.
  - Canonical URL and hreflang tags are present on every public page.
  - JSON-LD schema blocks are valid JSON.
  - Internal links are not broken.
  - Analytics configuration is filled in (reported as a warning, not a hard failure, until IDs are available).
- Added `LAUNCH.md` runbook with a complete launch checklist covering copy, business setup, domain/hosting, Google setup, Google Business Profile, final testing, and post-launch monitoring.
- Added `noindex, nofollow` to the hidden `form-blueprint.html` utility page.
- Added homepage `BreadcrumbList` schema alongside the existing LocalBusiness and FAQPage schemas.
- Removed a long-standing SyntaxWarning in the generated site README.
- Added a dedicated `newsletter-success.html` page and wired the footer newsletter form to `action="/newsletter-success.html"`.
- Added step-by-step Netlify form notification setup instructions to `LAUNCH.md` so contact and newsletter submissions actually reach the business inbox.

### Why
A pre-launch verification script turns launch day from a manual checklist into a repeatable, fast test. It catches forgotten placeholders, missing images, broken links, and invalid schema before visitors or search engines see them. The runbook makes it easy to hand off the remaining business-only steps to the owner.
---

## Phase 7 — Breadcrumbs, Alt-Text Audit, and Image Optimization

### What changed
- Added a reusable `create_breadcrumb_schema()` helper and added `BreadcrumbList` JSON-LD to every public page:
  - Services & Pricing, How It Works, Service Area, About, FAQ, Contact, Contact Success, Blog, Gallery, 404, Privacy Policy.
  - Cemetery and city pages already had breadcrumbs; now they use the shared helper.
- Audited image `alt` text across the site and fixed the header logo, which had an empty `alt` attribute. It now reads `alt="Peace Blooming logo"`.
- Added image optimization:
  - `generate_webp_version()` creates a `.webp` sibling for every JPG/PNG image (placeholder or real) during the build.
  - Wrapped all content `<img>` tags in `<picture>` elements with a WebP `<source>` and the original image as fallback.
  - Added CSS so `<picture>` elements behave like images (block display, max-width, height auto).
- Updated `pre_launch_check.py` with two new checks:
  - Every public page `<img>` tag has a non-empty `alt` attribute.
  - Every JPG/PNG in `site/images/` has a corresponding `.webp` variant.
- Added a fallback `apple-touch-icon.png` generator in the logo fallback path so the icon is always created.

### Why
Breadcrumb schema helps Google display richer navigation paths in search results. Descriptive alt text improves accessibility and image SEO. WebP images are typically 25–35% smaller than JPG/PNG, which improves page load speed — especially important for mobile visitors on cemetery grounds with weaker signal.

---


---

## Files Changed

- `build_site.py` — templates, CSS, JS, schema generation, new pages, analytics hooks, form improvements, breadcrumbs, image optimization, sitemap/netlify updates.
- `pre_launch_check.py` — new pre-launch verification script.
- `LAUNCH.md` — new launch runbook checklist.
- `CHANGELOG.md` — this file.
- `site/css/style.css` — regenerated with design system and newsletter styles.
- `site/js/site.js` — regenerated with mobile nav, sticky CTA, form validation helpers.
- All public HTML files — regenerated with social tags, canonical/hreflang, breadcrumbs, footer newsletter, and privacy link.
- `site/404.html`, `site/privacy-policy.html`, and `site/newsletter-success.html` — new pages.
- `site/images/social/default.jpg` — new social sharing placeholder.
- `site/images/**/*.webp` — WebP variants generated for every JPG/PNG.
- `site/netlify.toml` — updated with 404 redirect.
- `site/sitemap.xml` — updated to include privacy policy.

## Files NOT Changed

- `website-copy.md` — content source unchanged; placeholders intact.
- `seo-aio-strategy.md` — strategy unchanged.
- `visual-design-plan.md` — design spec unchanged.
- `photo-shot-list.md` — shot list unchanged.

## Verification

- `python3 build_site.py` completed successfully with 41 pages.
- `python3 pre_launch_check.py` runs successfully and reports only the expected `[PHONE]` placeholders and empty analytics IDs as warnings.
- All public HTML files contain social tags, canonical URLs, hreflang tags, and breadcrumb schema.
- Contact form and newsletter form retain `data-netlify="true"` and honeypot fields.
- All JSON-LD schema blocks are valid JSON.
- All content images have non-empty alt text and WebP variants with `<picture>` fallback.

## Next Steps for Launch

1. Replace `[PHONE]`, `[EMAIL]`, `[COVERAGE AMOUNT]`, and `[RESPONSE TIME]` with real values in `website-copy.md` and `build_site.py`, then rebuild.
2. Replace placeholder images with real photos per `photo-shot-list.md`.
3. Fill `GA_MEASUREMENT_ID` and `GOOGLE_SEARCH_CONSOLE_TAG` in `build_site.py` and rebuild.
4. Purchase and connect `peaceblooming.com` in Netlify.
5. File Michigan LLC and set up Google Business Profile.
6. Run `python3 pre_launch_check.py` until all hard checks pass.
# Visual Design Plan — Peace Blooming
*Prepared for review before implementation.Companion to `website-copy.md`, `seo-aio-strategy.md`, and `competitor-site-teardown.md`.*

---

## 1. Goal

Design a website that looks like a trustworthy, personal, local service business — not a funeral home, not a tech startup, and not a generic template. The visual identity should make a first-time, often anxious visitor feel:

- **This is a real, local business** (not a platform or franchise)
- **I can trust them with something personal**
- **I know exactly what to do next**
- **The owner understands my situation**

---

## 2. Competitor Visual Audit (What We Learned)

### Tending (tending.app) — The most "designed" competitor
- **Palette:** Warm cream background (`#f3efde`), dark forest green (`#1c2e1c`), soft blue accent (`#e3f1f8`). Earthy, premium, calm.
- **Typography:** Lora serif + Mulish sans (or Poppins + Libre Baskerville on a subscription landing page). Serif headings = trust; sans body = readability.
- **Strengths:** Clean, modern, high-contrast, looks funded/legitimate. Insurance and trust signals prominent.
- **Weaknesses for us:** Can feel slightly corporate/tech. The custom-quote model is less approachable for a small local operator.
- **What to borrow:** Cream + dark green palette structure; serif headings; strong trust band; real before/after photos.
- **What to avoid:** Any hint of a generic SaaS platform; we should look more personal/handcrafted.

### Gravesite Cleanup (gravesitecleanup.com) — Best conversion layout
- **Palette:** Same cream/green family as Tending (likely built with similar tooling).
- **Typography:** DM Sans + Fraunces (elegant serif). Modern but warm.
- **Strengths:** Tight homepage funnel — hero → testimonial → services → process → pricing → CTA. Transparent pricing. Prominent phone CTA.
- **Weaknesses:** Looks like a generic AI-generated landing page (Lovable-style). The brand personality is thin.
- **What to borrow:** The exact page flow; the strong, direct CTAs; the "you don't need to be present" reassurance high on the page.
- **What to avoid:** Generic AI-site aesthetic. We need authentic photography and a warmer, more personal story.

### Keeper of the Stones (keeperofthestones.com) — Template-driven
- **Palette:** Weebly template defaults; neutral blues/grays.
- **Typography:** Raleway + Lora + Montserrat (mixed template fonts).
- **Strengths:** Clear, simple, content-first. No distracting design.
- **Weaknesses:** Looks dated and template-y. Low visual trust.
- **What to avoid:** We should not look like a free Weebly template.

### Grave Care Services (gravecareservices.com) — Old, personal
- **Palette:** None detectable — very plain, dated layout.
- **Typography:** Default serif/system fonts.
- **Strengths:** Heavy personal story and one-on-one relationship emphasis.
- **Weaknesses:** Looks old/unprofessional. No transparent pricing. Poor mobile experience likely.
- **What to borrow:** The personal narrative angle (your mom's story is even stronger).
- **What to avoid:** Dated, low-trust design.

### Grave Conservation LLC (graveconservation.com) — E-commerce + service hybrid
- **Palette:** WordPress default theme colors; neutral with some orange accents.
- **Typography:** Asap (rounded sans).
- **Strengths:** Actual photos of stones; clear service area list; seasonal policy.
- **Weaknesses:** Confusing retail shop focus; the service page is buried under products.
- **What to borrow:** Use real photos of the work and the named service area; publish the seasonal operating policy honestly.
- **What to avoid:** Don't make the site look like an e-commerce store.

### Cross-cutting design truths
1. **Cream + dark green is the emerging category standard** for modern grave care sites (Tending, Gravesite Cleanup). It signals earth, growth, care, and calm.
2. **Serif headings + sans-serif body** is the trust/readability pairing every serious competitor uses.
3. **No one has a big public gallery.** Before/after photos are framed as a delivered service, not a portfolio.
4. **Mobile-first is mandatory** — this is a local, often emergency-adjacent search. Click-to-call must be frictionless.
5. **Generic template look = low trust.** A clean custom design with real photos beats a flashy AI template.

---

## 3. Recommended Design Direction for Peace Blooming

### Overall mood
**Warm, calm, handcrafted, local.** Think of a well-tended garden, a clean stone after rain, and a handwritten note — not a funeral home, not a startup dashboard.

### Name + tagline lockup
The logo should always appear with the tagline or in a context where the tagline is visible, because "Peace Blooming" is not literally descriptive:

> **Peace Blooming**  
> Grave Cleaning & Seasonal Flowers, Wyandotte & Metro Detroit

On the website, the logo wordmark can be the primary brand element, with the tagline visible in the hero or under the logo in the nav on desktop.

---

## 4. Color Palette

| Role | Hex | Name | Usage |
|---|---|---|---|
| **Primary dark** | `#2c3e32` | Deep forest green | Headings, primary CTA buttons, nav hover, footer background, key text |
| **Primary light** | `#f6f4ed` | Warm cream | Page background, card backgrounds, section alternation |
| **Accent** | `#c9a86c` | Warm gold / aged brass | Secondary CTAs, hover states, small icons, seasonal highlights |
| **Secondary soft** | `#dce8e0` | Sage mist | Accent section backgrounds, trust band, FAQ blocks, quote blocks |
| **Text** | `#3d3d3d` | Charcoal | Body text (not pure black — softer) |
| **Muted text** | `#6b6b6b` | Warm gray | Captions, meta text, footer secondary text |
| **White** | `#ffffff` | White | Cards, nav bar, content areas, contrast sections |
| **Cream dark** | `#e8e4d9` | Border/divider | Subtle borders, section dividers, table borders |

**Why this palette:**
- Green = growth, care, balance, nature. It fits a service that literally works with grass and stone.
- Cream = warmth, paper, calm, approachable. Avoids the cold clinical feel of a pure white funeral site.
- Gold = dignity, a small touch of "honoring memory" without being flashy or religious.
- Avoids: bright funeral-home blues, somber blacks, clinical hospital whites, or trendy purples that don't fit the name.

**Accessibility note:** The primary dark green on cream passes WCAG AA for normal text. The gold accent should only be used for large text or decorative elements, not small body text.

---

## 5. Typography

**Font pairing:**
- **Headings:** `Fraunces` (Google Fonts) — a soft, warm serif with a little personality. More human than stark Lora or traditional Times.
- **Body:** `Inter` or `DM Sans` — clean, highly readable, modern sans-serif. Inter is free, fast-loading, and excellent on mobile.
- **Accent/Logo tagline:** `Fraunces` italic or `DM Sans` medium — for the tagline under the logo.

**Type scale (mobile-first):**
- H1: 2.25rem (36px) on mobile, 3rem (48px) on desktop
- H2: 1.75rem (28px) mobile, 2.25rem (36px) desktop
- H3: 1.25rem (20px) mobile, 1.5rem (24px) desktop
- Body: 1rem (16px), line-height 1.7
- Small/caption: 0.875rem (14px)

**Why this typography:**
- Serif headings = trust, tradition, care.
- Sans body = modern readability, especially for older visitors and mobile screens.
- Fraunces has slight rounded softness that matches "Peace Blooming" better than sharp serif fonts.
- No more than two font families. No script fonts (too fussy for a service business).

---

## 6. Imagery & Photography Style

### What photos should look like
- **Real, not stock.** No posed stock models at a grave. The most important image is the owner photo.
- **Soft, natural light.** Overcast Michigan days, morning light, or shaded cemetery scenes. Avoid harsh midday sun or flash.
- **Close but respectful.** Focus on the stone, the flowers, and the hands doing the work — not wide sad cemetery vistas.
- **Before/after pairs:** Same angle, same distance, same lighting. Show the transformation honestly.
- **Seasonal variety:** Easter lilies, Memorial Day flags/mums, fall chrysanthemums, Christmas wreaths.
- **Privacy:** No other families' names or dates visible. Blur or crop. Your mom's own family grave is the perfect first subject.

### Key images to capture (minimum launch set)
1. **Hero:** A well-tended grave with fresh flowers in soft daylight — warm, peaceful, not sad.
2. **Before/after cleaning:** One dirty stone, same stone cleaned.
3. **Before/after decorating:** A bare grave, then with seasonal flowers.
4. **Cleaning in progress:** Soft brush on a stone (shows gentle method).
5. **Finished decorated grave:** A completed seasonal arrangement.
6. **Owners:** Real, warm photo of your mom and her friend — outdoors or at a cemetery, approachable.
7. **Mt Carmel grounds:** Respectful entrance or grounds shot for the Mt Carmel page.
8. **Logo/favicon:** Simple bloom mark + wordmark.

### Image treatment
- Slight warmth in editing (not desaturated/gray).
- Consistent aspect ratios: hero 16:9, before/after pairs 4:3 or 1:1, owner photo 3:4 or 4:5.
- Compress to WebP for performance; keep JPG fallbacks.
- Lazy-load below-the-fold images.

---

## 7. Layout & UX Principles

### Mobile-first, thumb-first
- Sticky nav with a prominent **Call** button on mobile.
- Primary CTAs minimum 48px tall (ideally 56px for thumb tapping).
- Click-to-call everywhere. A phone call is the highest-intent action for this demographic.
- Short paragraphs, lots of white space, clear section breaks.

### Homepage structure (unchanged in content, refined in visual execution)
1. **Hero:** Full-width warm background or photo with the personal value prop and a phone-first CTA.
2. **Trust band:** Insured • Photos after every visit • Cemetery rules checked — visually distinct (sage mist background).
3. **Story block:** Owner photo + short personal story. This is the emotional anchor.
4. **Services preview:** 3 cards (Cleaning, Decorating, Photo Proof) with icons, brief text, and a link to pricing.
5. **How it works:** 4 numbered steps, clear and simple.
6. **Service area preview:** Named cities with a map to the full service area page.
7. **Pricing preview:** A few key prices + link to full pricing page.
8. **FAQ block:** 3 questions on the homepage, link to full FAQ.
9. **Closing CTA:** Holiday-booking reminder + phone + form.

### Service-area / cemetery pages
- Each page should feel like a landing page, not a thin stub.
- Use a small, relevant photo if available (e.g., Mt Carmel grounds for the Mt Carmel page).
- Repeat the trust band near the top of every service-area page.
- Always end with a clear CTA: Call + Request Service Online.

### Pricing page
- Use a clean table layout on desktop, stacked cards on mobile.
- Highlight the Seasonal Care Plan as "most popular."
- Add a short trust note: "No surprise bills. We confirm exact price before scheduling."

### Contact page
- Form first, contact info second on mobile.
- Large tap targets, clear labels.
- Keep the "How did you hear about us?" field — it's critical for attribution.

---

## 8. CTA Strategy

**Primary action:** Call the phone number.  
**Secondary action:** Request service online via the Netlify form.

- **Primary CTA style:** Solid deep green background, white text, rounded corners (8px). Use for "Call [PHONE]."
- **Secondary CTA style:** White or cream background, green border, green text. Use for "Request Service Online" and "See Pricing."
- **Accent CTA (seasonal urgency):** Gold background, dark green text for limited holiday-slot messaging.
- **Sticky mobile CTA:** On long pages (services, pricing, contact), a fixed bottom bar with "Call" + "Request Service" buttons.

**CTA copy:**
- "Call [PHONE]"
- "Request Service Online"
- "See Services & Pricing"
- "Get a Free Quote"
- "Reserve Holiday Visit"

Avoid: "Submit," "Learn More," "Contact Us" (too vague).

---

## 9. Logo Direction

### Concept
A simple, hand-drawn or line-art bloom mark paired with a clean wordmark. The bloom should feel:
- **Not a religious symbol** (crosses are too specific)
- **Not overly funereal** (no urns, stones, or wilted imagery)
- **Not childish or cartoonish** (no thick outlines or emoji-like flowers)

### Recommended approach
- **Mark:** A single stylized flower or bud with a few leaves — minimal line art, one color.
- **Wordmark:** "Peace Blooming" in `Fraunces` medium or semi-bold, with the tagline in `DM Sans` or `Inter` below or beside it.
- **Color versions:** Green mark on light backgrounds; white/light mark on dark green backgrounds.
- **Favicon:** Just the bloom mark.

### Implementation options
1. **DIY:** Use a simple SVG icon from a reputable source (e.g., Phosphor Icons or Heroicons floral line icons) and pair with the wordmark in Fraunces.
2. **Low-cost designer:** Hire a Fiverr/99designs designer for ~$100–$200 to create a simple custom bloom mark.
3. **AI generation:** Generate a clean line-art bloom mark using an AI image tool, then convert to SVG with `recraft_svg` or trace it.

For launch, option 1 is perfectly fine. The logo can be upgraded later once revenue justifies it.

---

## 10. What to Change from the Current Site

The current site is structurally correct but visually generic. Here's the priority order of changes:

| Priority | Change | Effort | Impact |
|---|---|---|---|
| 1 | Apply the new color palette to CSS | Low | High |
| 2 | Switch to Fraunces + Inter fonts (Google Fonts) | Low | High |
| 3 | Redesign the header/nav with a sticky mobile CTA | Medium | High |
| 4 | Replace placeholder images with real photos | Medium | Highest |
| 5 | Add a real logo (mark + wordmark) | Medium | High |
| 6 | Add trust band and refine section spacing | Low | Medium |
| 7 | Add before/after image components and seasonal accent blocks | Medium | Medium |
| 8 | Add subtle animations (fade-in on scroll) | Low | Low/Medium |
| 9 | Create printable/service-vehicle brand kit | Medium | Future |

---

## 11. What to Avoid

- **No dark/black dominant theme.** This is a care service, not a funeral announcement.
- **No clinical pure white everywhere.** Cream/warm backgrounds feel more human.
- **No stock photos of strangers grieving.** Authenticity matters more than polish.
- **No trendy gradients, glassmorphism, or neon accents.** Keep it timeless.
- **No all-caps headings.** Use sentence case or title case for warmth.
- **No more than 2 fonts.** Keep it simple.
- **No burying the phone number.** It should be visible within one tap at all times on mobile.

---

## 12. Implementation Plan (Once Approved)

1. **Phase 1 — Color & type update:** Apply the new palette and fonts to `css/style.css` and re-run `build_site.py` to refresh all 38 pages.
2. **Phase 2 — Layout refinements:** Update the header, add sticky mobile CTA, improve trust band and service cards.
3. **Phase 3 — Media & logo:** Replace placeholder images with real photos; design or source the bloom mark logo and update the generated logo files.
4. **Phase 4 — Polish:** Add subtle hover transitions, lazy loading, and final accessibility checks.

Each phase can be done independently. The first two phases alone will make the site feel much more intentional without needing real photos yet.

---

## 13. Confidence Notes

- **High confidence:** Color palette direction (validated by Tending/Gravesite Cleanup + general color psychology), typography pairing, mobile-first CTA strategy, real-photo approach.
- **Medium confidence:** Exact hex values — these are recommendations and can be tuned after seeing the logo and photos.
- **Low confidence:** Logo design specifics — depends on whether we source a custom mark or use a clean icon. This is a launch-then-refine item.

---

*Next step: Review and approve this plan, then I'll implement Phase 1 and Phase 2 (CSS + layout) and prepare a list of the exact photos we need for Phase 3.*

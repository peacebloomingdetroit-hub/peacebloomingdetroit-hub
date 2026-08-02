# Peace Blooming — Logo Mark Generation Prompt (GPT-4o)

Use this prompt with **GPT-4o image generation** (DALL·E) to generate the **icon/mark only**. Add the wordmark "Peace Blooming" in Fraunces later in Figma / Illustrator — do not ask the model to render text.

---

## Primary Prompt (copy-paste)

> **A single, elegant stylized flower bud icon for a premium memorial-care brand. Continuous one-line / monoline vector style, flat 2D, single color #2c3e32 deep forest green, centered on a pure white background. The mark forms a closed, abstract bloom: a rounded bud shape with a few delicate leaf/petal curves wrapping around it, subtle suggestion of new growth and peace. Clean, minimalist, high-end gardening-service aesthetic. No gradients, no shadows, no 3D, no fills, no photorealism, no texture, no extra colors, no text, no lettering, no frames, no background shapes. Icon should read clearly at 16px as a favicon. Vector silhouette style, uniform stroke weight, balanced negative space.**

---

## Technical specs to include if the platform allows

- **Format:** square PNG, 1024 × 1024 px (transparent background optional, but white background is safer for the first test)
- **Color:** single dark green `#2c3e32` on white `#ffffff`
- **Style:** flat vector / line art / monoline
- **Content:** icon-only, no words
- **Use case:** favicon, social avatar, website header mark, app icon

---

## Negative prompt add-ons (paste after the main prompt if desired)

> No gradients, no drop shadows, no glow, no 3D effects, no metallic textures, no realism, no photographs, no shading, no filled shapes, no watercolor, no sketchy pencil lines, no cartoons, no crosses, no religious symbols, no ribbons, no hearts, no human figures, no monuments, no text, no letters, no numbers, no frames, no borders, no corner badges, no halftone, no background texture.

---

## Why this works

- **Icon-only** avoids text rendering issues (GPT image generators struggle with clean wordmarks).
- **Monoline** stays crisp at small sizes (favicon, mobile header).
- **Single color** makes vectorization easy via Illustrator trace or Recraft vectorizer.
- **Closed-loop bud** suggests blooming life and care without being literal or cartoonish.
- **Negative prompts** protect against the default "gradient-shiny-stock-logo" look.

---

## Suggested next steps after generation

1. Generate 4–6 variants with the prompt above.
2. Pick the strongest mark, crop it tightly, and convert to vector (SVG):
   - **Adobe Illustrator:** Image Trace → `Silhouettes` preset, adjust threshold, expand.
   - **Recraft:** use the `recraft_vectorize` tool to convert the chosen PNG to SVG.
   - **Figma plugin:** Vectorize It / Tracer.
3. In Figma/Illustrator, add the wordmark:
   - **Text:** `Peace Blooming`
   - **Font:** Fraunces (soft / medium weight, or Fraunces Italic for the tagline)
   - **Color:** `#2c3e32` for dark/light cream; white `#ffffff` for dark green backgrounds.
4. Export the required set:
   - `logo.svg` (vector)
   - `logo-compact.svg` (~300×80 artboard)
   - `logo-mark.svg` (~100×100 artboard)
   - `logo.png` (800×200 px)
   - `favicon.png` (512×512 px)
   - `apple-touch-icon.png` (180×180 px)
5. Test the favicon at 16×16 and the header mark at 32×32. If details collapse, simplify the bud/leaf curves further.

---

## Alternative directions (short-form prompts)

If the first result feels too generic, try one of these variations:

**A — Leafy bud:**
> Minimalist botanical line icon: a flower bud with two small leaves, continuous outline, deep forest green #2c3e32, flat vector, white background, no text, no shading, centered, readable at 16px.

**B — Blooming seed:**
> Abstract single-line icon of a seed sprouting into a gentle bloom, closed loop, premium garden-service brand, forest green #2c3e32, flat 2D, white background, no gradients, no photorealism, no text.

**C — Wildflower silhouette:**
> Simple wildflower silhouette icon, single stem with a small bud and two leaves, dark green #2c3e32, flat vector, centered, white background, no fill, no shading, no text, favicon-ready.

---

*Generated for the Peace Blooming website project, `3-Website/`.*

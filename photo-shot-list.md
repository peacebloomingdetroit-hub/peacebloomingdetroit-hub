# Photo Shot List & Naming Convention — Peace Blooming
*Companion to `website-copy.md`, `seo-aio-strategy.md`, and `competitor-site-teardown.md`. Tells you exactly which photos to take, what to name each file, and where to save it so it plugs straight into the site.*

## Where photos live

All site images go in `3-Website/images/`, split into one subfolder per page area:

```
3-Website/images/
├── home/          hero + before/after pairs for the homepage
├── services/      cleaning-in-progress + finished decoration shots
├── about/         photo of the two owners
├── service-area/  cemetery grounds shots (one per cemetery)
├── logo/          logo files + favicon
└── gbp/           extra photos for the Google Business Profile (not the website)
```

When the site is built, these map to a matching `/images/...` path on the live site (e.g., `images/home/hero.jpg` → `https://warcraft.wiki.gg/images/Genn%2C_Cursed_King_HS.png?72b47f`).

## Naming rules (so files plug straight in)

1. **All lowercase, words separated by hyphens** — `before-after-cleaning-01.jpg`, never `Before After (1).JPG`. Spaces, capitals, and parentheses break web links.
2. **Describe the content, then a 2-digit number** for sets — `-01`, `-02`, so they sort correctly and you can add more later.
3. **Before/after pairs share a base name** with a `-before` / `-after` suffix — keeps each pair obviously linked.
4. **Keep extensions lowercase** — `.jpg` for photos, `.png` for the logo/anything needing transparency, `.svg` if you get a vector logo.
5. **Web-optimized:** shoot landscape (horizontal), export around 1600–2000px on the long edge, JPG quality ~80%, aim for under ~400 KB each so pages load fast (page speed affects local ranking — see `seo-aio-strategy.md` §9.5).
6. **No other family's names/dates visible** in any public photo — blur or crop them out (matches the consent clause in `service-agreement-template.md`). Your own family's grave is fine to show fully.

---

## The shot list

Legend: **[MUST]** = needed to launch · **[NICE]** = add when you can.

### `images/home/`
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** Hero image | `hero.jpg` | Peaceful, well-tended grave with fresh flowers, or a soft daylight grounds shot. Calm and warm, not somber. This sets the whole site's tone. |
| **[MUST]** Before/after cleaning | `before-after-cleaning-01-before.jpg` / `before-after-cleaning-01-after.jpg` | A dirty/stained headstone, then the same stone cleaned. Same angle, same framing for both. |
| **[MUST]** Before/after decorating | `before-after-decorating-01-before.jpg` / `before-after-decorating-01-after.jpg` | A bare grave, then the same grave with seasonal flowers/decoration placed. |
| **[NICE]** Extra before/after pair | `before-after-cleaning-02-before.jpg` / `-after.jpg` | Add more pairs over time as you do real jobs. |

### `images/services/`
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** Cleaning in progress | `cleaning-in-progress-01.jpg` | Soft brush on a headstone — shows the gentle, non-damaging method the copy promises. |
| **[MUST]** Finished decorated grave | `decorated-grave-01.jpg` | A completed seasonal decoration (e.g., Memorial Day or Easter flowers). |
| **[NICE]** Seasonal variety | `decorated-grave-easter-01.jpg`, `decorated-grave-christmas-01.jpg` | Different holidays, added across the year. Season name in the filename keeps them organized. |

### `images/about/`
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** The two owners | `owners.jpg` | A real, warm photo of your mom and her friend — ideally outdoors/at a cemetery, approachable. This is the biggest trust asset on the site; do NOT use a stock photo here. |
| **[NICE]** Owner at work | `owner-at-work-01.jpg` | One of them actually cleaning/decorating — reinforces "the same people who'll be there." |

### `images/service-area/`
One grounds shot per cemetery you serve. Filename = the cemetery, kebab-case (matches the page URLs in `seo-aio-strategy.md` §2).
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** Mt Carmel Cemetery | `mt-carmel-cemetery.jpg` | Respectful grounds or entrance shot. Helps the Mt Carmel page rank and proves you work there. |
| **[NICE]** Each added cemetery | `<cemetery-name>.jpg` | e.g., `our-lady-of-hope-cemetery.jpg`. One per cemetery as you add clients there. |

### `images/logo/`
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** Primary logo | `logo.png` | "Peace Blooming" wordmark + a simple flower/bloom motif. PNG with transparent background so it works on any color. Avoid religious imagery that isn't yours to use. |
| **[MUST]** Favicon | `favicon.png` | Small square version (just the bloom mark), 512×512px, for the browser tab. |
| **[NICE]** Vector logo | `logo.svg` | If a designer provides it — scales perfectly at any size. |
| **[NICE]** Light-on-dark version | `logo-white.png` | White version for use on dark backgrounds/footers. |

### `images/gbp/` (Google Business Profile — not the website)
Real photos here are your public "gallery" since the site has no big gallery (per `competitor-site-teardown.md`). Reuse the same naming rules. Add a few each season.
| Shot | Filename | Notes |
|---|---|---|
| **[MUST]** Profile/owners photo | `gbp-owners.jpg` | Can reuse `about/owners.jpg`. |
| **[MUST]** A few before/afters | `gbp-before-after-01.jpg` … | Reuse or add to the homepage pairs. |
| **[NICE]** Grounds/seasonal shots | `gbp-grounds-01.jpg`, `gbp-easter-01.jpg` | Post new ones around each seasonal push (§4 of the SEO guide). |

---

## Minimum set to launch
1. `home/hero.jpg`
2. `home/before-after-cleaning-01-before.jpg` + `-after.jpg`
3. `home/before-after-decorating-01-before.jpg` + `-after.jpg`
4. `services/cleaning-in-progress-01.jpg`
5. `services/decorated-grave-01.jpg`
6. `about/owners.jpg`
7. `service-area/mt-carmel-cemetery.jpg`
8. `logo/logo.png` + `logo/favicon.png`

Everything else is [NICE] and can be added over time — start with your mom's own family grave for the before/after and decoration shots, since she already tends it.

## What you do NOT need
- **No large photo gallery** — none of the 5 competitors run one; photos are framed as a delivered service, not a portfolio.
- **No stock photos** on About, GBP, or reviews — authentic photos read as more trustworthy and can rank better; stock can hurt.

# SEO & AI Search Strategy Guide
*Build guide for the site developer — not customer-facing.*
*Companion to: `grave-care-business-plan.md` and `competitor-site-teardown.md`*

## 0. Why This Is Winnable

1. **The out-of-town adult child searching "[cemetery] grave cleaning" starts on Google or an AI assistant, not a bulletin.** For that person, the website + Google Business Profile (GBP) is the whole acquisition channel.
2. **There's no strong local competitor to beat.** No dominant Detroit/Downriver grave-care brand has a real web presence, so decent fundamentals can win #1 rankings outright.
3. **The 5 real competitors reviewed in `competitor-site-teardown.md` (Tending, Gravesite Cleanup, Keeper of the Stones, Grave Care Services, Grave Conservation LLC) show no sign of a deliberate SEO/AI strategy** — no per-cemetery pages, no visible schema, no FAQ content. Even the more established operators haven't built this. Notes below tagged `[Teardown]` point back to specific evidence from that file.

Two channels to win: normal Google search (blue links, Local Pack) and AI answer engines (AI Overviews, ChatGPT, Perplexity, Gemini) — where a business needs to be the *cited* source, not just a ranked link. Same fix serves both: clear, specific, well-structured content.

---

## 1. Target Keywords & Intent

Search volume for phrases like "grave cleaning Wyandotte MI" is too small for keyword tools to register — that's fine. The goal is to be the only good answer to a small set of specific queries, not to win a big generic term.

**Primary (build a page around each):**
- "grave cleaning Wyandotte MI"
- "Mt Carmel Cemetery grave decoration / cleaning"
- "headstone cleaning Downriver Michigan"
- "cemetery flower service Wyandotte"
- "grave decorating service Metro Detroit"
- "[cemetery name] + grave cleaning" for each cemetery served, starting with Mt Carmel/Our Lady of the Scapular

**Secondary (blog/FAQ, catches research-stage traffic):**
- "how much does grave cleaning cost"
- "what flowers are allowed at [cemetery]"
- "how to clean a headstone without damaging it"
- "grave decoration rules Catholic cemetery Michigan"
- "grave care service for family who can't visit"

| Intent | Query | Page |
|---|---|---|
| Ready to hire, local | "grave cleaning Wyandotte MI" | Homepage + Service Area page |
| Ready to hire, cemetery-specific | "Mt Carmel Cemetery grave cleaning" | Dedicated cemetery page |
| Comparing/pricing | "how much does grave cleaning cost" | Services & Pricing + FAQ |
| Research/rules | "what flowers allowed at [cemetery]" | Blog post citing the actual policy |
| Out-of-town, anxious | "grave care for family who can't visit" | About/How It Works, photo-proof front and center |

**Gap `[Teardown]`:** none of the 5 competitors build individual per-cemetery pages — Tending and Grave Conservation LLC just list named cemeteries/counties in one paragraph. A page built specifically to answer "Mt Carmel Cemetery grave cleaning" has essentially no competition anywhere in the markets reviewed. This is the single biggest opportunity here.

---

## 2. Site Architecture

One dedicated page per core query — don't make one page try to rank for everything.

```
/ (Home)
/services-and-pricing
/how-it-works
/service-area
  /service-area/wyandotte               <- city page (lists all Wyandotte cemeteries)
  /service-area/brownstown              <- city page (lists all Brownstown cemeteries)
  /service-area/flat-rock               <- city page (lists all Flat Rock cemeteries)
  /service-area/riverview               <- city page (lists all Riverview cemeteries)
  /service-area/trenton                 <- city page (lists all Trenton cemeteries)
  /service-area/lincoln-park            <- city page (lists all Lincoln Park cemeteries)
  /service-area/woodhaven               <- city page (lists all Woodhaven cemeteries)
  /service-area/romulus                 <- city page (lists all Romulus cemeteries)
  /service-area/taylor                  <- city page (lists all Taylor cemeteries)
  /service-area/gibraltar               <- city page (lists all Gibraltar cemeteries)
  /service-area/brighton                <- city page (lists all Brighton city cemeteries)
  /service-area/brighton-township       <- city page (lists all Brighton Township cemeteries)
  /service-area/genoa-township          <- city page (lists all Genoa Township cemeteries)
  /service-area/green-oak-township      <- city page (lists all Green Oak Township cemeteries)
  /service-area/hamburg-township        <- city page (lists all Hamburg Township cemeteries)
  /service-area/livonia                 <- city page (lists all Livonia cemeteries) [NEW]
  /service-area/southfield              <- city page (lists all Southfield cemeteries) [NEW]
  /service-area/troy                    <- city page (lists all Troy cemeteries) [NEW]
  /service-area/dearborn-heights        <- city page (lists all Dearborn Heights cemeteries) [NEW]
  /service-area/farmington-hills        <- city page (lists all Farmington Hills cemeteries) [NEW]
  /service-area/mt-carmel-cemetery      <- dedicated cemetery page (Wyandotte, strict CFCS rules)
  /service-area/our-lady-of-hope-cemetery <- dedicated cemetery page (Brownstown, strict CFCS rules)
  /service-area/michigan-memorial-park  <- dedicated cemetery page (Flat Rock, moderate rules)
  /service-area/fairview-cemetery       <- dedicated cemetery page (Brighton, permit-based)
  /service-area/st-patricks-calvary-cemetery <- dedicated cemetery page (Brighton, parish)
  /service-area/holy-sepulchre-cemetery <- dedicated cemetery page (Southfield, strict CFCS rules) [NEW]
  /service-area/glen-eden-cemetery      <- dedicated cemetery page (Livonia, moderate rules) [NEW]
  /service-area/white-chapel-cemetery   <- dedicated cemetery page (Troy, unconfirmed rules) [NEW]
  /service-area/st-hedwig-cemetery      <- dedicated cemetery page (Dearborn Heights, moderate-strict) [NEW]
/about
/gallery
/faq
/blog
/contact
```

This architecture implements a two-layer SEO strategy: (1) city/township pages that answer "grave cleaning [city] MI" searches by listing all cemeteries in each city, and (2) dedicated cemetery pages for the most popular/established locations (Mt Carmel, Our Lady of Hope, Michigan Memorial Park, Fairview, St. Patrick's Calvary) that answer "[cemetery name] grave cleaning" searches. A page titled "Grave Cleaning & Decorating at Mt Carmel Cemetery" that names the cemetery, cites its real decoration policy, and shows real photos will out-rank a generic homepage for that search almost every time. City pages provide discoverability for smaller/less-known cemeteries while focusing search authority on the five established cemetery pages. Additional cemetery pages will be built as policies are confirmed and client demand justifies it.

**Structure `[Teardown]`:** Gravesite Cleanup runs a tight single-page funnel (hero → testimonial → services → process → pricing → CTA); Keeper of the Stones uses traditional multi-page nav. Do both: build the homepage as that same tight funnel, then repeat a condensed version of it (trust line → pricing → FAQ → CTA) on every service-area/cemetery page, so each indexable page converts on its own instead of being a thin location stub.

**Name places specifically `[Teardown]`:** Grave Conservation LLC names all 11 counties it serves individually instead of saying "the region." Do the same one level deeper — name Downriver cities (Wyandotte, Southgate, Riverview, Trenton, Woodhaven, etc.) and cemeteries by name on the service-area pages, not just "Downriver."

---

## 3. On-Page Content Rules

Google and AI Overviews reward the same thing: clear, specific, extractable answers.

1. **Answer first.** Open every page/section with a 1-2 sentence direct answer, then expand. E.g. "Yes, we clean and decorate graves at Mt Carmel Cemetery in Wyandotte, MI, following the cemetery's official decoration policy."
2. **Question-style headings.** "How much does grave cleaning cost near Wyandotte?" not "Our Pricing" — this is what featured snippets and AI Overviews pull from.
3. **Short, factual blocks (40-80 words).** Specific numbers and names beat vague adjectives like "professional" or "trusted."
4. **Use bullets, steps, and tables** wherever content is naturally structured — easier for AI and crawlers to parse than paragraphs.
5. **State cemetery, city, and price plainly** — "$60-$140 per visit," "serving Wyandotte, Downriver, Metro Detroit, and Metro Ann Arbor." Don't make anyone infer it.
6. **FAQ blocks on every key page**, not just one FAQ page — highest-leverage format for both AI citation and Google's People Also Ask.
7. **Cite the actual cemetery policy** ("per Mt Carmel Cemetery's official decoration policy...") — real sourced content most competitors won't bother writing.
8. **Publish real prices `[Teardown]`.** Gravesite Cleanup ($69 headstone cleaning, $199/yr care plan) and Keeper of the Stones ($100 single/$150 double stone) publish flat prices; Grave Care Services and Tending don't. Real numbers convert better *and* are exactly what AI Overviews extract — "contact for a quote" isn't answerable.
9. **Skip the big gallery `[Teardown]`.** None of the 5 competitors run a public before/after grid — they all treat photos as something delivered privately to the client, not a portfolio page. Don't feel pressure to stock `/gallery` before launch; a few real photos are enough. Put the writing effort into FAQ and pricing content instead.
10. **Lead with the personal story, but don't bury the trust signals `[Teardown]`.** Grave Care Services opens with the owner's story and puts its testimonial at the bottom; Gravesite Cleanup puts a short testimonial right after the hero. Since your mom's real story (her own parents' grave, deep Wyandotte roots) is stronger than any generic "family owned" line, lead with it — but still put a short trust line (insured, photo-proof, knows the cemetery rules) right below the hero, not buried at the bottom.

---

## 3.5. Competitor Gaps to Exploit `[Teardown]`

This was a front-end review of what's visible on each site, not a code audit — "no evidence of X" means "not visible on the page," not "confirmed absent." Treat it as a good directional read, not a guarantee.

| Gap across the 5 competitors | Opportunity | Handled in |
|---|---|---|
| No per-cemetery/county pages, only list mentions | No real competition for "[cemetery] grave cleaning" | Section 2 |
| No visible FAQ content | Cheap to write, exactly what AI Overviews reward | Section 3, Section 8 |
| No visible schema markup | Minimal JSON-LD is a real edge here | Section 5 |
| Only Tending writes any educational content; the other 4 are purely transactional | A real blog cadence is close to uncontested | Section 8 |
| Only Tending states its insurance coverage | A concrete number is a cheap trust signal | Section 5, Section 4 |
| No sign anyone's thought about AI crawler access | Clean-sheet advantage | Section 6 |

These competitors are winning on real service quality and personal trust, not SEO. That's the gap this plan is built to use.

---

## 4. Google Business Profile — Priority #1

GBP often matters more than the website for "near me" searches, and feeds directly into Google's AI Overviews.

- [ ] Claim/verify GBP under the exact legal business name (no keyword-stuffed names — Google suspends profiles for this).
- [ ] Pick the closest available category (no direct "Cemetery" option — try Landscaper/Gardener/Cleaning Service; confirm at setup since categories change).
- [ ] List the actual service area (cities/ZIPs), not one pin — this is a mobile business.
- [ ] Fill every field: hours, phone, website, and each service named individually.
- [ ] Write the ~750-character description with the value prop and 2-3 target locations in the first sentence.
- [ ] Post real before/after photos regularly — no stock photos. `[Teardown]`: since no competitor runs a public gallery, GBP photos are effectively the primary public portfolio at launch.
- [ ] Seed the Q&A with likely questions ("Do you serve Mt Carmel Cemetery?").
- [ ] Post updates at least monthly, ideally around each seasonal push.
- [ ] **Reviews matter most here.** Ask after every job, and nudge clients to mention the cemetery and service by name ("cleaned my mom's grave at Mt Carmel, put out Easter flowers") — specific reviews outweigh star rating alone for both Google's algorithm and AI sentiment reading.
- [ ] Reply to every review personally, not with a template.

---

## 5. Structured Data (Schema Markup)

Tells Google and AI systems exactly what the business is, where it works, and what it costs. Use JSON-LD.

- **Homepage:** `LocalBusiness` entity as the single source of truth.
- **Every service-area/cemetery page:** reference that same entity via `@id`, plus `areaServed` naming the specific city/cemetery. `[Teardown]`: name the cemetery itself as an entity, e.g. `{"@type": "Cemetery", "name": "Mt Carmel Cemetery"}`, the way Tending names specific cemeteries in its copy.
- **Services & Pricing page:** `Service` schema per service with real `offers` pricing — never leave it as a placeholder at launch.
- **FAQ blocks:** `FAQPage` schema on every page that has one.
- **Reviews:** only mark up real reviews actually collected — never fabricate `Review`/`AggregateRating` schema; Google penalizes this.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.peaceblooming.com/#business",
  "name": "Peace Blooming",
  "telephone": "[phone]",
  "priceRange": "$60-$400",
  "areaServed": [
    {"@type": "City", "name": "Wyandotte, MI"},
    {"@type": "City", "name": "Detroit, MI"},
    {"@type": "City", "name": "Ann Arbor, MI"}
  ],
  "address": {"@type": "PostalAddress", "addressLocality": "Brighton", "addressRegion": "MI", "addressCountry": "US"},
  "sameAs": ["https://www.google.com/maps/place/[GBP link]", "https://www.facebook.com/[page]"]
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Headstone Cleaning",
  "provider": {"@id": "https://www.peaceblooming.com/#business"},
  "areaServed": {"@type": "City", "name": "Wyandotte, MI"},
  "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "[final price]", "description": "One-time visit; discount for an additional grave same visit"}
}
```
*(Benchmarks used to sanity-check pricing: Gravesite Cleanup's $69/$199-per-year, Keeper of the Stones' $100/$150 per stone — use this business's own decided numbers, not these.)*

**Insurance `[Teardown]`:** once liability insurance is bound, state the real coverage amount on the homepage and in the schema — Tending states "$2M general liability insurance" plainly and it reads as genuine trust, not marketing.

**Validate** every page with Google's Rich Results Test before launch, then recheck monthly via Search Console.

---

## 6. AI Search (AIO/AEO/GEO) Tactics

Beyond standard SEO, to get cited by AI assistants:

1. **Allow the crawlers.** `robots.txt` must explicitly allow `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Claude-SearchBot`, `Google-Extended` — some site builders block these by default, which makes a site invisible to AI answer engines.
2. **Server-render the content.** Many AI crawlers don't run JavaScript — core text (services, pricing, FAQ) must be in the raw HTML.
3. **`llms.txt`:** a nice-to-have, not proven to matter yet. Ten minutes of work, low priority — don't let it distract from schema/content work.
4. **Platform notes:** ChatGPT leans on Bing's index (get listed on Bing Places, Yelp, BBB too). Perplexity rewards freshness and pulls from Yelp/Reddit — genuine, non-promotional participation in a local subreddit can help. Google's AI Overviews mostly run on the same signals as normal ranking + GBP, so Sections 3-5 already cover it.
5. **Get mentioned elsewhere.** Yelp, Bing Places, Nextdoor, local Facebook groups, a parish bulletin mention — every independent mention with matching name/address/phone builds AI "entity confidence."

---

## 7. Local Citations & NAP Consistency

Use the exact same Name, Address/service area, and Phone everywhere: GBP, Bing Places, Yelp, Facebook, Nextdoor, Apple Business Connect, and any parish/diocese directory. Small mismatches ("Wyandotte, MI" vs. "Wyandotte, Michigan") quietly hurt local ranking — keep one master copy of the NAP text and paste it everywhere rather than retyping.

---

## 8. Content Plan — First 6 Pieces

1. **"Grave Cleaning & Decorating at Mt Carmel Cemetery: What's Allowed"** — cites the real policy; highest-value page given the research already done.
2. **"How Much Does Grave Cleaning Cost in Michigan?"** — matches the pricing page, captures comparison searches.
3. **"How to Clean a Headstone Without Damaging It"** — real how-to content (soft brushes, no bleach/pressure washers), high national search interest.
4. **"Cemetery Decoration Rules Before Memorial Day / Christmas"** — seasonal, refreshed yearly, good repeat-citation candidate.
5. **"Grave Care for Families Who Live Out of State"** — speaks to the highest-value persona directly.
6. **FAQ page** — pricing, service area, photo-proof, insurance, what's not allowed, cancellations.

Refresh or add one piece per season (Easter, Memorial Day, All Souls Day, Christmas) — keeps a freshness signal going and matches the business's real seasonal rhythm.

**All Souls' Day content opportunity (high ROI, seasonal):** Metro Detroit Catholic communities (particularly in Livonia, Southfield, Dearborn Heights, and surrounding Downriver areas) observe All Souls' Day (November 1–2) with elaborate grave decoration — chrysanthemums, wreaths, votive candles, family visits. A piece like **"All Souls' Day Cemetery Traditions in Metro Detroit: Fresh Flowers, Wreaths, and How We Help"** would target seasonal search intent specific to these communities and position the business as understanding local Catholic cemetery culture. Similarly, Polish-American families around Hamtramck and Warren observe these traditions intensely. This content angle is nearly uncontested — most grave-care competitors don't acknowledge cultural/seasonal decoration traditions at all.

**Second wave, once the first 6 are live `[Teardown]`:**
- "Why We Only Work March Through November" — modeled on Grave Conservation LLC's no-work-below-40°F policy; sets honest expectations and explains freeze damage to stone.
- "Grave Location Mapping for Family Genealogy Research" — modeled on Gravesite Cleanup's GPS pin-drop add-on; a phone photo + map pin costs nothing extra on a visit already happening.
- "What Does a Grave Care 'Concierge' Actually Do?" — borrows Keeper of the Stones' concierge framing.
- "Is Your Grave Cleaning Company Insured?" — once insurance is bound, discloses this business's coverage (like Tending does) while giving readers a real vetting checklist.
- "One-on-One, Not a Franchise" — a positioning piece in your mom's own voice, echoing Grave Care Services' relationship-first story.

---

## 9. Measurement & KPIs

| Metric | Tool | Why |
|---|---|---|
| Local Pack ranking | Manual search / Search Console | Visibility for "near me" searches |
| GBP calls, directions, clicks | GBP Insights (free) | Direct lead measure |
| Organic clicks/impressions by page | Search Console (free) | Which pages/queries work |
| Phone calls and conversion | Google forwarding number (GBP, free) + optional tracked number (~$20–30/mo, e.g. CallRail) | Direct lead attribution; tie inbound calls to source |
| AI Overview appearance | Manual test queries, monthly | No dedicated tool exists yet |
| Review count, rating, recency | GBP + Yelp | Core trust signal |
| NAP consistency | Quarterly manual check | Catches silent ranking decay |
| Form submissions by source | Intake form "How did you hear about us?" field → simple tracking spreadsheet | Attribution for online leads |

**Phone call tracking (no-cost and low-cost options):**
- **Free option:** Google Business Profile forwarding number. Set up in GBP → "Calls" section → enable a forwarding number. Google will show you a monthly count of calls and (if enabled) let you listen to a log. Minimal friction, works on all GBP displays.
- **Low-cost paid option:** CallRail or similar (~$20–30/month) provides per-call attribution, recording, and conversion tracking (which calls lead to bookings). Worth the investment if you want to tie specific calls to specific marketing sources (e.g., "This call came from a Google search, and it converted to a $200/year plan").
- **Hybrid approach:** Use GBP free forwarding for volume, add CallRail later if call volume justifies it.
- **Manual log:** Create a simple monthly spreadsheet tracking (call date, source from form submission or GBP label, outcome: inquiry / booked / no follow-up). Over 3–6 months, patterns will show which channels drive actual bookings.

**Lead-source KPI (tied to new form field):**
The "How did you hear about us?" form field on the intake form is critical. Log responses in a simple spreadsheet indexed by month and source, then measure conversion rate (inquiries → bookings) by source. Example:
- Google: 8 inquiries → 5 bookings (62% conversion)
- Facebook: 3 inquiries → 1 booking (33% conversion)
- Referral: 4 inquiries → 4 bookings (100% conversion)

This tells you where to spend marketing effort and reinforces the importance of asking every lead "How did you find us?"

**Timeline:** local SEO for a new site typically takes 3-6 months to gain traction, even in a low-competition niche. Bulletins and word of mouth are the near-term bridge while search visibility builds.

---

## 9.5. Hosting (for a hardcoded/static site)

Hand-coded HTML/CSS/JS is actually the best-case setup here — inherently server-rendered, schema can be pasted straight into each page's `<head>`.

Build it as true multi-page (`/index.html`, `/services.html`, `/service-area/mt-carmel.html`, etc.), not one long scroll.

- **Cloudflare Pages** — fastest, unlimited bandwidth on the free tier. Best default.
- **Netlify** — similar performance, plus built-in form handling for the intake form.
- **GitHub Pages** — free and simple, but needs a third-party form service (Formspree).
- Shared hosting (Bluehost/GoDaddy) — avoid; slower, which hurts local rankings.

**Forms:** a static site has no backend, so the intake form (see `client-intake-process.md`) needs Netlify Forms or Formspree.

## 10. Build Checklist

- [ ] Fast, mobile-first, server-rendered pages
- [ ] One named page per service area/cemetery, not one generic "areas we serve" page
- [ ] Homepage follows the funnel structure from Section 2 (story → trust line → pricing → how it works → service area → FAQ → CTA)
- [ ] Real prices published — no "contact for quote"
- [ ] Gallery kept small; photos framed as a delivered feature, not a portfolio requirement
- [ ] Answer-first copy, question-style headings, FAQ block on every key page
- [ ] JSON-LD schema on every relevant page, validated before launch
- [ ] `robots.txt` allows the AI crawlers in Section 6
- [ ] GBP fully built out before/at launch
- [ ] NAP identical everywhere
- [ ] First 6 content pieces written at or shortly after launch
- [ ] Analytics + Search Console installed at launch

---

## Sources & Confidence

Built from current (2026) public local-SEO/AI-search best practices, the cemetery facts already verified in `grave-care-business-plan.md`, and direct review of 5 real competitor sites in `competitor-site-teardown.md`.

- **High confidence:** GBP optimization, NAP consistency, schema markup, answer-first content — well-established, consistent across sources.
- **High confidence, directly observed:** everything tagged `[Teardown]` is based on actually looking at 5 live competitor sites. What those sites show is solid; what to *conclude* from it (a gap = an opportunity) is a reasonable read, not a guarantee — especially since this was a front-end review, not a code audit.
- **Medium confidence:** platform-specific AI tactics (crawler allow-lists, ChatGPT/Perplexity quirks) — directionally right but changing fast; revisit every few months.
- **Low confidence:** `llms.txt` — cheap to add, no proven benefit yet. Don't prioritize it.

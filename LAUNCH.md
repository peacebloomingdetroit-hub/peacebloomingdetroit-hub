# Peace Blooming Launch Runbook

This checklist walks you from the current state of the website to a live, indexed, and ready-for-business launch.

## Pre-Launch — Website & Copy (can be done now)

- [ ] Run `python3 build_site.py` to regenerate all pages.
- [ ] Run `python3 pre_launch_check.py` to catch any remaining placeholders or missing assets.
- [ ] Review every page at `http://localhost:8000` after running `python3 -m http.server 8000 --directory site`.
- [ ] Replace any remaining `[PHONE]`, `[EMAIL]`, `[COVERAGE AMOUNT]`, `[RESPONSE TIME]`, `[PHOTOS]` placeholders in `website-copy.md` and `build_site.py`, then rebuild.
- [ ] Replace placeholder images in `site/images/` with real photos per `photo-shot-list.md`.
- [ ] Verify the social sharing image at `site/images/social/default.jpg` is a real branded 1200×630 image.
- [ ] Fill in `GA_MEASUREMENT_ID` and `GOOGLE_SEARCH_CONSOLE_TAG` in `build_site.py` (top of file) and rebuild.

## Business Setup (blocking launch)

- [ ] Confirm `Peace Blooming LLC` is available via Michigan LARA name search.
- [ ] File Michigan LLC registration.
- [ ] Register `peaceblooming.com` (or confirm availability and purchase).
- [ ] Set up business phone number (local 734 or 810 area recommended for trust).
- [ ] Set up business email (hello@peaceblooming.com).
- [ ] Bind general liability insurance and note the coverage amount.
- [ ] Confirm business address (or use a mail forwarding service per `business-address-options.md`).

## Domain & Hosting

- [ ] In Netlify, add the custom domain `peaceblooming.com`.
- [ ] Update DNS at your registrar to point to Netlify (CNAME for `www`, A record for apex, or use Netlify nameservers).
- [ ] Verify the site loads at `https://peaceblooming.com` and `https://www.peaceblooming.com`.
- [ ] Confirm SSL certificate is provisioned automatically by Netlify.

## Google Setup

- [ ] Create a Google Analytics 4 property and copy the Measurement ID into `build_site.py`.
- [ ] Create a Google Search Console property for `peaceblooming.com`.
- [ ] Copy the Search Console verification meta tag into `build_site.py`.
- [ ] Rebuild and redeploy.
- [ ] Submit `https://peaceblooming.com/sitemap.xml` to Search Console.
- [ ] Request indexing for the homepage and a few key service-area pages.

## Google Business Profile

- [ ] Create or claim the Google Business Profile once the LLC and address are confirmed.
- [ ] Add business hours, services, and description.
- [ ] Upload 20–30 photos per `photo-shot-list.md` (exterior, work, team, before/after).
- [ ] Set up call tracking or forward the GBP number to the business phone.
- [ ] Add a link to the website and request reviews from early customers.

## Final Testing

- [ ] Test the contact form end-to-end: submit on `/contact.html` and confirm the email is received.
- [ ] Test the newsletter signup form on the footer and confirm it redirects to `/newsletter-success.html`.
- [ ] Test the 404 redirect by visiting a non-existent URL.
- [ ] Validate schema markup with [Google Rich Results Test](https://search.google.com/test/rich-results).
- [ ] Test mobile layout on iOS Safari and Android Chrome.
- [ ] Check page speed with [PageSpeed Insights](https://pagespeed.web.dev/).
- [ ] Verify all internal links with `python3 pre_launch_check.py`.
- [ ] Confirm phone numbers and email links are clickable and correct.

## Post-Launch

- [ ] Monitor Search Console for crawl errors and indexing issues.
- [ ] Set up regular Google Business Profile posts and photo updates.
- [ ] Publish the first blog post from the planned list in `website-copy.md`.
- [ ] Ask satisfied customers for reviews and respond to them promptly.

## Netlify Form Notifications Setup

After you deploy the site, configure Netlify so form submissions actually reach you:

1. Go to your Netlify dashboard and open the Peace Blooming site.
2. Deploy the latest changes from GitHub (`git push origin main`).
3. Wait for the deploy to finish, then go to **Forms** in the top navigation.
4. You should see two forms:
   - `service-request` (contact form)
   - `newsletter` (email signup)
5. If a form is missing, confirm the form HTML is present in the deployed files and redeploy.
6. Go to **Site settings → Forms → Form notifications**.
7. Click **Add notification → Email**.
8. Select the form (`service-request` or `newsletter`) and enter the email address that should receive submissions (e.g. `hello@peaceblooming.com`).
9. Repeat for the other form.
10. Optional: turn on **daily or weekly submission summaries** in the same section.

**Important:** Netlify does not send email notifications by default. Without this step, submissions are only stored in the dashboard and you have to log in to see them.

## Quick Commands
## Quick Commands

```bash
cd "/Users/themachine2.0/Desktop/AI/Peace Blooming/3-Website"
python3 build_site.py
python3 pre_launch_check.py
python3 -m http.server 8000 --directory site
```
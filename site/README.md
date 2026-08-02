# Peace Blooming Website

A static site for Peace Blooming, a grave cleaning and seasonal flower decorating service in Michigan.

## About

This is the website for Peace Blooming, serving Wyandotte, Downriver, Metro Detroit, and Metro Ann Arbor with professional grave cleaning and seasonal decorating services. The site is built as a pure static HTML/CSS site with no server-side processing or build step — just open the files in a browser or deploy directly to any host.

## File Structure

```
site/
├── index.html                     # Home page
├── services-and-pricing.html      # Pricing and services
├── how-it-works.html              # Process explanation
├── service-area.html              # Main service area page
├── service-area/                  # City and cemetery pages
│   ├── wyandotte.html
│   ├── brownstown.html
│   ├── ... (18 more cities)
│   ├── mt-carmel-cemetery.html
│   ├── our-lady-of-hope-cemetery.html
│   └── ... (7 more cemetery pages)
├── about.html                     # About the business
├── faq.html                       # Full FAQ
├── contact.html                   # Contact form
├── blog.html                      # Blog (coming soon)
├── gallery.html                   # Gallery (coming soon)
├── css/
│   └── style.css                  # All styling
├── images/
│   ├── home/                      # Hero, before/afters
│   ├── services/                  # Service photos
│   ├── about/                     # Owner photo
│   ├── service-area/              # Cemetery photos
│   └── logo/                      # Logo and favicon
├── robots.txt                     # Search engine rules
├── sitemap.xml                    # Page listing for search engines
├── netlify.toml                   # Netlify deployment config
└── README.md                      # This file
```

## Preview Locally

To preview the site on your computer before deploying:

1. Open Terminal and navigate to this folder:
   ```bash
   cd /Users/themachine2.0/Desktop/AI/Peace\ Blooming/3-Website/site
   ```

2. Start a simple web server:
   ```bash
   python3 -m http.server 8000
   ```

3. Open your browser to `http://localhost:8000` and you should see the home page.

4. Click through pages to test links. Press `Ctrl+C` in Terminal to stop the server when done.

## Deploy to Netlify (Step-by-Step)

Peace Blooming is set up to deploy to Netlify's free tier via GitHub. Here's how:

### Step 1: Push the Site to GitHub

1. In your Terminal, from inside the `site/` folder:
   ```bash
   git init
   git add .
   git commit -m "Initial site build"
   ```

2. Create a new repository on GitHub (https://github.com/new) named `peace-blooming` (or anything you like). Don't add a README, license, or .gitignore — just create the empty repo.

3. Follow the "push an existing repository" instructions GitHub shows you. It'll look something like:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/peace-blooming.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Connect to Netlify

1. Go to https://app.netlify.com/ and sign in (or create a free account).

2. Click "Add new site" → "Import an existing project".

3. Select GitHub as the provider and sign in.

4. Choose the `peace-blooming` repository you just pushed.

5. In the deployment settings:
   - **Build command**: leave blank (no build needed)
   - **Publish directory**: `.` (the root of the repo)

6. Click "Deploy site" and wait ~1 minute. Netlify will assign you a temporary URL like `peace-blooming-abc123.netlify.app`.

### Step 3: Add Your Custom Domain

1. On the Netlify dashboard, go to your site's settings.

2. Under "Domain management" → "Custom domains", click "Add domain" and enter `peaceblooming.com`.

3. Netlify will ask you to verify the domain by updating your DNS records.

4. Log in to wherever you bought the domain (GoDaddy, Namecheap, etc.) and update the nameservers or create a CNAME record pointing to Netlify. Netlify's site will show you exactly what to do.

5. DNS changes take a few minutes to propagate. Once done, `https://peaceblooming.com` will show your live site.

### Step 4: Enable HTTPS

Netlify automatically provides a free SSL certificate. In the Netlify site settings, confirm that "HTTPS" is enabled and "Force HTTPS" is toggled on so all traffic is secure.

## Before Going Live — Update Placeholders

In the HTML files, you'll see placeholders in **[brackets]** that need real values before launch:

- `[PHONE]` — Add the phone number in `/index.html`, `/contact.html`, footer, etc.
- `[EMAIL]` — Set to `hello@peaceblooming.com` in `/contact.html` and footer.
- `[COVERAGE AMOUNT]` — Insurance limit on `/about.html` and `/faq.html`.
- `[RESPONSE TIME]` — Response promise on `/contact.html` (e.g., "24 hours").
- `[PHOTOS]` — Replace placeholder images with real photos.

Use Find & Replace in your text editor to update `[PHONE]` everywhere at once.

## Forms & Contact

The contact form on `/contact.html` uses Netlify Forms. Once your site is live on Netlify, form submissions will automatically go to your Netlify dashboard. No backend needed.

## Updates & Maintenance

This `site/` folder is generated by `build_site.py` in the parent folder. To make changes:

1. Edit `website-copy.md` or `build_site.py` in the project root.
2. Run `python3 build_site.py` from the project root.
3. Test locally: `cd site && python3 -m http.server 8000`.
4. Commit and push from the project root: `git add . && git commit -m "..." && git push`.
5. Netlify auto-deploys the `site/` folder within seconds.

## SEO Notes

- Each page has title tags, descriptions, and JSON-LD schema for search engines.
- `robots.txt` allows AI search crawlers (ChatGPT, Perplexity, etc.).
- `sitemap.xml` lists all pages for Google.
- The site is mobile-first and fast (no JavaScript frameworks or build steps).

## Questions?

For help, refer to the project docs in the parent folder (`/Users/themachine2.0/Desktop/AI/Peace Blooming/3-Website/`):

- `website-copy.md` — Full content for every page
- `seo-aio-strategy.md` — SEO and search strategy
- `photo-shot-list.md` — Image naming and organization
- `visual-design-plan.md` — Design palette, typography, and layout notes

---

Built with Python. Last updated: 2026-08-02

# Peace Blooming Website

Static website for **Peace Blooming** — a grave cleaning and seasonal flower decorating service in Michigan.

## Project layout

- `build_site.py` — Python generator that rebuilds all 38 pages from `website-copy.md`
- `website-copy.md` — Master copy for all page content
- `seo-aio-strategy.md` — SEO and AIO strategy
- `photo-shot-list.md` — Image naming guide and shot list
- `visual-design-plan.md` — Design palette, typography, and layout notes
- `logo-prompt.md` — Logo generation prompt (archived)
- `CHANGELOG.md` — Project history
- `site/` — Generated static site deployed to Netlify

## Local development

```bash
cd "~/Desktop/AI/Peace Blooming/3-Website"
python3 build_site.py
python3 -m http.server 8000 --directory site
```

Open http://localhost:8000

## Deploying

Netlify is connected to this repo. The publish directory is `site/`.

1. Edit `website-copy.md` or `build_site.py`
2. Run `python3 build_site.py`
3. Commit and push:

```bash
git add .
git commit -m "describe your change"
git push origin main
```

Netlify will deploy the updated `site/` folder automatically.

## Requirements

```bash
pip install -r requirements.txt
```

Only needed to run `build_site.py` locally.

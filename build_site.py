#!/usr/bin/env python3
"""
Peace Blooming Static Site Generator
Generates ~38-page website from website-copy.md, seo-aio-strategy.md, and photo-shot-list.md
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Configuration
PROJECT_ROOT = Path("/Users/themachine2.0/Desktop/AI/Peace Blooming/3-Website")
SITE_ROOT = PROJECT_ROOT / "site"
IMAGES_DIR = SITE_ROOT / "images"
CSS_DIR = SITE_ROOT / "css"
SERVICE_AREA_DIR = SITE_ROOT / "service-area"

# Ensure directories exist
SITE_ROOT.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(exist_ok=True)
CSS_DIR.mkdir(exist_ok=True)
SERVICE_AREA_DIR.mkdir(exist_ok=True)

# Subdirectories for images
for subdir in ["home", "services", "about", "service-area", "logo"]:
    (IMAGES_DIR / subdir).mkdir(exist_ok=True)

# ============================================================================
# READ SOURCE DOCUMENTS
# ============================================================================

def read_source_file(filename):
    """Read a source markdown file."""
    path = PROJECT_ROOT / filename
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

website_copy = read_source_file("website-copy.md")
seo_strategy = read_source_file("seo-aio-strategy.md")
photo_shot_list = read_source_file("photo-shot-list.md")

# ============================================================================
# PARSE WEBSITE COPY
# ============================================================================

def extract_section(content, section_name, end_marker=None):
    """Extract a section from markdown by heading."""
    # Find the section start
    marker = f"## {section_name}"
    if marker not in content:
        return None
    
    start = content.find(marker) + len(marker)
    
    # Find the end (next ## or end of document)
    if end_marker:
        end = content.find(f"## {end_marker}", start)
    else:
        end = content.find("\n## ", start + 1)
    
    if end == -1:
        end = len(content)
    
    return content[start:end].strip()


def strip_internal_notes(text):
    """Remove internal notes from public-facing location page copy.

    Keeps useful parenthetical facts (e.g. parish names) but removes
    business-owner-only notes like 'policy unconfirmed — call ahead'.
    """
    if not text:
        return text

    # Remove '[see dedicated page]' and any following em-dash phrase
    text = re.sub(r'\s*—\s*\[see dedicated page\][^\n]*', '', text, flags=re.IGNORECASE)

    # Remove parenthetical notes containing internal status keywords
    text = re.sub(
        r'\s*\([^)]*(?:policy unconfirmed|call ahead|call to confirm)[^)]*\)',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove stray em-dash policy notes
    text = re.sub(r'\s*—\s*(?:Strict CFCS policy|CFCS policy)[^\n]*', '', text, flags=re.IGNORECASE)

    # Replace weak "confirm availability" language with confident service language
    text = re.sub(
        r'Call us to confirm availability at your specific cemetery, or start with a quote for Mt Carmel\.?',
        'Start with a quote for Mt Carmel, or reach out about any cemetery in this area.',
        text,
        flags=re.IGNORECASE
    )

    # Clean up double spaces left behind
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def markdown_to_html(text):
    """Convert simple markdown to HTML. Handles headings, bold, lists, paragraphs."""
    if not text:
        return ""

    # Remove internal notes before rendering
    text = strip_internal_notes(text)

    # Replace bare HTML entities so user-supplied text stays safe
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Inline bold: **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    # Markdown links: [text](url)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)

    lines = text.splitlines()
    html = []
    in_list = False
    in_para = False
    para_lines = []

    for raw_line in lines:
        line = raw_line.strip()
        if line == "":
            if in_list:
                html.append("</ul>")
                in_list = False
            if in_para:
                html.append("<p>" + " ".join(para_lines) + "</p>")
                para_lines = []
                in_para = False
            continue

        # Horizontal rule
        if line == "---":
            continue

        # Headings (top-level # becomes h2 because the template already provides an h1)
        if line.startswith("### "):
            html.append(f"<h3>{line[4:]}</h3>")
            continue
        if line.startswith("## "):
            html.append(f"<h2>{line[3:]}</h2>")
            continue
        if line.startswith("# "):
            html.append(f"<h2>{line[2:]}</h2>")
            continue

        # List item
        if line.startswith("- ") or line.startswith("* "):
            if in_para:
                html.append("<p>" + " ".join(para_lines) + "</p>")
                para_lines = []
                in_para = False
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{line[2:]}</li>")
            continue

        # Regular paragraph line
        if in_list:
            html.append("</ul>")
            in_list = False
        in_para = True
        para_lines.append(line)

    if in_list:
        html.append("</ul>")
    if in_para:
        html.append("<p>" + " ".join(para_lines) + "</p>")

    return "\n\n".join(html)


# Extract main sections
home_content = extract_section(website_copy, "Home", "Trust line")
services_content = extract_section(website_copy, "Services & Pricing", "Seasonal Care Plans")
howItWorks_content = extract_section(website_copy, "How It Works", "Service Area")
serviceArea_content = extract_section(website_copy, "Service Area", "Service by City")
about_content = extract_section(website_copy, "About", "FAQ")
faq_content = extract_section(website_copy, "FAQ", "Contact")
contact_content = extract_section(website_copy, "Contact", "Service Area — Our Lady")

# Extract cemetery pages
mt_carmel = extract_section(website_copy, "Mt Carmel Cemetery", "Service Area — Our Lady")
our_lady_hope = extract_section(website_copy, "Our Lady of Hope Cemetery", "Michigan Memorial Park")
michigan_memorial = extract_section(website_copy, "Michigan Memorial Park", "Fairview Cemetery")
fairview = extract_section(website_copy, "Fairview Cemetery", "St. Patrick's Calvary")
st_patricks = extract_section(website_copy, "St. Patrick's Calvary Cemetery", "Holy Sepulchre")
holy_sepulchre = extract_section(website_copy, "Holy Sepulchre Catholic Cemetery", "Glen Eden")
glen_eden = extract_section(website_copy, "Glen Eden Lutheran Memorial Park", "White Chapel")
white_chapel = extract_section(website_copy, "White Chapel Memorial Park Cemetery", "St. Hedwig")
st_hedwig = extract_section(website_copy, "St. Hedwig Cemetery", "Service Area — City Pages")

# Cemetery data: (name, city, content_key)
CEMETERIES = [
    ("mt-carmel-cemetery", "Mt Carmel Cemetery", "Wyandotte"),
    ("our-lady-of-hope-cemetery", "Our Lady of Hope Cemetery", "Brownstown"),
    ("michigan-memorial-park", "Michigan Memorial Park", "Flat Rock"),
    ("fairview-cemetery", "Fairview Cemetery", "Brighton"),
    ("st-patricks-calvary-cemetery", "St. Patrick's Calvary Cemetery", "Brighton"),
    ("holy-sepulchre-cemetery", "Holy Sepulchre Catholic Cemetery", "Southfield"),
    ("glen-eden-cemetery", "Glen Eden Lutheran Memorial Park", "Livonia"),
    ("white-chapel-cemetery", "White Chapel Memorial Park Cemetery", "Troy"),
    ("st-hedwig-cemetery", "St. Hedwig Cemetery", "Dearborn Heights"),
]

# City pages: (slug, city_name, region)
CITIES = [
    ("wyandotte", "Wyandotte", "Downriver"),
    ("brownstown", "Brownstown", "Downriver"),
    ("flat-rock", "Flat Rock", "Downriver"),
    ("riverview", "Riverview", "Downriver"),
    ("trenton", "Trenton", "Downriver"),
    ("lincoln-park", "Lincoln Park", "Downriver"),
    ("woodhaven", "Woodhaven", "Downriver"),
    ("romulus", "Romulus", "Downriver"),
    ("taylor", "Taylor", "Downriver"),
    ("gibraltar", "Gibraltar", "Downriver"),
    ("brighton", "Brighton", "Livingston County"),
    ("brighton-township", "Brighton Township", "Livingston County"),
    ("genoa-township", "Genoa Township", "Livingston County"),
    ("green-oak-township", "Green Oak Township", "Livingston County"),
    ("hamburg-township", "Hamburg Township", "Livingston County"),
    ("livonia", "Livonia", "Metro Detroit"),
    ("southfield", "Southfield", "Metro Detroit"),
    ("troy", "Troy", "Metro Detroit"),
    ("dearborn-heights", "Dearborn Heights", "Metro Detroit"),
    ("farmington-hills", "Farmington Hills", "Metro Detroit"),
]

# ============================================================================
# GENERATE PLACEHOLDER IMAGES
# ============================================================================

def create_placeholder_image(filepath, text, width=1600, height=900, bg_color=(230, 240, 230)):
    """Create a placeholder image with text."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    # Create image with gradient-like effect
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a built-in font, fall back to default if not available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
    except:
        font = ImageFont.load_default()
    
    # Center text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill=(100, 120, 100), font=font)
    img.save(filepath, 'PNG')

def generate_logo_variants(source_path=None):
    """Generate logo.png, favicon.png, and apple-touch-icon.png from the supplied mark image.
    If no source image is provided, falls back to the original text-based placeholders.
    """
    source_path = source_path or IMAGES_DIR / "logo" / "logo-source.png"
    logo_path = IMAGES_DIR / "logo" / "logo.png"
    favicon_path = IMAGES_DIR / "logo" / "favicon.png"
    apple_path = IMAGES_DIR / "logo" / "apple-touch-icon.png"

    if not source_path.exists():
        # Fallback to the previous text-based logo and favicon
        img = Image.new('RGBA', (400, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        except Exception:
            font = ImageFont.load_default()
        draw.text((20, 20), "Peace Blooming", fill=(100, 130, 100, 255), font=font)
        img.save(str(logo_path), 'PNG')

        favicon = Image.new('RGBA', (512, 512), (230, 240, 230, 255))
        draw = ImageDraw.Draw(favicon)
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 120)
        except Exception:
            font = ImageFont.load_default()
        draw.text((150, 160), "❀", fill=(100, 130, 100, 255), font=font)
        favicon.save(str(favicon_path), 'PNG')
        return

    src = Image.open(source_path).convert('RGBA')
    # Build a mask from the dark mark (background is light cream)
    mask = Image.new('L', src.size, 0)
    px = mask.load()
    for y in range(src.height):
        for x in range(src.width):
            r, g, b, a = src.getpixel((x, y))
            if max(r, g, b) < 200:
                px[x, y] = 255

    # Crop to the mark
    bbox = mask.getbbox()
    if bbox:
        mask = mask.crop(bbox)

    brand_green = (44, 62, 50, 255)  # #2c3e32
    white = (255, 255, 255, 255)

    def make_layer(color):
        layer = Image.new('RGBA', mask.size, color)
        layer.putalpha(mask)
        return layer

    green_mark = make_layer(brand_green)
    white_mark = make_layer(white)

    def center_paste(canvas, layer, pad_frac=0.12):
        size = canvas.width
        max_w = int(size * (1 - 2 * pad_frac))
        max_h = int(size * (1 - 2 * pad_frac))
        scale = min(max_w / layer.width, max_h / layer.height)
        new_w = max(1, int(layer.width * scale))
        new_h = max(1, int(layer.height * scale))
        resized = layer.resize((new_w, new_h), Image.LANCZOS)
        x = (size - new_w) // 2
        y = (size - new_h) // 2
        canvas.paste(resized, (x, y), resized)

    # Header logo: transparent background, brand green mark
    logo = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
    center_paste(logo, green_mark, pad_frac=0.10)
    logo.save(str(logo_path), 'PNG')

    # Favicon: dark green background with white mark
    favicon = Image.new('RGBA', (512, 512), brand_green)
    center_paste(favicon, white_mark, pad_frac=0.14)
    favicon.save(str(favicon_path), 'PNG')

    # Apple touch icon: same as favicon at 180x180
    apple = Image.new('RGBA', (180, 180), brand_green)
    center_paste(apple, white_mark, pad_frac=0.14)
    apple.save(str(apple_path), 'PNG')

def generate_placeholder_images():
    """Generate all placeholder images."""
    images_to_create = [
        ("home/hero.jpg", "Photo coming soon — Peace Blooming"),
        ("home/before-after-cleaning-01-before.jpg", "Before: Dirty headstone"),
        ("home/before-after-cleaning-01-after.jpg", "After: Cleaned"),
        ("home/before-after-decorating-01-before.jpg", "Before: Bare grave"),
        ("home/before-after-decorating-01-after.jpg", "After: Decorated with flowers"),
        ("services/cleaning-in-progress-01.jpg", "Gentle cleaning in progress"),
        ("services/decorated-grave-01.jpg", "Completed seasonal decoration"),
        ("about/owners.jpg", "Photo of owners coming soon"),
        ("service-area/mt-carmel-cemetery.jpg", "Mt Carmel Cemetery grounds"),
    ]

    for rel_path, text in images_to_create:
        filepath = IMAGES_DIR / rel_path
        # Don't overwrite real photos that have been placed here
        if filepath.exists():
            continue
        create_placeholder_image(str(filepath), text)

    # Generate logo, favicon, and apple-touch-icon from the provided mark
    generate_logo_variants()

# ============================================================================
# HTML TEMPLATES
# ============================================================================

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="icon" type="image/png" href="/images/logo/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/logo/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">
    {schema}
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <header>
        <nav class="navbar" aria-label="Main navigation">
            <div class="nav-container">
                <a href="/" class="logo" aria-label="Peace Blooming home">
                    <img src="/images/logo/logo.png" alt="" class="logo-img">
                    <span>Peace Blooming</span>
                </a>
                <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Toggle menu">
                    <span class="nav-toggle-bar"></span>
                    <span class="nav-toggle-bar"></span>
                    <span class="nav-toggle-bar"></span>
                </button>
                <div id="nav-menu" class="nav-menu">
                    <a href="/">Home</a>
                    <a href="/services-and-pricing.html">Services & Pricing</a>
                    <a href="/how-it-works.html">How It Works</a>
                    <a href="/service-area.html">Service Area</a>
                    <a href="/about.html">About</a>
                    <a href="/faq.html">FAQ</a>
                    <a href="/contact.html">Contact</a>
                </div>
                <a href="tel:[PHONE]" class="nav-cta btn btn-primary">Call [PHONE]</a>
            </div>
        </nav>
    </header>
    
    <main id="main-content">
        {content}
    </main>
    
    <div class="sticky-cta" role="complementary" aria-label="Quick contact">
        <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
        <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
    </div>
    
    <footer>
        <div class="footer-container">
            <div class="footer-section">
                <h3>Peace Blooming</h3>
                <p>Grave Cleaning & Seasonal Flowers<br>Metro Detroit including Downriver</p>
            </div>
            <div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services-and-pricing.html">Services & Pricing</a></li>
                    <li><a href="/how-it-works.html">How It Works</a></li>
                    <li><a href="/service-area.html">Service Area</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Contact</h4>
                <p>
                    Phone/Text: <a href="tel:[PHONE]">[PHONE]</a><br>
                    Email: <a href="mailto:hello@peaceblooming.com">hello@peaceblooming.com</a>
                </p>
            </div>
            <div class="footer-section">
                <p class="copyright">&copy; 2026 Peace Blooming. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="/js/site.js"></script>
</body>
</html>
"""

def wrap_in_template(content, title, description, schema_json=None):
    """Wrap content in the base template. Accepts a single schema dict or a list of schemas."""
    schema_tag = ""
    if schema_json:
        if isinstance(schema_json, list):
            tags = []
            for schema in schema_json:
                tags.append(f'    <script type="application/ld+json">\n{json.dumps(schema, indent=6)}\n    </script>')
            schema_tag = "\n".join(tags)
        else:
            schema_tag = f'    <script type="application/ld+json">\n{json.dumps(schema_json, indent=6)}\n    </script>'

    return BASE_TEMPLATE.format(
        title=title,
        description=description,
        schema=schema_tag,
        content=content
    )

# ============================================================================
# JSON-LD SCHEMA GENERATION
# ============================================================================

def create_local_business_schema():
    """Create the main LocalBusiness schema for homepage."""
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": "https://www.peaceblooming.com/#business",
        "name": "Peace Blooming",
        "telephone": "[PHONE]",
        "email": "hello@peaceblooming.com",
        "priceRange": "$60-$400",
        "description": "Grave cleaning and seasonal flower service for families across Metro Detroit, Downriver, and Metro Ann Arbor.",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Brighton",
            "addressLocality": "Brighton",
            "addressRegion": "MI",
            "addressCountry": "US"
        },
        "areaServed": [
            {"@type": "City", "name": "Wyandotte, MI"},
            {"@type": "City", "name": "Detroit, MI"},
            {"@type": "City", "name": "Ann Arbor, MI"}
        ],
        "url": "https://www.peaceblooming.com"
    }

def create_faq_schema(faqs):
    """Create FAQPage schema from Q&A pairs."""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            }
            for q, a in faqs
        ]
    }

def create_cemetery_schema(cemetery_name, city):
    """Create Cemetery entity schema."""
    return {
        "@context": "https://schema.org",
        "@type": "Cemetery",
        "name": cemetery_name,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": city,
            "addressRegion": "MI",
            "addressCountry": "US"
        }
    }


def create_home_faq_schema():
    """FAQPage schema for the homepage's short FAQ block."""
    faqs = [
        ("Do I need to be there?", "No. Most of our clients live out of state or can't visit often — that's exactly who we built this for."),
        ("How much does it cost?", "A one-time cleaning and decorating visit runs $90–$140 (or $75–$110 at strict cemeteries). Seasonal Care Plans start around $180/year."),
        ("Will you follow my cemetery's rules?", "Yes — we check the specific rules for your cemetery before every visit, so nothing gets removed or confiscated."),
    ]
    return create_faq_schema(faqs)


def create_services_schema():
    """Service schema with an aggregate offer for the Services & Pricing page."""
    business_ref = {"@id": "https://www.peaceblooming.com/#business"}
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Grave cleaning and seasonal decorating",
        "provider": business_ref,
        "areaServed": [
            {"@type": "City", "name": "Wyandotte, MI"},
            {"@type": "City", "name": "Detroit, MI"},
            {"@type": "City", "name": "Ann Arbor, MI"}
        ],
        "offers": {
            "@type": "AggregateOffer",
            "lowPrice": "60",
            "highPrice": "400",
            "priceCurrency": "USD",
            "offers": [
                {"@type": "Offer", "name": "Basic Cleaning Visit", "description": "$60–$90 per visit"},
                {"@type": "Offer", "name": "Cleaning + Seasonal Decoration Visit", "description": "$90–$140 per visit"},
                {"@type": "Offer", "name": "Cemetery-Compliant Light Cleaning", "description": "$75–$110 per visit"},
                {"@type": "Offer", "name": "Seasonal Care Plans", "description": "$180–$400 per year per grave"}
            ]
        }
    }


# ============================================================================
# PAGE GENERATION FUNCTIONS
# ============================================================================

def generate_home_page():
    """Generate home page."""
    content = """<section class="hero">
        <div class="hero-content">
            <p class="tagline">Grave Cleaning & Seasonal Flowers, Metro Detroit including Downriver</p>
            <h1>Caring for your loved one's resting place, the way you would.</h1>
            <p>Grave cleaning and seasonal flowers for families across Metro Detroit, Downriver, and Metro Ann Arbor — including Mt Carmel Cemetery in Wyandotte. You don't have to be there. We'll send you photos every time we are.</p>
            <div class="hero-cta">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
                <a href="/services-and-pricing.html" class="btn btn-secondary">See Pricing</a>
            </div>
        </div>
        <div class="hero-image-wrapper">
            <img src="/images/home/hero.jpg" alt="Well-maintained grave with fresh flowers" class="hero-image" loading="eager">
        </div>
    </section>

    <section class="trust-line">
        <div class="container">
            <p><strong>Insured</strong> • <strong>Photos after every visit</strong> • <strong>We check your cemetery's rules before we touch a thing</strong></p>
        </div>
    </section>

    <section class="story">
        <div class="container story-grid">
            <div class="story-text">
                <h2>Our Story</h2>
                <p>I've been caring for my own parents' grave for years — cleaning the stone, bringing flowers for Easter and Memorial Day, making sure it never looks forgotten. A lot of families want that same care for someone they love, but can't get there themselves — because they moved away, because it's hard to get around anymore, or because life is just full.</p>
                <p>That's why I started Peace Blooming. We treat every grave like it's our own family's.</p>
            </div>
            <div class="story-photo">
                <img src="/images/about/owners.jpg" alt="Peace Blooming owners" loading="lazy">
                <p class="caption">The two people who'll be at your loved one's grave.</p>
            </div>
        </div>
    </section>

    <section class="what-we-do">
        <div class="container">
            <h2>What We Do</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon" aria-hidden="true">
                        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a2 2 0 0 0-2 2c0 1.1.9 2 2 2 2.2 0 4 1.8 4 4v10c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V10c0-2.2 1.8-4 4-4h.1C6 4.7 8.7 2 12 2z"/><path d="M14 22V12c0-2.2 1.8-4 4-4h.1c.1-2.3 2.7-5 6.9-5"/></svg>
                    </div>
                    <h3>Grave Cleaning</h3>
                    <p>Gentle cleaning of the headstone or marker, trimming and clearing around the base. No bleach, no pressure washers — just soft brushes and safe cleaners that won't damage the stone.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon" aria-hidden="true">
                        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7.5a4.5 4.5 0 0 1 4.5-4.5H18v0a4.5 4.5 0 0 1-4.5 4.5H12v0z"/><path d="M12 7.5a4.5 4.5 0 0 0-4.5-4.5H6v0a4.5 4.5 0 0 0 4.5 4.5H12v0z"/><path d="M12 7.5V22"/></svg>
                    </div>
                    <h3>Seasonal Decorating</h3>
                    <p>Fresh or artificial flowers, wreaths, and seasonal touches for Easter, Memorial Day, All Souls Day, and Christmas — always within what your specific cemetery allows.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon" aria-hidden="true">
                        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13" r="3"/><path d="M8 7h8"/></svg>
                    </div>
                    <h3>Photo Proof</h3>
                    <p>After every visit, we send you dated before-and-after photos. You'll see it done, even from a thousand miles away.</p>
                </div>
            </div>
            <p class="centered"><a href="/services-and-pricing.html" class="btn btn-secondary">See Services & Pricing</a></p>
        </div>
    </section>

    <section class="how-it-works-preview">
        <div class="container">
            <h2>How It Works</h2>
            <ol class="steps">
                <li><strong>Tell us the cemetery and the grave.</strong></li>
                <li><strong>We confirm that cemetery's decoration rules before we schedule anything.</strong></li>
                <li><strong>We clean and decorate on the schedule you choose.</strong></li>
                <li><strong>You get photos after every visit.</strong></li>
            </ol>
            <p class="centered"><a href="/how-it-works.html" class="btn btn-secondary">See the full How It Works page</a></p>
        </div>
    </section>

    <section class="service-area-preview">
        <div class="container">
            <h2>Where We Work</h2>
            <p>Serving Metro Detroit, Downriver, and Metro Ann Arbor. Currently caring for graves at Mt Carmel Cemetery in Wyandotte (Our Lady of the Scapular), with more cemeteries added as we grow.</p>
            <p class="centered"><a href="/service-area.html" class="btn btn-secondary">See Service Area</a></p>
        </div>
    </section>

    <section class="pricing-preview">
        <div class="container">
            <h2>Clear, Upfront Pricing</h2>
            <div class="pricing-cards">
                <div class="pricing-card">
                    <span class="price">$60–$90</span>
                    <p>Basic Cleaning Visit</p>
                </div>
                <div class="pricing-card">
                    <span class="price">$90–$140</span>
                    <p>Cleaning + Decorating Visit</p>
                </div>
                <div class="pricing-card featured">
                    <span class="price">$180–$400/year</span>
                    <p>Seasonal Care Plans <em>(most popular)</em></p>
                </div>
            </div>
            <p class="centered"><a href="/services-and-pricing.html" class="btn btn-secondary">See Full Pricing</a></p>
        </div>
    </section>

    <section class="real-work">
        <div class="container">
            <h2>What the Work Looks Like</h2>
            <div class="work-grid">
                <figure class="work-photo">
                    <img src="/images/home/before-after-decorating-01-after.jpg" alt="A grave after seasonal decorating" loading="lazy">
                    <figcaption>Winter decorating after a fresh visit.</figcaption>
                </figure>
                <div class="work-text">
                    <p>Every visit ends with dated photos, so you can see what was done — even if you can't be there yourself.</p>
                    <p><a href="/gallery.html" class="btn btn-secondary">See More Photos</a></p>
                </div>
            </div>
        </div>
    </section>

    <section class="faq-preview">
        <div class="container">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-items">
                <div class="faq-item">
                    <h3>Do I need to be there?</h3>
                    <p>No. Most of our clients live out of state or can't visit often — that's exactly who we built this for.</p>
                </div>
                <div class="faq-item">
                    <h3>How much does it cost?</h3>
                    <p>A one-time cleaning and decorating visit runs $90–$140 (or $75–$110 at strict cemeteries where decorations aren't allowed — our Cemetery-Compliant Light Cleaning tier). Seasonal Care Plans start around $180/year. <a href="/services-and-pricing.html">Full pricing</a></p>
                </div>
                <div class="faq-item">
                    <h3>Will you follow my cemetery's rules?</h3>
                    <p>Yes — we check the specific rules for your cemetery before every visit, so nothing gets removed or confiscated.</p>
                </div>
            </div>
            <p class="centered"><a href="/faq.html" class="btn btn-secondary">See All FAQ</a></p>
        </div>
    </section>

    <section class="closing-cta">
        <div class="container">
            <h2>Booking for a Holiday?</h2>
            <p>Slots fill up — reserve 2–3 weeks before Easter, Memorial Day, All Souls' Day (Nov 1–2), or Christmas.</p>
            <p><strong>Ready to have someone looking after it for you?</strong></p>
            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
            </div>
        </div>
    </section>
    """
    
    schema = [create_local_business_schema(), create_home_faq_schema()]
    return wrap_in_template(content, 
        "Peace Blooming | Grave Cleaning & Seasonal Flowers",
        "Grave cleaning and seasonal flower service for families in Metro Detroit, Downriver, and Ann Arbor.",
        schema)

def generate_services_page():
    """Generate Services & Pricing page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Services & Pricing</h1>
            <p>Clear, upfront pricing — no "contact us for a quote." Here's exactly what things cost.</p>
        </div>
    </section>

    <section class="services-detailed">
        <div class="container">
            <h2>Seasonal Care Plans (Our Most Popular Option — Recommended)</h2>
            <p>Most families who use us choose a plan rather than one-time visits. You set it once, we handle the holidays for you, and it costs about 25% less than paying per visit.</p>
            
            <h3>Why Most Families Choose a Seasonal Care Plan</h3>
            <ul>
                <li>Holiday slots fill up — book ahead and yours is locked in</li>
                <li>Never have to remember to call again (Easter, Memorial Day, All Souls' Day, Christmas — we handle it)</li>
                <li>Regular attention throughout the year keeps the grave looking cared for</li>
                <li>Roughly 25% savings compared to one-time holiday visits</li>
                <li>Easy to scale up or down, pause anytime with no penalty</li>
            </ul>

            <table class="pricing-table">
                <thead>
                    <tr>
                        <th>Plan</th>
                        <th>What's Included</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>3-Visit Seasonal Plan</strong></td>
                        <td>Spring/Memorial Day, Summer/Independence Day, Fall/All Souls or Christmas</td>
                        <td>$180–$250/year per grave</td>
                    </tr>
                    <tr>
                        <td><strong>5-Visit Full-Year Plan</strong></td>
                        <td>Adds Easter and a winter/Christmas visit</td>
                        <td>$280–$400/year per grave</td>
                    </tr>
                    <tr>
                        <td><strong>Multiple graves, same family plot</strong></td>
                        <td>10–15% off</td>
                        <td>—</td>
                    </tr>
                </tbody>
            </table>

            <p><strong>Seasonal availability:</strong> holiday slots are limited — book 2–3 weeks before Easter, Memorial Day, All Souls' Day (Nov 1–2), or Christmas to ensure your visit is scheduled.</p>
        </div>
    </section>

    <section class="one-time-visits">
        <div class="container">
            <h2>One-Time Visits</h2>
            <p>Need just a single visit? These prices apply too — but consider a plan if you find yourself calling back for every holiday.</p>

            <table class="pricing-table">
                <thead>
                    <tr>
                        <th>Service</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Basic Cleaning Visit (cleaning + trimming, single grave)</td>
                        <td>$60–$90</td>
                    </tr>
                    <tr>
                        <td>Cleaning + Seasonal Decoration Visit</td>
                        <td>$90–$140</td>
                    </tr>
                    <tr>
                        <td>Cemetery-Compliant Light Cleaning + Approved Flower Holder Refresh</td>
                        <td>$75–$110</td>
                    </tr>
                    <tr>
                        <td>Additional grave, same cemetery, same visit</td>
                        <td>25% off</td>
                    </tr>
                </tbody>
            </table>

            <h3>About the Cemetery-Compliant Tier</h3>
            <p>At strict-policy cemeteries (Mt Carmel in Wyandotte, Our Lady of Hope in Brownstown, Holy Sepulchre in Southfield), decorations and plantings are closely restricted. This tier provides headstone cleaning + gentle grass trimming + fresh flowers in approved containers only (max 12" tall, max 8" opening, up to 2 per grave) — exactly what these cemeteries allow. No edging, plantings, or prohibited items, so nothing gets removed.</p>
        </div>
    </section>

    <section class="pricing-notes">
        <div class="container">
            <h3>What's Not Included</h3>
            <p>Headstone repair, resetting, leveling, or engraving. If we ever see a stone that looks cracked, leaning, or unstable, we'll stop and let you know so a monument company can take a look — we won't attempt structural work.</p>

            <h3>A Note on Price Ranges</h3>
            <p>The exact price depends on your cemetery, the size of the marker, and what decorations are involved. We'll confirm your exact price before we schedule anything — never a surprise bill.</p>

            <h3>Not Sure Yet?</h3>
            <p>Ask for a free quote and a photo of the grave — no obligation. Call <a href="tel:[PHONE]">[PHONE]</a> or <a href="/contact.html">Request Service Online</a>.</p>

            <div class="cta-buttons">
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
            </div>
        </div>
    </section>

    <section class="real-work">
        <div class="container">
            <h2>Real Seasonal Decorating</h2>
            <figure class="work-photo">
                <img src="/images/services/decorated-grave-01.jpg" alt="A grave decorated with Christmas poinsettias" loading="lazy">
                <figcaption>Christmas decorating at a local cemetery.</figcaption>
            </figure>
            <p class="centered"><a href="/contact.html" class="btn btn-primary">Schedule a Holiday Visit</a></p>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "Services & Pricing | Peace Blooming",
        "Clear, upfront grave cleaning and decorating pricing for Metro Detroit, Downriver, and Ann Arbor.",
        create_services_schema())

def generate_how_it_works_page():
    """Generate How It Works page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>How It Works</h1>
        </div>
    </section>

    <section class="how-it-works-detailed">
        <div class="container">
            <ol class="steps-detailed">
                <li>
                    <h2>Tell Us About the Grave</h2>
                    <p>Cemetery name, section/lot if you know it, and what you'd like done. If you don't know the exact location, that's okay — we can often find it.</p>
                </li>
                <li>
                    <h2>We Check the Cemetery's Rules</h2>
                    <p>Every cemetery has its own policy on what's allowed — container sizes, seasonal windows, what can and can't be left at the grave. We confirm the specific rules for your cemetery before we schedule a single visit, so your flowers or decorations stay in place.</p>
                </li>
                <li>
                    <h2>We Do the Work</h2>
                    <p>Gentle cleaning with soft brushes and safe cleaners — never bleach or pressure washers, which can damage older stone. Decorating is placed exactly where and how your cemetery allows it.</p>
                </li>
                <li>
                    <h2>You Get Photos</h2>
                    <p>Dated before-and-after photos, sent by text or email after every visit. You'll see it's done, even if you're states away.</p>
                </li>
            </ol>

            <h2>A Few Honest Notes</h2>
            <ul>
                <li>We work outdoors, generally March through November — winter weather in Michigan can risk damaging stone and makes travel to some cemeteries impractical. If weather forces a reschedule, we'll let you know and there's no charge for the delay.</li>
                <li>We only take requests from relatives of the person buried, or someone with clear authority to request the work.</li>
                <li>You never need to be present. Most of our clients aren't.</li>
            </ul>

            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
                <a href="/services-and-pricing.html" class="btn btn-secondary">See Pricing</a>
            </div>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "How It Works | Peace Blooming",
        "Step-by-step process for grave cleaning and seasonal flower service.",
        None)

def generate_service_area_index():
    """Generate Service Area index page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Service Area</h1>
            <p>We serve families across Metro Detroit, Downriver, and Metro Ann Arbor.</p>
        </div>
    </section>

    <section class="service-area-overview">
        <div class="container">
            <h2>Our Service Regions</h2>
            <ul class="region-list">
                <li><strong>Wyandotte & Downriver</strong> — Wyandotte, Southgate, Riverview, Trenton, Woodhaven, Taylor, Lincoln Park, and Allen Park.</li>
                <li><strong>Metro Detroit</strong> — Novi, Farmington Hills, Wixom, South Lyon, Milford, Northville, Plymouth, Livonia, Southfield, Royal Oak, Birmingham, Bloomfield Hills, Troy, Dearborn, and the City of Detroit.</li>
                <li><strong>Metro Ann Arbor</strong> — Ann Arbor, Ypsilanti, Dexter, Chelsea, Saline, Whitmore Lake, and Pinckney.</li>
            </ul>
            <p><em>If your city or cemetery isn't listed, reach out anyway — we're happy to check whether we can serve it.</em></p>
        </div>
    </section>

    <section class="cities">
        <div class="container">
            <h2>Service by City / Township</h2>
            <p>We serve families across 20 cities and townships. Start with your city for a list of all cemeteries we serve there:</p>

            <div class="cities-grid">
                <div class="city-section">
                    <h3>Downriver</h3>
                    <ul>
                        <li><a href="/service-area/wyandotte.html">Wyandotte</a> — Mt Carmel Cemetery, Oakwood Cemetery, and church gardens</li>
                        <li><a href="/service-area/brownstown.html">Brownstown</a> — Our Lady of Hope Cemetery</li>
                        <li><a href="/service-area/flat-rock.html">Flat Rock</a> — Michigan Memorial Park</li>
                        <li><a href="/service-area/riverview.html">Riverview</a> — Ferndale Cemetery</li>
                        <li><a href="/service-area/trenton.html">Trenton</a> — Bloomdale Cemetery, Old Burial Ground</li>
                        <li><a href="/service-area/lincoln-park.html">Lincoln Park</a> — Memorial Park</li>
                        <li><a href="/service-area/woodhaven.html">Woodhaven</a> — Oak Ridge Cemetery</li>
                        <li><a href="/service-area/romulus.html">Romulus</a> — Romulus Memorial Cemetery</li>
                        <li><a href="/service-area/taylor.html">Taylor</a> — Taylor Township Cemetery, West Mound Cemetery</li>
                        <li><a href="/service-area/gibraltar.html">Gibraltar</a> — Gibraltar Cemetery</li>
                    </ul>
                </div>

                <div class="city-section">
                    <h3>Brighton & Livingston County</h3>
                    <ul>
                        <li><a href="/service-area/brighton.html">Brighton (City)</a> — Fairview, St. Patrick's Calvary, Old Village, Brighton Hills Memorial Gardens</li>
                        <li><a href="/service-area/brighton-township.html">Brighton Township</a> — Bird, Kensington Baptist, Pleasant Valley, Woodruff Farm</li>
                        <li><a href="/service-area/genoa-township.html">Genoa Township</a> — Chilson, Euler, Kelly, Saint George</li>
                        <li><a href="/service-area/green-oak-township.html">Green Oak Township</a> — Free-Will Baptist, Hayes, Marion Hill, Monahan, Old Kensington, Plains, Whitmore Lakeview</li>
                        <li><a href="/service-area/hamburg-township.html">Hamburg Township</a> — Campbell, Hamburg Village, North Hamburg, Placeway</li>
                    </ul>
                </div>

                <div class="city-section">
                    <h3>Metro Detroit</h3>
                    <ul>
                        <li><a href="/service-area/livonia.html">Livonia</a> — Glen Eden Lutheran Memorial Park and many others</li>
                        <li><a href="/service-area/southfield.html">Southfield</a> — Holy Sepulchre Catholic Cemetery</li>
                        <li><a href="/service-area/troy.html">Troy</a> — White Chapel Memorial Park Cemetery</li>
                        <li><a href="/service-area/dearborn-heights.html">Dearborn Heights</a> — St. Hedwig Cemetery & Mausoleum</li>
                        <li><a href="/service-area/farmington-hills.html">Farmington Hills</a> — East, West, and North Farmington Cemeteries</li>
                    </ul>
                </div>
            </div>

            <p>Don't see your city or cemetery listed? Reach out anyway — if it's in our service area, we're happy to serve it.</p>

            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
            </div>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "Service Area | Peace Blooming",
        "Grave cleaning service in Metro Detroit, Downriver, and Metro Ann Arbor. Find your cemetery.",
        None)

def generate_about_page():
    """Generate About page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>About Peace Blooming</h1>
        </div>
    </section>

    <section class="about-content">
        <div class="container">
            <div class="about-intro">
                <p>Peace Blooming was started by two Downriver-area women who've spent years caring for family graves ourselves — including our own parents'. We know what it feels like to want a grave looked after and not always be able to get there. So we started doing it for other families too.</p>
                <p>We're not a franchise or a call center. When you reach out, you're talking to one of us — the same two people who'll actually be at the cemetery, cleaning the stone and setting out the flowers.</p>
            </div>

            <div class="about-image">
                <img src="/images/about/owners.jpg" alt="Peace Blooming owners" class="about-photo" loading="lazy">
            </div>

            <h2>What You Can Count On</h2>
            <ul class="trust-list">
                <li><strong>Insured</strong> — we carry general liability insurance covering our work in the Metro Detroit area.</li>
                <li><strong>We Follow the Rules</strong> — we confirm each cemetery's specific decoration policy before every visit.</li>
                <li><strong>We Document Everything</strong> — dated photos after every visit, so you always know it was done.</li>
                <li><strong>We Keep It Personal</strong> — a small, two-person business, not a big operation. You'll always know who's caring for your family's grave.</li>
            </ul>

            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
            </div>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "About | Peace Blooming",
        "Learn about Peace Blooming's small, personal grave cleaning service in Michigan.",
        None)

def generate_faq_page():
    """Generate FAQ page."""
    faqs = [
        ("Do I need to be there when you visit?", "No. Most of our clients live out of state, can't drive anymore, or just don't have the time — that's the whole reason this business exists. You'll get photos after every visit so you can see it's done."),
        ("How much does it cost?", "One-time visits: Basic Cleaning runs $60–$90, Cleaning + Decorating runs $90–$140, Cemetery-Compliant Light Cleaning (for strict-policy cemeteries like Mt Carmel, Our Lady of Hope, Holy Sepulchre) runs $75–$110. Seasonal Care Plans start around $180–$250/year (3-visit plan) up to $280–$400/year (5-visit full-year plan). See the full Services & Pricing page for all details — we'll always confirm your exact price before scheduling."),
        ("Are you insured?", "Yes, we carry general liability insurance covering our work in the Metro Detroit area."),
        ("Will my flowers/decorations be allowed?", "Every cemetery has its own rules on containers, seasonal windows, and what's permanently allowed. We check your specific cemetery's policy before every visit, so what we place is allowed to stay."),
        ("What's NOT included?", "Headstone repair, resetting, leveling, or engraving. If we notice a stone that looks damaged or unstable, we'll stop and let you know so you can contact a monument company."),
        ("What if it's raining or there's snow on the ground?", "We generally work March through November. Michigan winters can make travel and stonework impractical, and freezing conditions can risk damaging stone. If we need to reschedule for weather, we'll tell you and there's no charge for the delay."),
        ("Who can request service for a grave?", "We only take requests from a relative of the person buried, or someone with clear authority to request the work on the family's behalf."),
        ("How do I know the work happened?", "We send dated before-and-after photos by text or email after every single visit — no exceptions."),
        ("Can you cancel or reschedule my plan?", "Yes, anytime — just let us know. If a visit can't happen because of a cemetery restriction or access issue on our end, we'll reschedule it or refund that visit, your choice."),
    ]
    
    content = """<section class="page-hero">
        <div class="container">
            <h1>Frequently Asked Questions</h1>
        </div>
    </section>

    <section class="faq-full">
        <div class="container">
    """
    
    for question, answer in faqs:
        content += f"""
            <div class="faq-item">
                <h3>{question}</h3>
                <p>{answer}</p>
            </div>
        """
    
    content += """
            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
            </div>
        </div>
    </section>
    """
    
    schema = create_faq_schema(faqs)
    return wrap_in_template(content,
        "FAQ | Peace Blooming",
        "Frequently asked questions about grave cleaning and decoration services.",
        schema)

def generate_contact_success_page():
    """Generate Contact Success page shown after Netlify form submission."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Thank You</h1>
            <p>Your service request has been sent. We’ll be in touch soon.</p>
        </div>
    </section>

    <section class="contact-content">
        <div class="container">
            <div class="contact-form-section">
                <div class="form-success" style="display:block">
                    <h3>Your request was received.</h3>
                    <p>We’ll review the details and get back to you within 24–48 hours. If you don’t hear from us, please call or email directly.</p>
                    <p><a href="/" class="btn btn-secondary">Back to Home</a></p>
                </div>

                <h2>Or Reach Us Directly</h2>

                <h3>Our Response Promise</h3>
                <p><strong>We respond within 24–48 hours.</strong> After we confirm pricing and your cemetery's rules, we'll send you a service agreement to review and sign before we schedule anything.</p>

                <h3>Our Guarantee</h3>
                <p>We check every cemetery's decoration rules before we visit. If anything we place doesn't follow those rules, we'll replace or fix it at no extra charge.</p>
            </div>

            <div class="contact-info-section">
                <h2>Contact Information</h2>
                <p><strong>Phone:</strong> <a href="tel:[PHONE]">[PHONE]</a></p>
                <p><strong>Email:</strong> <a href="mailto:hello@peaceblooming.com">hello@peaceblooming.com</a></p>
                <p><strong>Service Area:</strong> Metro Detroit including Downriver and Metro Ann Arbor</p>
            </div>
        </div>
    </section>
    """

    return wrap_in_template(
        content,
        "Thank You | Peace Blooming",
        "Your service request has been sent to Peace Blooming.",
        None
    )


def generate_contact_page():
    """Generate Contact page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Contact Us</h1>
            <p>Tell us a little about the grave and what you'd like done, and we'll follow up with pricing and next steps.</p>
        </div>
    </section>

    <section class="contact-content">
        <div class="container">
            <div class="contact-form-section">
                <h2>Request Service</h2>
                <div class="form-success" id="form-success" hidden>
                    <h3>Thank you — your request was sent.</h3>
                    <p>We’ll review the details and get back to you within 24–48 hours. If you don’t hear from us, please call or email directly.</p>
                    <p><a href="/" class="btn btn-secondary">Back to Home</a></p>
                </div>

                <form name="service-request" id="service-request" method="POST" action="/contact-success.html" netlify netlify-honeypot="honeypot" class="contact-form">
                    <input type="hidden" name="form-name" value="service-request">
                    <input type="hidden" name="subject" value="New Peace Blooming service request">
                    <div class="form-group" hidden>
                        <label for="honeypot">Don’t fill this out if you’re human:</label>
                        <input type="text" id="honeypot" name="honeypot" tabindex="-1">
                    </div>

                    <div class="form-group">
                        <label for="name">Your Name</label>
                        <input type="text" id="name" name="name" required>
                    </div>

                    <div class="form-group">
                        <label for="contact">Phone or Email (how should we reach you?)</label>
                        <input type="text" id="contact" name="contact" required>
                    </div>

                    <div class="form-group">
                        <label for="cemetery">Cemetery Name</label>
                        <input type="text" id="cemetery" name="cemetery" required>
                    </div>

                    <div class="form-group">
                        <label for="section-lot">Section/Lot Number (if known — okay to leave blank)</label>
                        <input type="text" id="section-lot" name="section-lot">
                    </div>

                    <div class="form-group">
                        <label for="relationship">Your Relationship to the Person Buried</label>
                        <input type="text" id="relationship" name="relationship" required>
                    </div>

                    <div class="form-group">
                        <label for="service-type">What Would You Like Done?</label>
                        <select id="service-type" name="service-type" required>
                            <option value="">Choose one…</option>
                            <option value="cleaning">Cleaning</option>
                            <option value="decorating">Seasonal Decorating</option>
                            <option value="plan">Seasonal Care Plan</option>
                            <option value="not-sure">Not Sure Yet</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="heard-about">How Did You Hear About Us?</label>
                        <select id="heard-about" name="heard-about" required>
                            <option value="">Choose one…</option>
                            <option value="church-bulletin">Church Bulletin</option>
                            <option value="google">Google Search</option>
                            <option value="referral">Referral from Friend or Family</option>
                            <option value="facebook">Facebook</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="message">Anything Else We Should Know?</label>
                        <textarea id="message" name="message" rows="4"></textarea>
                    </div>

                    <button type="submit" class="btn btn-primary">Request Service</button>
                </form>
            </div>

            <div class="contact-info-section">
                <h2>Or Reach Us Directly</h2>
                
                <h3>Our Response Promise</h3>
                <p><strong>We respond within 24–48 hours.</strong> After we confirm pricing and your cemetery's rules, we'll send you a service agreement to review and sign before we schedule anything.</p>

                <h3>Our Guarantee</h3>
                <p>If a visit can't be completed due to cemetery restrictions, access issues, or weather, we'll reschedule it or refund that visit — your choice. No questions asked.</p>

                <h3>Contact Information</h3>
                <p>
                    <strong>Phone/Text:</strong> <a href="tel:[PHONE]">[PHONE]</a><br>
                    <strong>Email:</strong> <a href="mailto:hello@peaceblooming.com">hello@peaceblooming.com</a>
                </p>
            </div>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "Contact | Peace Blooming",
        "Contact Peace Blooming to request grave cleaning or seasonal decorating service.",
        None)

def generate_form_blueprint():
    """Generate a hidden static HTML form blueprint for Netlify Forms detection.

    Netlify parses static HTML files at build time to detect forms. A plain
    HTML blueprint ensures the form is registered even if the visible form is
    generated from a template string.
    """
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Blueprint</title>
</head>
<body>
    <!-- Hidden blueprint for Netlify Forms detection. Not linked from the site. -->
    <form name="service-request" method="POST" data-netlify="true" netlify-honeypot="honeypot">
        <input type="hidden" name="form-name" value="service-request">
        <input type="hidden" name="subject" value="New Peace Blooming service request">
        <input type="text" id="honeypot" name="honeypot" tabindex="-1">
        <input type="text" name="name" required>
        <input type="text" name="contact" required>
        <input type="text" name="cemetery" required>
        <input type="text" name="section-lot">
        <input type="text" name="relationship" required>
        <select name="service-type" required>
            <option value="">Choose one…</option>
            <option value="cleaning">Cleaning</option>
            <option value="decorating">Seasonal Decorating</option>
            <option value="plan">Seasonal Care Plan</option>
            <option value="not-sure">Not Sure Yet</option>
        </select>
        <select name="heard-about" required>
            <option value="">Choose one…</option>
            <option value="church-bulletin">Church Bulletin</option>
            <option value="google">Google Search</option>
            <option value="referral">Referral from Friend or Family</option>
            <option value="facebook">Facebook</option>
            <option value="other">Other</option>
        </select>
        <textarea name="message" rows="4"></textarea>
    </form>
</body>
</html>
"""


def generate_blog_page():
    """Generate blog placeholder page."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Blog</h1>
            <p>Tips, seasonal guides, and cemetery care stories.</p>
        </div>
    </section>

    <section class="coming-soon">
        <div class="container">
            <div class="coming-soon-box">
                <h2>Coming Soon</h2>
                <p>We're preparing articles on headstone care, cemetery traditions, seasonal flower guides, and family grave care stories. Check back soon for the first posts.</p>
            </div>
        </div>
    </section>
    """
    
    return wrap_in_template(content,
        "Blog | Peace Blooming",
        "Coming soon: articles on grave care, headstone cleaning, and cemetery traditions.",
        None)

def generate_gallery_page():
    """Generate gallery page with available real work photos."""
    content = """<section class="page-hero">
        <div class="container">
            <h1>Gallery</h1>
            <p>Before-and-after photos from our work across Michigan cemeteries.</p>
        </div>
    </section>

    <section class="gallery">
        <div class="container">
            <div class="gallery-grid">
                <figure class="gallery-item">
                    <img src="/images/home/hero.jpg" alt="A well-maintained grave with fresh spring flowers" loading="lazy">
                    <figcaption>Spring visit — fresh flowers and a clean stone.</figcaption>
                </figure>
                <figure class="gallery-item">
                    <img src="/images/home/before-after-decorating-01-after.jpg" alt="A grave decorated with a winter arrangement" loading="lazy">
                    <figcaption>Winter decorating after a fresh visit.</figcaption>
                </figure>
                <figure class="gallery-item">
                    <img src="/images/services/decorated-grave-01.jpg" alt="A grave decorated with Christmas poinsettias" loading="lazy">
                    <figcaption>Christmas decorating at a local cemetery.</figcaption>
                </figure>
            </div>
            <p>More before-and-after photos are added as we complete visits. When you hire Peace Blooming, you receive dated photos of your loved one's grave after every visit.</p>
            <p class="centered"><a href="/contact.html" class="btn btn-primary">Request Service</a></p>
        </div>
    </section>
    """

    return wrap_in_template(content,
        "Gallery | Peace Blooming",
        "Before-and-after photos of grave cleaning and seasonal decorating in Michigan.",
        None)

def generate_cemetery_page(cemetery_slug, cemetery_name, city):
    """Generate a dedicated cemetery page."""
    section_marker = f"## Service Area — {cemetery_name}"
    start = website_copy.find(section_marker)
    page_url = f"https://www.peaceblooming.com/service-area/{cemetery_slug}.html"

    if start == -1:
        # Fallback generic cemetery page
        body_html = """<p>Yes — we clean and decorate graves at {cemetery_name} in {city}, MI, following the cemetery's official decoration policy.</p>
            <h2>Service Details</h2>
            <p>We'll confirm the specific decoration policy with the cemetery before every visit, so your flowers or decorations stay in place.</p>
            <h3>Our Methods</h3>
            <p>Soft brushes and pH-neutral, stone-safe cleaners only — never bleach or pressure washers, which can damage stone.</p>""".format(cemetery_name=cemetery_name, city=city)
    else:
        end = website_copy.find("\n## ", start + 1)
        if end == -1:
            end = len(website_copy)
        cemetery_text = website_copy[start:end].strip()
        # Remove the heading line since the template provides the page h1
        cemetery_text = cemetery_text.split('\n', 1)[1] if '\n' in cemetery_text else cemetery_text

        # Strip trailing horizontal rule and the generic CTA line (template adds buttons below)
        lines = cemetery_text.splitlines()
        while lines and (lines[-1].strip() == "" or lines[-1].strip().startswith("Call [PHONE]") or lines[-1].strip() == "---"):
            lines.pop()
        cemetery_text = "\n".join(lines)

        body_html = markdown_to_html(cemetery_text)

    # Cemetery photo: if a real image exists at service-area/{slug}.jpg, use it
    photo_path = IMAGES_DIR / "service-area" / f"{cemetery_slug}.jpg"
    photo_html = f'''<figure class="cemetery-photo">
                <img src="/images/service-area/{cemetery_slug}.jpg" alt="{cemetery_name} grounds" loading="lazy">
            </figure>''' if photo_path.exists() else ""

    content = f"""<section class="page-hero">
        <div class="container">
            <h1>Grave Cleaning & Decorating at {cemetery_name}</h1>
        </div>
    </section>

    <section class="cemetery-content">
        <div class="container">
            {body_html}

            {photo_html}

            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
                <a href="/services-and-pricing.html" class="btn btn-secondary">See Pricing</a>
            </div>
        </div>
    </section>
    """

    business_ref = {"@id": "https://www.peaceblooming.com/#business"}
    cemetery_schema = create_cemetery_schema(cemetery_name, city)
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Grave cleaning and seasonal decorating",
        "provider": business_ref,
        "areaServed": [
            {"@type": "City", "name": f"{city}, MI"},
            {"@type": "Cemetery", "name": cemetery_name}
        ],
        "url": page_url
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.peaceblooming.com/"},
            {"@type": "ListItem", "position": 2, "name": "Service Area", "item": "https://www.peaceblooming.com/service-area.html"},
            {"@type": "ListItem", "position": 3, "name": cemetery_name, "item": page_url}
        ]
    }

    return wrap_in_template(
        content,
        f"{cemetery_name} | Peace Blooming",
        f"Grave cleaning and seasonal decorating at {cemetery_name} in {city}, MI.",
        [business_ref, cemetery_schema, service_schema, breadcrumb_schema]
    )

def generate_city_page(city_slug, city_name, region):
    """Generate a city/township service area page."""
    section_marker = f"### {city_name}"
    start = website_copy.find(section_marker)
    page_url = f"https://www.peaceblooming.com/service-area/{city_slug}.html"

    if start == -1:
        # Fallback generic city page
        body_html = f"""<p>Yes — we provide grave cleaning and seasonal decorating for cemeteries in {city_name}, a community in {region} Michigan.</p>
            <h2>Cemeteries in {city_name}</h2>
            <p>We serve several cemeteries in {city_name}. Call us to confirm availability at your specific cemetery.</p>"""
    else:
        end = website_copy.find("\n### ", start + 1)
        if end == -1:
            end = website_copy.find("\n## ", start + 1)
        if end == -1:
            end = len(website_copy)
        city_text = website_copy[start:end].strip()
        # Remove the heading line since the template provides the page h1
        city_text = city_text.split('\n', 1)[1] if '\n' in city_text else city_text

        # Strip trailing horizontal rule and generic CTA line (template adds buttons below)
        lines = city_text.splitlines()
        while lines and (lines[-1].strip() == "" or lines[-1].strip().startswith("Call [PHONE]") or lines[-1].strip() == "---"):
            lines.pop()
        city_text = "\n".join(lines)

        body_html = markdown_to_html(city_text)

    content = f"""<section class="page-hero">
        <div class="container">
            <h1>Grave Cleaning & Decorating in {city_name}, MI</h1>
        </div>
    </section>

    <section class="city-content">
        <div class="container">
            {body_html}

            <div class="cta-buttons">
                <a href="tel:[PHONE]" class="btn btn-primary">Call [PHONE]</a>
                <a href="/contact.html" class="btn btn-secondary">Request Service Online</a>
                <a href="/services-and-pricing.html" class="btn btn-secondary">See Pricing</a>
            </div>
        </div>
    </section>
    """

    business_ref = {"@id": "https://www.peaceblooming.com/#business"}
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Grave cleaning and seasonal decorating",
        "provider": business_ref,
        "areaServed": {"@type": "City", "name": f"{city_name}, MI"},
        "url": page_url
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.peaceblooming.com/"},
            {"@type": "ListItem", "position": 2, "name": "Service Area", "item": "https://www.peaceblooming.com/service-area.html"},
            {"@type": "ListItem", "position": 3, "name": f"{city_name}, MI", "item": page_url}
        ]
    }

    return wrap_in_template(
        content,
        f"{city_name}, MI | Peace Blooming",
        f"Grave cleaning and seasonal decorating service in {city_name}, MI.",
        [business_ref, service_schema, breadcrumb_schema]
    )

# ============================================================================
# GENERATE ALL PAGES
# ============================================================================

def main():
    """Main build function."""
    print("Generating Peace Blooming website...")
    
    # Create placeholder images
    print("  → Creating placeholder images...")
    generate_placeholder_images()
    
    # Generate core pages
    print("  → Generating core pages...")
    pages = {
        "index.html": generate_home_page(),
        "services-and-pricing.html": generate_services_page(),
        "how-it-works.html": generate_how_it_works_page(),
        "service-area.html": generate_service_area_index(),
        "about.html": generate_about_page(),
        "faq.html": generate_faq_page(),
        "contact.html": generate_contact_page(),
        "contact-success.html": generate_contact_success_page(),
        "blog.html": generate_blog_page(),
        "gallery.html": generate_gallery_page(),
    }
    
    for filename, html in pages.items():
        filepath = SITE_ROOT / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    # Write Netlify form blueprint (static, not linked)
    blueprint_path = SITE_ROOT / "form-blueprint.html"
    with open(blueprint_path, 'w', encoding='utf-8') as f:
        f.write(generate_form_blueprint())
    
    # Generate cemetery pages
    print("  → Generating cemetery pages...")
    for slug, name, city in CEMETERIES:
        html = generate_cemetery_page(slug, name, city)
        filepath = SERVICE_AREA_DIR / f"{slug}.html"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    
    # Generate city pages
    print("  → Generating city pages...")
    for slug, city_name, region in CITIES:
        html = generate_city_page(slug, city_name, region)
        filepath = SERVICE_AREA_DIR / f"{slug}.html"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    
    # Generate CSS
    print("  → Generating CSS...")
    css_content = """/* Peace Blooming — Main Stylesheet */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --green-dark: #2c3e32;
    --cream: #f6f4ed;
    --gold: #c9a86c;
    --sage-soft: #dce8e0;
    --text: #3d3d3d;
    --muted: #6b6b6b;
    --white: #ffffff;
    --border: #e8e4d9;

    --font-serif: 'Fraunces', Georgia, 'Times New Roman', serif;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

html {
    scroll-behavior: smooth;
}

.skip-link {
    position: absolute;
    top: -100%;
    left: 1.5rem;
    z-index: 200;
    background-color: var(--green-dark);
    color: var(--white);
    padding: 0.75rem 1.25rem;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: top 0.2s ease;
}

.skip-link:focus {
    top: 1rem;
}

body {
    font-family: var(--font-sans);
    color: var(--text);
    background-color: var(--cream);
    line-height: 1.7;
    font-size: 16px;
}

/* Header & Navigation */
header {
    background-color: var(--white);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

.navbar {
    padding: 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.875rem 1.5rem;
    gap: 1rem;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    text-decoration: none;
    color: var(--green-dark);
    font-size: 1.35rem;
    font-weight: 600;
    font-family: var(--font-serif);
    letter-spacing: -0.01em;
    flex-shrink: 0;
}

.logo-img {
    height: 36px;
    width: auto;
}

.nav-toggle {
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 44px;
    height: 44px;
    gap: 5px;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 8px;
    cursor: pointer;
}

.nav-toggle-bar {
    display: block;
    width: 22px;
    height: 2px;
    background-color: var(--green-dark);
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.nav-menu {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    list-style: none;
}

.nav-menu a {
    text-decoration: none;
    color: var(--text);
    font-weight: 500;
    font-size: 0.92rem;
    transition: color 0.2s ease;
    padding: 0.5rem 0;
}

.nav-menu a:hover {
    color: var(--green-dark);
}

.nav-cta {
    flex-shrink: 0;
    padding: 0.6rem 1.1rem;
    font-size: 0.92rem;
    min-height: 40px;
}

/* Sticky bottom CTA */
.sticky-cta {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    align-items: center;
    padding: 0.75rem 1rem;
    background-color: var(--white);
    border-top: 1px solid var(--border);
    box-shadow: 0 -2px 10px rgba(0,0,0,0.08);
    z-index: 99;
    transition: transform 0.3s ease;
}

.sticky-cta .btn {
    flex: 1;
    max-width: 220px;
    min-height: 48px;
    font-size: 0.95rem;
    padding: 0.75rem 1rem;
}

.sticky-cta.is-hidden {
    transform: translateY(110%);
}

/* Main Content */
main {
    min-height: 70vh;
    padding: 0;
}

section {
    padding: 3.5rem 2rem;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-serif);
    color: var(--green-dark);
    margin: 1.5rem 0 1rem 0;
    line-height: 1.25;
    font-weight: 600;
    letter-spacing: -0.01em;
}

h1 {
    font-size: 2.25rem;
    margin-top: 0;
}

h2 {
    font-size: 1.75rem;
    border-bottom: 2px solid var(--border);
    padding-bottom: 0.5rem;
}

h3 {
    font-size: 1.25rem;
}

p {
    margin: 0.75rem 0;
    line-height: 1.7;
    color: var(--text);
}

a {
    color: var(--green-dark);
    text-decoration: underline;
    text-underline-offset: 0.15em;
    transition: color 0.2s ease;
}

a:hover {
    color: #1d2a20;
}

a:focus-visible {
    outline: 2px solid var(--gold);
    outline-offset: 2px;
}

/* Hero Section */
.hero {
    background: var(--cream);
    padding: 4rem 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5rem;
    align-items: center;
}

.hero-content h1 {
    font-size: 2.5rem;
    margin-top: 0;
    color: var(--green-dark);
}

.hero-content p {
    font-size: 1.1rem;
    margin: 1.5rem 0;
    line-height: 1.8;
    color: var(--text);
}

.hero-image {
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(44, 62, 50, 0.12);
    display: block;
}

.hero-image-wrapper {
    background-color: var(--sage-soft);
    border-radius: 12px;
    padding: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 280px;
}

.hero-cta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 2rem;
}

.hero .tagline {
    display: inline-block;
    font-family: var(--font-sans);
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.75rem;
}

/* Page Hero (secondary pages) */
.page-hero {
    background: var(--green-dark);
    color: var(--white);
    padding: 4rem 2rem;
    text-align: center;
}

.page-hero h1 {
    color: var(--white);
    margin-bottom: 1rem;
    border: none;
}

.page-hero p {
    color: rgba(255,255,255,0.9);
    font-size: 1.1rem;
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.875rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease;
    border: 2px solid transparent;
    cursor: pointer;
    font-size: 1rem;
    font-family: var(--font-sans);
    line-height: 1.2;
    min-height: 48px;
}

.btn:focus-visible {
    outline: 3px solid var(--gold);
    outline-offset: 2px;
}

.btn-primary {
    background-color: var(--green-dark);
    color: var(--white);
    border-color: var(--green-dark);
}

.btn-primary:hover {
    background-color: #1d2a20;
    border-color: #1d2a20;
    color: var(--white);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(44, 62, 50, 0.2);
}

.btn-secondary {
    background-color: var(--white);
    color: var(--green-dark);
    border: 2px solid var(--green-dark);
}

.btn-secondary:hover {
    background-color: var(--green-dark);
    color: var(--white);
}

.btn-accent {
    background-color: var(--gold);
    color: var(--green-dark);
    border-color: var(--gold);
}

.btn-accent:hover {
    background-color: #b89a5e;
    border-color: #b89a5e;
    color: var(--green-dark);
}

.cta-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin: 2rem 0;
}

/* Trust Line */
.trust-line {
    background-color: var(--sage-soft);
    padding: 1.5rem 2rem;
    text-align: center;
    font-size: 1.05rem;
    font-weight: 500;
    color: var(--green-dark);
}

.trust-line strong {
    color: var(--green-dark);
    font-weight: 600;
}

/* Story Section */
.story {
    background-color: var(--white);
}

.story-grid {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 3rem;
    align-items: center;
}

.story-text p {
    font-size: 1.1rem;
    line-height: 1.9;
}

.story-photo img {
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(44, 62, 50, 0.12);
    display: block;
}

.story-photo .caption {
    font-size: 0.875rem;
    color: var(--muted);
    margin-top: 0.75rem;
    font-style: italic;
}

/* Services Grid */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.service-card {
    background-color: var(--white);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.service-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(44, 62, 50, 0.1);
}

.service-card h3 {
    color: var(--green-dark);
    margin-top: 0;
}

.service-icon {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--sage-soft);
    border-radius: 12px;
    color: var(--green-dark);
    margin-bottom: 1rem;
}

.service-icon svg {
    width: 28px;
    height: 28px;
}

/* Steps */
.steps, .steps-detailed {
    list-style: none;
    counter-reset: step-counter;
}

.steps li, .steps-detailed li {
    counter-increment: step-counter;
    margin: 1.5rem 0;
    padding-left: 3rem;
    position: relative;
}

.steps li:before, .steps-detailed li:before {
    content: counter(step-counter);
    position: absolute;
    left: 0;
    top: -2px;
    background-color: var(--green-dark);
    color: var(--white);
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-family: var(--font-sans);
}

.steps-detailed li h2 {
    margin-top: 0;
    border: none;
    padding: 0;
}

/* Tables */
.pricing-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: var(--white);
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    border-radius: 8px;
    overflow: hidden;
}

.pricing-table th, .pricing-table td {
    padding: 1.25rem;
    text-align: left;
    border-bottom: 1px solid var(--border);
}

.pricing-table th {
    background-color: var(--green-dark);
    color: var(--white);
    font-weight: 600;
    font-family: var(--font-sans);
}

.pricing-table tr:hover {
    background-color: var(--cream);
}

/* Pricing Preview */
.pricing-preview {
    background-color: var(--sage-soft);
}

.pricing-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.pricing-card {
    background-color: var(--white);
    border-radius: 12px;
    padding: 1.75rem;
    text-align: center;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.pricing-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(44, 62, 50, 0.1);
}

.pricing-card .price {
    display: block;
    font-family: var(--font-serif);
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--green-dark);
    margin-bottom: 0.5rem;
}

.pricing-card p {
    color: var(--muted);
    font-size: 0.95rem;
    margin: 0;
}

.pricing-card.featured {
    border-color: var(--gold);
    box-shadow: 0 4px 16px rgba(44, 62, 50, 0.08);
}

.pricing-card.featured .price {
    color: var(--green-dark);
}

.pricing-card em {
    color: var(--gold);
    font-weight: 600;
    font-style: normal;
}

/* FAQ */
.faq-item {
    background-color: var(--white);
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 8px;
    border-left: 4px solid var(--green-dark);
    box-shadow: 0 2px 4px rgba(44, 62, 50, 0.05);
    transition: box-shadow 0.2s ease;
}

.faq-item:hover {
    box-shadow: 0 6px 12px rgba(44, 62, 50, 0.08);
}

.faq-item h3 {
    margin-top: 0;
    color: var(--green-dark);
}

.faq-items {
    display: grid;
    gap: 1.5rem;
}

/* Contact Form */
.contact-form {
    background-color: var(--white);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    border: 1px solid var(--border);
}

.form-success {
    background-color: var(--sage-soft);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 2rem;
    text-align: center;
}

.form-success h3 {
    color: var(--green-dark);
    margin-bottom: 0.75rem;
}

.form-success:not([hidden]) + .contact-form {
    display: none;
}

.form-group {
    margin: 1.5rem 0;
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--green-dark);
    font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--border);
    border-radius: 8px;
    font-family: var(--font-sans);
    font-size: 1rem;
    color: var(--text);
    background-color: var(--white);
    min-height: 44px;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus,
.form-group input:focus-visible,
.form-group select:focus-visible,
.form-group textarea:focus-visible {
    outline: none;
    border-color: var(--green-dark);
    box-shadow: 0 0 0 3px rgba(44, 62, 50, 0.1);
}

.form-group input:focus-visible,
.form-group select:focus-visible,
.form-group textarea:focus-visible {
    outline: 3px solid var(--gold);
    outline-offset: 2px;
    box-shadow: none;
}

/* Cities Grid */
.cities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.city-section {
    background-color: var(--white);
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    border: 1px solid var(--border);
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.city-section:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(44, 62, 50, 0.1);
}

.city-section h3 {
    color: var(--green-dark);
    margin-top: 0;
}

.city-section ul {
    list-style: none;
}

.city-section li {
    margin: 0.5rem 0;
    padding-left: 1rem;
}

.city-section li:before {
    content: "→ ";
    color: var(--green-dark);
    margin-right: 0.5rem;
}

.region-list {
    list-style: none;
}

.region-list li {
    margin: 1rem 0;
    padding-left: 2rem;
}

.region-list li:before {
    content: "✓";
    color: var(--green-dark);
    font-weight: bold;
    margin-left: -1.5rem;
    margin-right: 1rem;
}

/* About Page */
.about-intro {
    font-size: 1.1rem;
    line-height: 1.9;
    margin: 2rem 0;
    max-width: 800px;
}

.about-photo {
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(44, 62, 50, 0.12);
    margin: 2rem 0;
    display: block;
}

/* Cemetery page photo */
.cemetery-photo {
    margin: 2rem 0;
}

.cemetery-photo img {
    width: 100%;
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(44, 62, 50, 0.12);
    display: block;
}

/* Real work section on homepage and services */
.real-work {
    padding: 4rem 0;
    background-color: var(--sage-soft);
}

.real-work h2 {
    text-align: center;
    margin-bottom: 2rem;
}

.work-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
}

.work-photo img {
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(44, 62, 50, 0.12);
}

.work-photo figcaption {
    font-size: 0.9rem;
    color: var(--text-light);
    margin-top: 0.5rem;
    text-align: center;
}

.work-text {
    font-size: 1.125rem;
}

/* Gallery page */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.gallery-item {
    margin: 0;
    background-color: var(--cream);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(44, 62, 50, 0.08);
}

.gallery-item img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}

.gallery-item figcaption {
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
    color: var(--text-light);
    text-align: center;
}

.trust-list {
    list-style: none;
    margin: 1.5rem 0;
}

.trust-list li {
    padding: 1rem;
    margin: 0.5rem 0;
    background-color: var(--white);
    border-radius: 8px;
    border-left: 4px solid var(--green-dark);
    box-shadow: 0 2px 4px rgba(44, 62, 50, 0.05);
    transition: box-shadow 0.2s ease;
}

.trust-list li:hover {
    box-shadow: 0 6px 12px rgba(44, 62, 50, 0.08);
}

.trust-list strong {
    color: var(--green-dark);
}

/* Coming Soon */
.coming-soon {
    text-align: center;
    padding: 4rem 2rem;
}

.coming-soon-box {
    background-color: var(--white);
    padding: 3rem;
    border-radius: 12px;
    max-width: 600px;
    margin: 0 auto;
    box-shadow: 0 2px 8px rgba(44, 62, 50, 0.05);
    border: 1px solid var(--border);
}

.coming-soon-box h2 {
    color: var(--green-dark);
    border: none;
}

/* Centered text */
.centered {
    text-align: center;
}

/* Footer */
footer {
    background-color: var(--green-dark);
    color: var(--white);
    padding: 3rem 2rem;
    margin-top: 4rem;
}

.footer-container {
    max-width: 1000px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}

.footer-section h3, .footer-section h4 {
    color: var(--gold);
    border: none;
    margin-top: 0;
    font-family: var(--font-serif);
}

.footer-section a {
    color: var(--cream);
    text-decoration: none;
}

.footer-section a:hover {
    color: var(--gold);
    text-decoration: underline;
}

.footer-section p, .footer-section li {
    color: rgba(255,255,255,0.9);
}

.footer-section ul {
    list-style: none;
}

.footer-section li {
    margin: 0.5rem 0;
}

.copyright {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid rgba(246, 244, 237, 0.2);
    margin-top: 2rem;
    font-size: 0.9rem;
    color: rgba(255,255,255,0.75);
}

/* Mobile Responsive */
@media (max-width: 768px) {
    body {
        padding-bottom: 72px; /* space for sticky CTA */
    }

    .nav-toggle {
        display: flex;
        order: 2;
    }

    .nav-cta {
        order: 3;
        padding: 0.5rem 0.85rem;
        font-size: 0.85rem;
    }

    .nav-menu {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        flex-direction: column;
        align-items: flex-start;
        gap: 0;
        background-color: var(--white);
        border-bottom: 1px solid var(--border);
        padding: 0.5rem 1.5rem 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.06);
    }

    .nav-menu.is-open {
        display: flex;
    }

    .nav-menu a {
        display: block;
        width: 100%;
        padding: 0.75rem 0;
        border-bottom: 1px solid var(--border);
        font-size: 1rem;
    }

    .nav-menu a:last-child {
        border-bottom: none;
    }

    h1 {
        font-size: 1.75rem;
    }

    h2 {
        font-size: 1.5rem;
    }

    h3 {
        font-size: 1.15rem;
    }

    .hero {
        grid-template-columns: 1fr;
        padding: 2.5rem 1.5rem;
        gap: 2rem;
    }

    .hero-content {
        order: 1;
    }

    .hero-image {
        order: 2;
    }

    .work-grid {
        grid-template-columns: 1fr;
    }

    .hero-content h1 {
        font-size: 1.75rem;
    }

    .hero-content p {
        font-size: 1rem;
    }

    .page-hero {
        padding: 2.5rem 1.5rem;
    }

    .page-hero h1 {
        font-size: 1.75rem;
    }

    section {
        padding: 2.5rem 1.5rem;
    }

    .services-grid {
        grid-template-columns: 1fr;
    }

    .story-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .story-photo {
        order: -1;
    }

    .pricing-cards {
        grid-template-columns: 1fr;
    }

    .pricing-table {
        font-size: 0.9rem;
    }

    .pricing-table th, .pricing-table td {
        padding: 0.75rem;
    }

    .cities-grid {
        grid-template-columns: 1fr;
    }

    .cta-buttons {
        flex-direction: column;
    }

    .cta-buttons .btn {
        width: 100%;
        text-align: center;
    }

    .sticky-cta .btn {
        max-width: none;
        font-size: 0.9rem;
    }

    .footer-container {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 1.5rem;
    }

    h2 {
        font-size: 1.25rem;
    }

    .logo {
        font-size: 1.15rem;
    }

    .logo-img {
        height: 30px;
    }

    .nav-cta {
        display: none;
    }

    .hero-cta {
        flex-direction: column;
    }

    .hero-cta .btn {
        width: 100%;
        text-align: center;
    }

    table {
        font-size: 0.85rem;
    }

    .sticky-cta {
        padding: 0.6rem 0.75rem;
    }

    .sticky-cta .btn {
        font-size: 0.85rem;
        padding: 0.6rem 0.5rem;
    }
}
"""
    
    css_path = CSS_DIR / "style.css"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    # Generate JS
    print("  → Generating JS...")
    js_dir = SITE_ROOT / "js"
    js_dir.mkdir(exist_ok=True)
    js_content = """/* Peace Blooming — minimal site JS */

(function () {
    'use strict';

    // Mobile nav toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            const expanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', String(!expanded));
            navMenu.classList.toggle('is-open');
            document.body.classList.toggle('nav-open');
        });

        // Close menu when a link is clicked
        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('is-open');
                document.body.classList.remove('nav-open');
            });
        });
    }

    // Sticky CTA: hide when footer is in view, show otherwise
    const stickyCta = document.querySelector('.sticky-cta');
    const footer = document.querySelector('footer');

    if (stickyCta && footer && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    stickyCta.classList.add('is-hidden');
                } else {
                    stickyCta.classList.remove('is-hidden');
                }
            });
        }, { threshold: 0.1 });

        observer.observe(footer);
    }

    // Contact form success message
    const formSuccess = document.getElementById('form-success');
    const serviceForm = document.getElementById('service-request');
    if (formSuccess && serviceForm) {
        const params = new URLSearchParams(window.location.search);
        if (params.get('success') === '1') {
            formSuccess.removeAttribute('hidden');
            serviceForm.setAttribute('hidden', '');
        }
    }
})();
"""
    js_path = js_dir / "site.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    # Generate robots.txt
    print("  → Generating robots.txt...")
    robots_content = """User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: *
Allow: /

Sitemap: https://www.peaceblooming.com/sitemap.xml
"""
    
    robots_path = SITE_ROOT / "robots.txt"
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write(robots_content)
    
    # Generate sitemap.xml
    print("  → Generating sitemap.xml...")
    all_urls = [
        "/index.html",
        "/services-and-pricing.html",
        "/how-it-works.html",
        "/service-area.html",
        "/about.html",
        "/faq.html",
        "/contact.html",
        "/blog.html",
        "/gallery.html",
    ]
    
    for slug, _, _ in CEMETERIES:
        all_urls.append(f"/service-area/{slug}.html")
    
    for slug, _, _ in CITIES:
        all_urls.append(f"/service-area/{slug}.html")
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in all_urls:
        # Remove index.html from URL
        if url == "/index.html":
            clean_url = "/"
        else:
            clean_url = url
        
        sitemap_xml += f"""  <url>
    <loc>https://www.peaceblooming.com{clean_url}</loc>
    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
    <changefreq>monthly</changefreq>
  </url>
"""
    
    sitemap_xml += '</urlset>\n'
    
    sitemap_path = SITE_ROOT / "sitemap.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    # Generate netlify.toml
    print("  → Generating netlify.toml...")
    netlify_toml = """[build]
  publish = "."
  command = ""

[[redirects]]
  from = "/index.html"
  to = "/"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
"""
    
    netlify_path = SITE_ROOT / "netlify.toml"
    with open(netlify_path, 'w', encoding='utf-8') as f:
        f.write(netlify_toml)
    
    # Generate .gitignore
    print("  → Generating .gitignore...")
    gitignore = """__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.vscode/
.DS_Store
*.local
"""
    
    gitignore_path = SITE_ROOT / ".gitignore"
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(gitignore)
    
    # Generate README for the site
    print("  → Generating site README...")
    readme_content = """# Peace Blooming Website

A static site for Peace Blooming, a grave cleaning and seasonal flower decorating service in Michigan.

## About

This is the website for Peace Blooming, serving Metro Detroit including Downriver and Metro Ann Arbor with professional grave cleaning and seasonal decorating services. The site is built as a pure static HTML/CSS site with no server-side processing or build step — just open the files in a browser or deploy directly to any host.

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
- Insurance coverage statement — Already updated to "Metro Detroit area" on `/about.html` and `/faq.html`.
- Response time — Already set to **24–48 hours** on `/contact.html` and the success page.
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

Built with Python. Last updated: {timestamp}
""".format(timestamp=datetime.now().strftime("%Y-%m-%d"))
    
    readme_path = SITE_ROOT / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("\n✓ Site generation complete!")
    print(f"  Location: {SITE_ROOT}")
    print(f"  Pages: 38 (9 core + 9 cemetery + 20 city)")
    print(f"  Images: 10 placeholder files")
    print(f"  Static assets: CSS, robots.txt, sitemap.xml, netlify.toml")
    print("\nNext steps:")
    print("  1. Preview locally: cd site && python3 -m http.server 8000")
    print("  2. Update placeholders: [PHONE] (remaining), [EMAIL], [PHOTOS]")
    print("  3. Add real photos to images/ subdirectories")
    print("  4. Commit changes from the project root and push to GitHub")
    print("  5. Netlify auto-deploys the site/ folder")

if __name__ == "__main__":
    main()
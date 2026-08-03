#!/usr/bin/env python3
"""
Peace Blooming — Pre-Launch Verification Script

Run this after `python3 build_site.py` to catch missing placeholders,
broken links, missing images, and incomplete configuration before launch.
"""

import re
import sys
import json
from pathlib import Path
from html.parser import HTMLParser

PROJECT_ROOT = Path("/Users/themachine2.0/Desktop/AI/Peace Blooming/3-Website")
SITE_ROOT = PROJECT_ROOT / "site"
IMAGES_DIR = SITE_ROOT / "images"
BUILD_SCRIPT = PROJECT_ROOT / "build_site.py"

PLACEHOLDERS = ["[PHONE]", "[EMAIL]", "[COVERAGE AMOUNT]", "[RESPONSE TIME]", "[PHOTOS]"]
UTILITY_PAGES = {"form-blueprint.html"}
REQUIRED_IMAGES = [
    "images/logo/logo.png",
    "images/logo/favicon.png",
    "images/logo/apple-touch-icon.png",
    "images/social/default.jpg",
]

CONTENT_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


class LinkExtractor(HTMLParser):
    def __init__(self, base_path):
        super().__init__()
        self.base_path = base_path
        self.links = []
        self.images = []
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs.get("href"))
        if tag == "img" and attrs.get("src"):
            self.images.append(attrs.get("src"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")


def find_all_html_files():
    return sorted(SITE_ROOT.rglob("*.html"))


def is_utility_page(f):
    return f.name in UTILITY_PAGES or f.parent.name != "site" and f.name in UTILITY_PAGES


def check_placeholders(files):
    issues = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        for ph in PLACEHOLDERS:
            if ph in text:
                issues.append((f.relative_to(SITE_ROOT), ph))
    return issues


def check_required_images():
    missing = []
    for img in REQUIRED_IMAGES:
        if not (SITE_ROOT / img).exists():
            missing.append(img)
    return missing


def check_social_tags(files):
    issues = []
    required = ["og:title", "og:description", "og:image", "og:url", "og:type",
                "twitter:card", "twitter:title", "twitter:description", "twitter:image"]
    for f in files:
        if is_utility_page(f):
            continue
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(SITE_ROOT)
        for tag in required:
            if f'property="{tag}"' not in text and f'name="{tag}"' not in text:
                issues.append((rel, tag))
    return issues


def check_canonical_and_hreflang(files):
    issues = []
    for f in files:
        if is_utility_page(f):
            continue
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(SITE_ROOT)
        if 'rel="canonical"' not in text:
            issues.append((rel, "missing canonical"))
        if 'hreflang="en-us"' not in text:
            issues.append((rel, "missing hreflang en-us"))
    return issues


def check_jsonld_validity(files):
    issues = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(SITE_ROOT)
        for match in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL):
            try:
                json.loads(match.group(1))
            except json.JSONDecodeError as e:
                issues.append((rel, f"invalid JSON-LD: {e}"))
    return issues


def check_broken_internal_links(files):
    issues = []
    for f in files:
        extractor = LinkExtractor(f)
        extractor.feed(f.read_text(encoding="utf-8"))
        for href in extractor.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if href.startswith("#"):
                continue
            target = SITE_ROOT / href.lstrip("/")
            if not target.exists():
                issues.append((f.relative_to(SITE_ROOT), href))
    return issues


def check_analytics_configuration():
    issues = []
    text = BUILD_SCRIPT.read_text(encoding="utf-8")
    if 'GA_MEASUREMENT_ID = ""' in text:
        issues.append("GA_MEASUREMENT_ID is empty")
    if 'GOOGLE_SEARCH_CONSOLE_TAG = ""' in text:
        issues.append("GOOGLE_SEARCH_CONSOLE_TAG is empty")
    return issues


def check_image_alt_text(files):
    """Check that all public pages have non-empty alt text on every <img> tag."""
    issues = []
    for f in files:
        if is_utility_page(f):
            continue
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(SITE_ROOT)
        for match in re.finditer(r'<img[^>]*>', text, re.IGNORECASE):
            img_tag = match.group(0)
            alt_match = re.search(r'alt\s*=\s*"([^"]*)"', img_tag, re.IGNORECASE)
            if not alt_match:
                issues.append((rel, "img tag missing alt attribute"))
            elif alt_match.group(1).strip() == "":
                issues.append((rel, "img tag has empty alt attribute"))
    return issues


def check_webp_variants():
    """Check that every content image (JPG/PNG) has a corresponding WebP variant."""
    issues = []
    if not IMAGES_DIR.exists():
        return issues
    for img_path in IMAGES_DIR.rglob("*"):
        if img_path.is_file() and img_path.suffix.lower() in CONTENT_IMAGE_EXTENSIONS:
            webp_path = img_path.with_suffix(".webp")
            if not webp_path.exists():
                issues.append(f"Missing WebP variant for {img_path.relative_to(SITE_ROOT)}")
    return issues



def main():
    print("Peace Blooming Pre-Launch Check")
    print("=" * 40)

    if not SITE_ROOT.exists():
        print("ERROR: site/ directory not found. Run `python3 build_site.py` first.")
        sys.exit(1)

    files = find_all_html_files()
    print(f"HTML files checked: {len(files)}\n")

    hard_issues = []
    warnings = []

    checks = [
        ("Placeholders", check_placeholders, hard_issues),
        ("Required images", check_required_images, hard_issues),
        ("Social tags", check_social_tags, hard_issues),
        ("Canonical + hreflang", check_canonical_and_hreflang, hard_issues),
        ("JSON-LD validity", check_jsonld_validity, hard_issues),
        ("Broken internal links", check_broken_internal_links, hard_issues),
        ("Image alt text", check_image_alt_text, hard_issues),
        ("WebP image variants", check_webp_variants, hard_issues),
        ("Analytics configuration", check_analytics_configuration, warnings),
    ]

    for name, fn, bucket in checks:
        print(f"Checking {name}...")
        if fn in (check_required_images, check_analytics_configuration, check_webp_variants):
            result = fn()
        else:
            result = fn(files)
        if result:
            bucket.extend((name, item) for item in result)

    print()

    def print_issues(issues, label):
        if not issues:
            return
        print(f"{label} ({len(issues)}):\n")
        current_section = None
        for section, item in issues:
            if section != current_section:
                current_section = section
                print(f"{section}:")
            if isinstance(item, tuple):
                print(f"  - {item[0]}: {item[1]}")
            else:
                print(f"  - {item}")
        print()

    print_issues(warnings, "Warnings")
    print_issues(hard_issues, "Issues to fix before launch")

    if hard_issues:
        print("Fix the hard issues above, then rerun this script.")
        sys.exit(1)
    elif warnings:
        print("All hard checks passed. Review the warnings above before launch.")
        sys.exit(0)
    else:
        print("All checks passed. Site is ready for final review.")
        sys.exit(0)


if __name__ == "__main__":
    main()

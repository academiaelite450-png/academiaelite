#!/usr/bin/env python3
"""Generate a 10-slide Instagram/LinkedIn carousel for the Zero-to-Millions Blueprint."""

from PIL import Image, ImageDraw, ImageFont
import os

# --- Config ---
W, H = 1080, 1080
OUTPUT_DIR = "carousel_slides"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors
BG_DARK = "#0F0F0F"
BG_CARD = "#1A1A2E"
ACCENT = "#00D4AA"
ACCENT2 = "#7B61FF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#B0B0B0"
DARK_TEXT = "#0F0F0F"
ORANGE = "#FF6B35"
YELLOW = "#FFD93D"

# Fonts
def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

FONT_TITLE = font(52, bold=True)
FONT_SUBTITLE = font(30)
FONT_BODY = font(28)
FONT_BODY_BOLD = font(28, bold=True)
FONT_BIG = font(72, bold=True)
FONT_HUGE = font(96, bold=True)
FONT_SMALL = font(22)
FONT_TAG = font(20, bold=True)
FONT_NUM = font(120, bold=True)
FONT_MID = font(38, bold=True)


def new_slide():
    img = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    return img, draw


def draw_rounded_rect(draw, xy, fill, radius=20):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def draw_accent_bar(draw, y=0):
    draw.rectangle([0, y, W, y + 6], fill=ACCENT)


def draw_bottom_bar(draw):
    draw.rectangle([0, H - 60, W, H], fill=BG_CARD)
    draw.text((W // 2, H - 30), "@academiaelite", font=FONT_SMALL, fill=LIGHT_GRAY, anchor="mm")


def draw_slide_number(draw, num, total=10):
    draw.text((W - 50, 40), f"{num}/{total}", font=FONT_SMALL, fill=LIGHT_GRAY, anchor="rm")


def wrap_text(text, font_obj, max_width, draw):
    """Simple word-wrap."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, x, y, text, f, fill, max_w, line_spacing=8):
    lines = wrap_text(text, f, max_w, draw)
    for line in lines:
        draw.text((x, y), line, font=f, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=f)
        y += (bbox[3] - bbox[1]) + line_spacing
    return y


# ============================================================
# SLIDE 1: Cover
# ============================================================
def slide_1():
    img, draw = new_slide()
    # gradient-like effect with rectangles
    for i in range(H):
        r = int(15 + (i / H) * 10)
        g = int(15 + (i / H) * 15)
        b = int(46 + (i / H) * 20)
        draw.line([(0, i), (W, i)], fill=(r, g, b))

    draw_accent_bar(draw, 0)

    # Tag
    draw_rounded_rect(draw, (80, 120, 480, 170), fill=ACCENT, radius=25)
    draw.text((280, 145), "ZERO INVESTMENT REQUIRED", font=FONT_TAG, fill=DARK_TEXT, anchor="mm")

    # Main title
    y = 220
    draw.text((W // 2, y), "$0 to", font=FONT_TITLE, fill=LIGHT_GRAY, anchor="mt")
    y += 70
    draw.text((W // 2, y), "MILLIONS", font=FONT_HUGE, fill=ACCENT, anchor="mt")
    y += 120
    draw.text((W // 2, y), "With Just a", font=FONT_TITLE, fill=WHITE, anchor="mt")
    y += 65
    draw.text((W // 2, y), "Laptop & WiFi", font=FONT_TITLE, fill=WHITE, anchor="mt")

    y += 110
    draw_rounded_rect(draw, (140, y, W - 140, y + 80), fill=BG_CARD, radius=15)
    draw.text((W // 2, y + 40), "A 3-Phase Blueprint That Actually Works", font=FONT_BODY, fill=ACCENT, anchor="mm")

    y += 120
    draw.text((W // 2, y), "Backed by real people who did it.", font=FONT_SUBTITLE, fill=LIGHT_GRAY, anchor="mt")
    draw.text((W // 2, y + 40), "No fluff. No fabrication.", font=FONT_SUBTITLE, fill=LIGHT_GRAY, anchor="mt")

    # Swipe indicator
    draw.text((W // 2, H - 90), "SWIPE  >>>", font=FONT_MID, fill=YELLOW, anchor="mm")
    draw_bottom_bar(draw)
    draw_slide_number(draw, 1)
    return img


# ============================================================
# SLIDE 2: The Problem
# ============================================================
def slide_2():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw.text((W // 2, 80), "Why Most People Fail", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 145), "at Making Money Online", font=FONT_TITLE, fill=ACCENT, anchor="mt")

    mistakes = [
        ("They buy courses", "instead of starting"),
        ("They chase passive income", "before earning active income"),
        ("They build a product", "nobody asked for"),
        ("They spread across", "10 platforms at once"),
        ("They wait for the", "perfect idea forever"),
    ]

    y = 260
    for i, (line1, line2) in enumerate(mistakes):
        draw_rounded_rect(draw, (60, y, W - 60, y + 110), fill=BG_CARD, radius=15)
        draw.text((110, y + 25), "X", font=FONT_MID, fill=ORANGE)
        draw.text((160, y + 22), line1, font=FONT_BODY_BOLD, fill=WHITE)
        draw.text((160, y + 60), line2, font=FONT_BODY, fill=LIGHT_GRAY)
        y += 125

    y += 20
    draw.text((W // 2, y), "This blueprint fixes all of that.", font=FONT_SUBTITLE, fill=ACCENT, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 2)
    return img


# ============================================================
# SLIDE 3: The 3-Phase Overview
# ============================================================
def slide_3():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw.text((W // 2, 70), "The 3-Phase Engine", font=FONT_TITLE, fill=WHITE, anchor="mt")

    phases = [
        ("1", "FREELANCING", "Month 1-3", "$1K-5K/mo", "Sell skills, build cash flow"),
        ("2", "PRODUCTIZE", "Month 3-12", "$5K-20K/mo", "Recurring revenue, systems"),
        ("3", "MICRO-SAAS", "Month 6-24", "$100K-1M+/yr", "Software scales infinitely"),
    ]

    colors = [ACCENT, ACCENT2, YELLOW]

    y = 200
    for i, (num, title, timeline, revenue, desc) in enumerate(phases):
        color = colors[i]
        draw_rounded_rect(draw, (60, y, W - 60, y + 210), fill=BG_CARD, radius=20)

        # Number circle
        draw.ellipse([90, y + 20, 170, y + 100], fill=color)
        draw.text((130, y + 60), num, font=FONT_BIG, fill=DARK_TEXT, anchor="mm")

        # Text
        draw.text((200, y + 25), title, font=FONT_MID, fill=color)
        draw.text((200, y + 75), timeline, font=FONT_SMALL, fill=LIGHT_GRAY)

        # Revenue badge
        draw_rounded_rect(draw, (200, y + 115, 520, y + 160), fill=color, radius=12)
        draw.text((360, y + 137), revenue, font=FONT_BODY_BOLD, fill=DARK_TEXT, anchor="mm")

        draw.text((200, y + 175), desc, font=FONT_SMALL, fill=LIGHT_GRAY)

        y += 230

    draw.text((W // 2, y + 15), "Each phase de-risks and funds the next", font=FONT_BODY, fill=ACCENT, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 3)
    return img


# ============================================================
# SLIDE 4: Phase 1 — Freelancing
# ============================================================
def slide_4():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw_rounded_rect(draw, (60, 50, 320, 100), fill=ACCENT, radius=25)
    draw.text((190, 75), "PHASE 1", font=FONT_TAG, fill=DARK_TEXT, anchor="mm")

    draw.text((W // 2, 140), "Start Freelancing", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 200), "Month 1-3  |  $0 Investment", font=FONT_SUBTITLE, fill=LIGHT_GRAY, anchor="mt")

    skills = [
        ("AI Copywriting", "$50-300/project"),
        ("Website Building", "$200-2,000/site"),
        ("Video Editing", "$50-500/video"),
        ("Resume Writing", "$50-200/resume"),
        ("SEO Writing", "$0.10-0.50/word"),
        ("Social Media Mgmt", "$500-2K/mo/client"),
    ]

    y = 280
    for i, (skill, rate) in enumerate(skills):
        draw_rounded_rect(draw, (60, y, W - 60, y + 70), fill=BG_CARD, radius=12)
        draw.text((100, y + 35), skill, font=FONT_BODY_BOLD, fill=WHITE, anchor="lm")
        draw.text((W - 100, y + 35), rate, font=FONT_BODY, fill=ACCENT, anchor="rm")
        y += 82

    y += 15
    draw_rounded_rect(draw, (60, y, W - 60, y + 85), fill="#1a2e1a", radius=15)
    draw.text((W // 2, y + 20), "Platforms: Fiverr + Upwork + LinkedIn", font=FONT_BODY, fill=ACCENT, anchor="mt")
    draw.text((W // 2, y + 55), "All FREE to join", font=FONT_SMALL, fill=LIGHT_GRAY, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 4)
    return img


# ============================================================
# SLIDE 5: Real Proof — Freelancing
# ============================================================
def slide_5():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw.text((W // 2, 70), "Real People. Real Money.", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 130), "Freelancing Success Stories", font=FONT_SUBTITLE, fill=ACCENT, anchor="mt")

    stories = [
        ("Georgia Austin", "$1.7M in 17 months", "Started as a freelance writer on Fiverr.",
         "Now runs 2 companies with 100+ writers.", ACCENT),
        ("Charmaine Pocek", "$1.2M on Fiverr", "Started writing resumes for $5 each.",
         "First US female seller to break $1M.", ACCENT2),
        ("Vadim Dagman", "$1M+ via Toptal", "Full-time freelance developer.",
         "Holds 7 patents, co-founded 2 companies.", YELLOW),
    ]

    y = 210
    for name, amount, line1, line2, color in stories:
        draw_rounded_rect(draw, (60, y, W - 60, y + 210), fill=BG_CARD, radius=20)

        draw.text((100, y + 30), name, font=FONT_MID, fill=WHITE)
        draw_rounded_rect(draw, (100, y + 80, 460, y + 120), fill=color, radius=10)
        draw.text((280, y + 100), amount, font=FONT_BODY_BOLD, fill=DARK_TEXT, anchor="mm")
        draw.text((100, y + 140), line1, font=FONT_SMALL, fill=LIGHT_GRAY)
        draw.text((100, y + 170), line2, font=FONT_SMALL, fill=LIGHT_GRAY)

        y += 230

    draw_bottom_bar(draw)
    draw_slide_number(draw, 5)
    return img


# ============================================================
# SLIDE 6: Phase 2 — Productize
# ============================================================
def slide_6():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw_rounded_rect(draw, (60, 50, 320, 100), fill=ACCENT2, radius=25)
    draw.text((190, 75), "PHASE 2", font=FONT_TAG, fill=WHITE, anchor="mm")

    draw.text((W // 2, 140), "Productize Your Service", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 200), "Month 3-12  |  Still $0 Investment", font=FONT_SUBTITLE, fill=LIGHT_GRAY, anchor="mt")

    y = 290
    draw.text((W // 2, y), "Stop trading time for money.", font=FONT_MID, fill=ORANGE, anchor="mt")
    draw.text((W // 2, y + 50), "Package your best service into a", font=FONT_BODY, fill=WHITE, anchor="mt")
    draw.text((W // 2, y + 85), "fixed-scope, fixed-price, recurring offer.", font=FONT_BODY, fill=WHITE, anchor="mt")

    examples = [
        "4 SEO blogs/month ---- $800/mo",
        "Instagram management -- $1,500/mo",
        "Landing page in 48hrs - $500 each",
    ]

    y = 500
    for ex in examples:
        draw_rounded_rect(draw, (80, y, W - 80, y + 60), fill=BG_CARD, radius=12)
        draw.text((W // 2, y + 30), ex, font=FONT_BODY, fill=ACCENT, anchor="mm")
        y += 75

    y += 20
    draw_rounded_rect(draw, (100, y, W - 100, y + 100), fill="#2e1a2e", radius=15)
    draw.text((W // 2, y + 25), "Ted Raad did exactly this.", font=FONT_BODY_BOLD, fill=ACCENT2, anchor="mt")
    draw.text((W // 2, y + 60), "Laptop + WiFi --> $80 MILLION/year", font=FONT_BODY, fill=WHITE, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 6)
    return img


# ============================================================
# SLIDE 7: Phase 3 — Micro-SaaS
# ============================================================
def slide_7():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw_rounded_rect(draw, (60, 50, 320, 100), fill=YELLOW, radius=25)
    draw.text((190, 75), "PHASE 3", font=FONT_TAG, fill=DARK_TEXT, anchor="mm")

    draw.text((W // 2, 140), "Build a Micro-SaaS", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 200), "The Millions Play", font=FONT_SUBTITLE, fill=YELLOW, anchor="mt")

    y = 280
    draw.text((60, y), "Your freelancing told you what", font=FONT_BODY, fill=WHITE)
    draw.text((60, y + 38), "people pay for. Now automate it.", font=FONT_BODY, fill=WHITE)

    founders = [
        ("Pieter Levels", "Nomad List", "$3M+/yr", "Solo"),
        ("AJ", "Carrd", "$360K/yr", "Solo"),
        ("Mizanur Rahman", "Dorik", "$11.9M/yr", "Started solo"),
        ("Nathan Barry", "ConvertKit", "$25M/yr", "Tiny start"),
    ]

    y = 400
    # Header
    draw_rounded_rect(draw, (60, y, W - 60, y + 50), fill=ACCENT, radius=10)
    draw.text((100, y + 25), "Founder", font=FONT_TAG, fill=DARK_TEXT, anchor="lm")
    draw.text((420, y + 25), "Product", font=FONT_TAG, fill=DARK_TEXT, anchor="lm")
    draw.text((700, y + 25), "Revenue", font=FONT_TAG, fill=DARK_TEXT, anchor="lm")
    draw.text((920, y + 25), "Team", font=FONT_TAG, fill=DARK_TEXT, anchor="lm")
    y += 60

    for name, product, rev, team in founders:
        draw_rounded_rect(draw, (60, y, W - 60, y + 55), fill=BG_CARD, radius=8)
        draw.text((100, y + 28), name, font=FONT_SMALL, fill=WHITE, anchor="lm")
        draw.text((420, y + 28), product, font=FONT_SMALL, fill=LIGHT_GRAY, anchor="lm")
        draw.text((700, y + 28), rev, font=FONT_SMALL, fill=YELLOW, anchor="lm")
        draw.text((920, y + 28), team, font=FONT_SMALL, fill=LIGHT_GRAY, anchor="lm")
        y += 65

    y += 20
    draw_rounded_rect(draw, (100, y, W - 100, y + 80), fill="#2e2e1a", radius=15)
    draw.text((W // 2, y + 20), "Build free: VS Code + Vercel + Supabase", font=FONT_BODY, fill=YELLOW, anchor="mt")
    draw.text((W // 2, y + 55), "Launch free: Product Hunt + Reddit + X", font=FONT_SMALL, fill=LIGHT_GRAY, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 7)
    return img


# ============================================================
# SLIDE 8: The Math
# ============================================================
def slide_8():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw.text((W // 2, 70), "The Math", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 130), "How This Reaches Millions", font=FONT_SUBTITLE, fill=ACCENT, anchor="mt")

    rows = [
        ("FREELANCING", "$3K/mo x 12", "$36,000", ACCENT),
        ("PRODUCTIZED", "$15K/mo x 12", "$180,000", ACCENT2),
        ("MICRO-SAAS", "1K users x $29/mo", "$348,000", YELLOW),
    ]

    y = 220
    for label, calc, total, color in rows:
        draw_rounded_rect(draw, (60, y, W - 60, y + 100), fill=BG_CARD, radius=15)
        draw_rounded_rect(draw, (60, y, 300, y + 100), fill=color, radius=15)
        draw.text((180, y + 50), label, font=FONT_TAG, fill=DARK_TEXT, anchor="mm")
        draw.text((520, y + 50), calc, font=FONT_BODY, fill=LIGHT_GRAY, anchor="mm")
        draw.text((W - 120, y + 50), total, font=FONT_BODY_BOLD, fill=color, anchor="mm")
        y += 120

    # Combined
    y += 20
    draw_rounded_rect(draw, (60, y, W - 60, y + 100), fill=ACCENT, radius=20)
    draw.text((W // 2, y + 25), "COMBINED YEAR 2", font=FONT_TAG, fill=DARK_TEXT, anchor="mt")
    draw.text((W // 2, y + 60), "$564,000/year", font=FONT_MID, fill=DARK_TEXT, anchor="mt")

    y += 130
    draw_rounded_rect(draw, (60, y, W - 60, y + 100), fill=YELLOW, radius=20)
    draw.text((W // 2, y + 25), "SCALING TO B2B (2K users x $199/mo)", font=FONT_TAG, fill=DARK_TEXT, anchor="mt")
    draw.text((W // 2, y + 60), "$4.8 MILLION / year", font=FONT_MID, fill=DARK_TEXT, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 8)
    return img


# ============================================================
# SLIDE 9: Week 1 Action Plan
# ============================================================
def slide_9():
    img, draw = new_slide()
    draw_accent_bar(draw)

    draw.text((W // 2, 70), "Your Week 1", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 130), "Action Plan", font=FONT_TITLE, fill=ACCENT, anchor="mt")

    steps = [
        ("DAY 1", "Choose your skill (writing, design,\nvideo editing, web dev, social media)"),
        ("DAY 1", "Create Fiverr + Upwork accounts\n(completely free)"),
        ("DAY 2", "Study top sellers in your niche.\nCopy their gig structure, not prices."),
        ("DAY 3-4", "Build 2-3 portfolio samples\nusing free AI tools"),
        ("DAY 5-7", "Send 10 proposals/day.\nOptimize gigs with keywords."),
        ("WEEK 1", "Land your first client.\nEven $10 -- the REVIEW matters more."),
    ]

    y = 220
    for day, desc in steps:
        draw_rounded_rect(draw, (60, y, W - 60, y + 105), fill=BG_CARD, radius=12)
        draw_rounded_rect(draw, (60, y, 230, y + 105), fill=ACCENT2, radius=12)
        draw.text((145, y + 52), day, font=FONT_TAG, fill=WHITE, anchor="mm")
        lines = desc.split("\n")
        draw.text((250, y + 30), lines[0], font=FONT_SMALL, fill=WHITE)
        if len(lines) > 1:
            draw.text((250, y + 60), lines[1], font=FONT_SMALL, fill=LIGHT_GRAY)
        y += 115

    draw_bottom_bar(draw)
    draw_slide_number(draw, 9)
    return img


# ============================================================
# SLIDE 10: CTA
# ============================================================
def slide_10():
    img, draw = new_slide()

    for i in range(H):
        r = int(15 + (i / H) * 10)
        g = int(15 + (i / H) * 15)
        b = int(46 + (i / H) * 20)
        draw.line([(0, i), (W, i)], fill=(r, g, b))

    draw_accent_bar(draw)

    draw.text((W // 2, 150), "The Only Investment", font=FONT_TITLE, fill=WHITE, anchor="mt")
    draw.text((W // 2, 215), "You Need:", font=FONT_TITLE, fill=WHITE, anchor="mt")

    y = 330
    items = [
        ("A Laptop", ACCENT),
        ("WiFi", ACCENT2),
        ("Consistency", YELLOW),
    ]
    for item, color in items:
        draw.text((W // 2, y), item, font=FONT_BIG, fill=color, anchor="mt")
        y += 100

    y += 30
    draw_rounded_rect(draw, (120, y, W - 120, y + 70), fill=ACCENT, radius=35)
    draw.text((W // 2, y + 35), "SAVE THIS. START TODAY.", font=FONT_MID, fill=DARK_TEXT, anchor="mm")

    y += 100
    draw.text((W // 2, y), "Follow @academiaelite for more", font=FONT_SUBTITLE, fill=LIGHT_GRAY, anchor="mt")

    draw_bottom_bar(draw)
    draw_slide_number(draw, 10)
    return img


# ============================================================
# Generate all slides
# ============================================================
slides = [slide_1, slide_2, slide_3, slide_4, slide_5,
          slide_6, slide_7, slide_8, slide_9, slide_10]

for i, slide_fn in enumerate(slides, 1):
    img = slide_fn()
    path = os.path.join(OUTPUT_DIR, f"slide_{i:02d}.png")
    img.save(path, "PNG", quality=95)
    print(f"Created: {path}")

print(f"\nDone! {len(slides)} slides saved to {OUTPUT_DIR}/")

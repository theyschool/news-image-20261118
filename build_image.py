#!/usr/bin/env python3
"""Render the news-image-20261118 poster: 'THE WORLD IN ONE DAY',
Wednesday 18 November 2026. All text is drawn with real fonts
(Liberation Serif/Sans); every illustration is drawn with PIL
primitives. No AI-generated imagery, no network. Deterministic:
same input, same bytes out."""

import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 247, 240)
INK = (26, 26, 26)
NAVY = (15, 42, 74)
NAVY_DARK = (10, 30, 54)
GOLD = (232, 184, 75)
RED = (185, 28, 28)
GRAY = (110, 110, 105)
RULE = (200, 192, 178)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def draw_tracked(draw, xy, s, f, fill, tracking=0):
    """Draw text with manual letter tracking (PIL has no tracking)."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x


def wrap(draw, s, f, max_w):
    """Greedy word wrap to lines fitting max_w."""
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, s, f, fill, tracking=0):
    w = sum(draw.textlength(ch, font=f) + tracking for ch in s) - tracking
    draw_tracked(draw, (cx - w / 2, y), s, f, fill, tracking)
    return w

# ---------------------------------------------------------------- illustrations
# Every picture is drawn from primitives: flat colour, bold shapes, no text.

def ill_summit(draw, box):
    """Summit: Shenzhen skyline at dawn, a tall spire above the towers."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    # dawn sky
    draw.rectangle(box, fill=(232, 222, 190))
    # sun
    sx, sy = x0 + int(w * 0.72), y0 + int(h * 0.24)
    draw.ellipse([sx - 20, sy - 20, sx + 20, sy + 20], fill=(232, 184, 75))
    # skyline: towers of different heights, dark silhouettes
    base = y0 + int(h * 0.88)
    towers = [(0.04, 0.52), (0.20, 0.70), (0.36, 0.44), (0.52, 0.62),
              (0.66, 0.86), (0.82, 0.58)]
    for fx, fh in towers:
        tx0 = x0 + int(w * fx)
        tw = int(w * 0.13)
        th = int(h * fh)
        draw.rectangle([tx0, base - th, tx0 + tw, base], fill=(38, 52, 74))
    # tall spire (Ping An style) rising above the rest
    px = x0 + int(w * 0.66)
    draw.polygon([(px - 8, base), (px, y0 + int(h * 0.06)), (px + 8, base)],
                 fill=(15, 42, 74))
    # ground
    draw.rectangle([x0, base, x1, y1], fill=(38, 52, 74))
    # lit windows
    for wx, wy in ((0.09, 0.60), (0.25, 0.52), (0.41, 0.68), (0.57, 0.58),
                   (0.72, 0.46), (0.87, 0.66)):
        draw.rectangle([x0 + int(w * wx), y0 + int(h * wy),
                        x0 + int(w * wx) + 5, y0 + int(h * wy) + 5],
                       fill=(232, 184, 75))


def ill_gulf(draw, box):
    """Gulf: radar dish sweeping, hostile drones overhead, shield below.
    Fixed sizes scale with the box so the picture reads in the large
    lead slot as well as in a grid cell."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    sc = min(w, h) / 168.0
    draw.rectangle(box, fill=(245, 232, 200))
    cx, cy = x0 + w // 2, y0 + int(h * 0.62)
    # signal arcs
    for r in (34, 52, 70):
        r = int(r * sc)
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=340,
                 fill=(46, 125, 50), width=max(2, int(4 * sc)))
    # radar dish
    R = int(46 * sc)
    draw.pieslice([cx - R, cy - R, cx + R, cy + R], start=180, end=360,
                  fill=(70, 70, 70))
    draw.rectangle([cx - int(4 * sc), cy, cx + int(4 * sc), cy + int(34 * sc)],
                   fill=(70, 70, 70))
    draw.rectangle([cx - int(26 * sc), cy + int(34 * sc),
                    cx + int(26 * sc), cy + int(40 * sc)], fill=(70, 70, 70))
    # drones
    def drone(dx, dy, s):
        s = max(4, int(s * sc))
        draw.ellipse([dx - s, dy - s // 2, dx + s, dy + s // 2], fill=(26, 26, 26))
        draw.line([(dx - s - 6, dy - s // 2 - 4), (dx + s + 6, dy - s // 2 - 4)],
                  fill=(26, 26, 26), width=2)
        draw.line([(dx - s - 6, dy + s // 2 + 4), (dx + s + 6, dy + s // 2 + 4)],
                  fill=(26, 26, 26), width=2)
        draw.line([(dx, dy - s), (dx, dy + 8)], fill=(26, 26, 26), width=2)
    drone(x0 + int(w * 0.24), y0 + int(h * 0.20), 12)
    drone(x0 + int(w * 0.76), y0 + int(h * 0.14), 10)
    drone(x0 + int(w * 0.55), y0 + int(h * 0.30), 8)
    # interception burst
    bx, by = x0 + int(w * 0.76), y0 + int(h * 0.14)
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        draw.line([(bx + 16 * sc * math.cos(a), by + 16 * sc * math.sin(a)),
                   (bx + 26 * sc * math.cos(a), by + 26 * sc * math.sin(a))],
                  fill=(185, 28, 28), width=3)


def ill_plane(draw, box):
    """Diplomacy: jet crossing a globe."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle(box, fill=(220, 232, 240))
    cx, cy, r = x0 + w // 2, y0 + int(h * 0.62), int(min(w, h) * 0.30)
    # globe
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 90, 136))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=3)
    for k in (-0.55, 0, 0.55):
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=270 + k * 90, end=270 + k * 90 + 180,
                 fill=(255, 255, 255), width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=2)
    draw.arc([cx - int(r * 0.55), cy - int(r * 0.32), cx + int(r * 0.55), cy + int(r * 0.32)],
             start=0, end=360, fill=(255, 255, 255), width=2)
    # jet: clean side profile in the sky above the globe
    jx, jy = x0 + int(w * 0.10), y0 + int(h * 0.10)
    # fuselage: long tapered body, nose to the right
    draw.polygon([(jx, jy + 6), (jx + 58, jy), (jx + 76, jy + 4), (jx + 76, jy + 8),
                  (jx + 58, jy + 12), (jx, jy + 12)], fill=(26, 26, 26))
    # main wing sweeping down-back
    draw.polygon([(jx + 30, jy + 10), (jx + 44, jy + 10), (jx + 34, jy + 30), (jx + 24, jy + 30)],
                 fill=(26, 26, 26))
    # tail fin
    draw.polygon([(jx + 4, jy + 8), (jx + 12, jy - 10), (jx + 18, jy - 10), (jx + 16, jy + 8)],
                 fill=(26, 26, 26))
    # flight path dashes behind the jet
    for i in range(3):
        px = jx + 84 + i * 16
        draw.line([(px, jy + 6), (px + 9, jy + 6)], fill=(110, 110, 105), width=2)


def ill_chip(draw, box):
    """Tech: microchip with a rising chart."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle(box, fill=(224, 240, 224))
    cx, cy = x0 + int(w * 0.38), y0 + int(h * 0.52)
    s = int(min(w, h) * 0.30)
    # pins
    for i in range(4):
        off = -s + i * (2 * s // 3)
        draw.rectangle([cx + off - 4, cy - s - 12, cx + off + 4, cy - s], fill=(90, 90, 90))
        draw.rectangle([cx + off - 4, cy + s, cx + off + 4, cy + s + 12], fill=(90, 90, 90))
        draw.rectangle([cx - s - 12, cy + off - 4, cx - s, cy + off + 4], fill=(90, 90, 90))
        draw.rectangle([cx + s, cy + off - 4, cx + s + 12, cy + off + 4], fill=(90, 90, 90))
    draw.rectangle([cx - s, cy - s, cx + s, cy + s], fill=(26, 26, 26))
    draw.rectangle([cx - s + 12, cy - s + 12, cx + s - 12, cy + s - 12],
                   outline=(46, 125, 50), width=3)
    draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], fill=(46, 125, 50))
    # rising bars
    bx = x0 + int(w * 0.66)
    base = y0 + int(h * 0.82)
    for i, bh in enumerate((16, 30, 46, 64)):
        draw.rectangle([bx + i * 18, base - bh, bx + i * 18 + 12, base],
                       fill=(46, 125, 50))
    draw.line([(bx - 4, base - 8), (bx + 22, base - 34), (bx + 40, base - 50), (bx + 66, base - 72)],
              fill=(185, 28, 28), width=4)
    draw.polygon([(bx + 66, base - 72), (bx + 52, base - 70), (bx + 64, base - 58)],
                 fill=(185, 28, 28))


def ill_cyclone(draw, box):
    """Weather: cyclone spiral over the sea."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle(box, fill=(224, 232, 240))
    cx, cy = x0 + w // 2, y0 + int(h * 0.46)
    # spiral arms
    for start_r, end_r, col, wd in ((8, 62, (15, 42, 74), 7), (8, 48, (46, 125, 150), 5)):
        pts = []
        turns = 2.1
        steps = 90
        for i in range(steps + 1):
            t = i / steps
            ang = t * turns * 2 * math.pi
            r = start_r + (end_r - start_r) * t
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang) * 0.92))
        draw.line(pts, fill=col, width=wd)
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(15, 42, 74))
    # sea
    draw.rectangle([x0, y0 + int(h * 0.82), x1, y1], fill=(110, 168, 205))
    for i, wy in enumerate((0.87, 0.93)):
        yy = y0 + int(h * wy)
        draw.line([(x0 + 10, yy), (x1 - 10, yy)], fill=(255, 255, 255), width=3)
    # rain drops
    for dx, dy in ((-52, -58), (48, -66), (64, -34), (-64, -30)):
        draw.ellipse([cx + dx - 3, cy + dy - 6, cx + dx + 3, cy + dy + 6],
                     fill=(46, 125, 150))

# ---------------------------------------------------------------- composition

def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.rectangle([0, 168, W, 172], fill=RED)
    f_kick = font(SANS_BOLD, 25)
    draw_centered(d, W // 2, 24, "T H E   W O R L D   I N   O N E   D A Y",
                  f_kick, GOLD, tracking=2)
    f_date = font(SERIF, 58)
    draw_centered(d, W // 2, 62, "WEDNESDAY 18 NOVEMBER 2026", f_date, (255, 255, 255))
    d.line([(W // 2 - 330, 140), (W // 2 + 330, 140)], fill=GOLD, width=2)
    f_sub = font(SANS, 21)
    draw_centered(d, W // 2, 146, "Five stories that defined the day  —  from the Gulf to Manila to Shenzhen",
                  f_sub, (200, 214, 228))

    # --- lead story: Gulf on alert ---
    ill_gulf(d, (24, 196, 400, 454))
    d.rectangle([24, 196, 400, 454], outline=INK, width=2)
    tx = 424
    f_lkick = font(SANS_BOLD, 20)
    draw_tracked(d, (tx, 198), "GULF  •  US–IRAN", f_lkick, RED, tracking=1)
    f_lhead = font(SERIF, 45)
    d.text((tx, 226), "GULF ON ALERT", font=f_lhead, fill=INK)
    d.text((tx, 272), "DRONES DOWNED", font=f_lhead, fill=INK)
    f_lbody = font(SANS, 23)
    lead = ("Kuwait's air defences down hostile drones in the early "
            "hours of Wednesday; Bahrain sounds the all-clear; US jets "
            "hit an Iran missile site on Qeshm Island.")
    y = 330
    for line in wrap(d, lead, f_lbody, 1000 - tx - 8):
        d.text((tx, y), line, font=f_lbody, fill=INK)
        y += 30
    f_lfoot = font(SANS_BOLD, 19)
    d.text((tx, 428), "No casualties or damage reported",
           font=f_lfoot, fill=GRAY)

    # --- divider ---
    d.line([(24, 478), (1000, 478)], fill=RULE, width=2)

    # --- four stories, 2 x 2 grid ---
    stories = [
        ("ASIA  •  DIPLOMACY", "TRUMP & MARCOS",
         "The US president meets Ferdinand Marcos Jr. in Manila on "
         "Wednesday, then flies to Shenzhen for APEC; Putin meets "
         "Trump and Xi on Thursday.",
         ill_plane, (15, 42, 74)),
        ("TECH  •  MARKETS", "NVIDIA SOARS",
         "Quarterly revenue doubles to $115.8bn; the board says ousted "
         "chief Jensen Huang will not return; Anthropic prices its IPO today.",
         ill_chip, (46, 125, 50)),
        ("WEATHER  •  ASIA", "CYCLONE AKVAN",
         "The storm over the Bay of Bengal strengthens on Wednesday, "
         "with heavy rain and winds of 110 km/h on the coast; landfall "
         "is due on Friday.",
         ill_cyclone, (15, 90, 120)),
        ("ASIA  •  SUMMIT", "APEC OPENS",
         "Leaders gather in Shenzhen as the APEC summit opens on "
         "Wednesday; Trump, Xi and Putin hold their trilateral on Thursday.",
         ill_summit, (15, 42, 74)),
    ]
    f_ckick = font(SANS_BOLD, 18)
    f_chead = font(SERIF, 31)
    f_cbody = font(SANS, 20)
    cell_w, cell_h = 476, 236
    for i, (kick, head, body, ill, col) in enumerate(stories):
        cx0 = 24 + (i % 2) * (cell_w + 24)
        cy0 = 496 + (i // 2) * (cell_h + 16)
        # illustration, left
        ill(d, (cx0, cy0, cx0 + 168, cy0 + 168))
        d.rectangle([cx0, cy0, cx0 + 168, cy0 + 168], outline=INK, width=2)
        tx2 = cx0 + 184
        tw = cx0 + cell_w - tx2
        draw_tracked(d, (tx2, cy0 + 2), kick, f_ckick, col, tracking=1)
        d.text((tx2, cy0 + 28), head, font=f_chead, fill=INK)
        y = cy0 + 70
        for line in wrap(d, body, f_cbody, tw):
            d.text((tx2, y), line, font=f_cbody, fill=INK)
            y += 26

    # --- footer ---
    d.line([(24, 984), (1000, 984)], fill=RULE, width=2)
    f_foot = font(SANS, 16)
    draw_centered(d, W // 2, 992,
                  "Sources: Reuters, Associated Press, Al Jazeera, The Guardian  •  18 November 2026",
                  f_foot, GRAY)
    return img


if __name__ == "__main__":
    render().save("entry.png", "PNG")
    print("wrote entry.png")

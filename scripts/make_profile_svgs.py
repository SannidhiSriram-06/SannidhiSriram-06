"""Generate the animated SVGs embedded in the profile README.

Run daily by .github/workflows/update-profile.yml. The portrait is a static
input; the heatmap and stats card change with the contribution calendar.
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter, ImageOps

USER = "SannidhiSriram-06"
ROOT = Path(__file__).resolve().parent.parent
PHOTO = ROOT / "IMG_20261010_114152.jpg"
RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

CELL, STEP = 11, 14
LEVEL_COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
FRAME_BG, FRAME_BORDER, TEXT, MUTED, ACCENT = "#0d1117", "#30363d", "#c9d1d9", "#8b949e", "#58a6ff"


def fetch_days():
    html = requests.get(f"https://github.com/users/{USER}/contributions", timeout=30).text
    # Cells come row by row (all Sundays, then all Mondays), so sort by date to get weeks.
    days = sorted(
        BeautifulSoup(html, "html.parser").select("td.ContributionCalendar-day[data-date]"),
        key=lambda d: d["data-date"],
    )
    total = re.search(r"([\d,]+)\s+contributions\s+in the last year", html)
    return days, int(total.group(1).replace(",", "")) if total else 0


def window(width, height, title, body):
    """Fake terminal window: title bar with three dots, then the body."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="monospace">\n'
        f'  <rect width="{width}" height="{height}" rx="8" fill="{FRAME_BG}" stroke="{FRAME_BORDER}"/>\n'
        f'  <circle cx="18" cy="16" r="5" fill="#ff5f56"/><circle cx="34" cy="16" r="5" fill="#ffbd2e"/>'
        f'<circle cx="50" cy="16" r="5" fill="#27c93f"/>\n'
        f'  <text x="70" y="20" fill="{MUTED}" font-size="12">{title}</text>\n'
        f"  {body}\n</svg>\n"
    )


def heatmap_svg(days):
    first = date.fromisoformat(days[0]["data-date"])
    first_sunday = first - timedelta(days=(first.weekday() + 1) % 7)  # column 0 starts on a Sunday
    cells = []
    for day in days:
        d = date.fromisoformat(day["data-date"])
        x = (d - first_sunday).days // 7
        y = (d.weekday() + 1) % 7  # Sunday = row 0
        level = int(day.get("data-level", 0))
        begin = f"{(x + y) * 0.02:.2f}s"
        cells.append(
            f'<rect x="{x * STEP}" y="{y * STEP}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{LEVEL_COLORS[level]}" opacity="0">'
            f'<animate attributeName="opacity" from="0" to="1" begin="{begin}" dur="0.4s" fill="freeze"/>'
            f"</rect>"
        )
    grid_w, grid_h = 53 * STEP, 7 * STEP
    width, height = grid_w + 40, grid_h + 70
    return window(width, height, f"{USER} ~ contributions", f'<g transform="translate(20 46)">{"".join(cells)}</g>')


def stats_svg(days, total):
    levels = [int(d.get("data-level", 0)) for d in days]
    current = 0
    for level in reversed(levels[:-1] if levels and levels[-1] == 0 else levels):  # today may not be counted yet
        if level == 0:
            break
        current += 1
    longest = run = 0
    for level in levels:
        run = run + 1 if level else 0
        longest = max(longest, run)
    rows = [("total", f"{total:,} contributions (last year)"), ("streak", f"{current} days current"), ("best", f"{longest} days longest")]
    lines = [
        f'<text x="20" y="{50 + i * 26}" fill="{TEXT}" opacity="0">'
        f'<tspan fill="{ACCENT}">{key}</tspan>: {value}'
        f'<animate attributeName="opacity" from="0" to="1" begin="{i * 0.3:.1f}s" dur="0.5s" fill="freeze"/></text>'
        for i, (key, value) in enumerate(rows)
    ]
    return window(490, 50 + len(rows) * 26, f"{USER} ~ stats", "\n  ".join(lines))


def typed_svg(lines, cycle, path_width=490, font_size=14):
    """Text that reveals line by line once, or cycles through lines forever with cycle=True."""
    height = 20 + len(lines) * 24
    out = []
    n = len(lines)
    for i, text in enumerate(lines):
        text = text.replace("&", "&amp;")
        y = 24 + i * 24
        if cycle:
            s, e = i / n, (i + 1) / n
            anim = (
                f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="{s:.4f};{s + 0.02:.4f};{e - 0.05:.4f};{e:.4f}" '
                f'dur="{n * 2.5:.1f}s" repeatCount="indefinite"/>'
            )
            start_opacity = "0"
        else:
            anim = f'<animate attributeName="opacity" from="0" to="1" begin="{i * 0.6:.1f}s" dur="0.4s" fill="freeze"/>'
            start_opacity = "0"
        out.append(f'<text x="10" y="{y}" fill="{TEXT}" opacity="{start_opacity}">{text}{anim}</text>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{path_width}" height="{height}" viewBox="0 0 {path_width} {height}" '
        f'font-family="monospace" font-size="{font_size}">\n  ' + "\n  ".join(out) + "\n</svg>\n"
    )


def portrait_rows(cols=100):
    img = Image.open(PHOTO).convert("L")
    img = img.crop((0, 0, img.width, int(img.height * 0.9)))  # drop the phone's footer bar
    img = ImageOps.autocontrast(img, cutoff=2)  # widen the tonal range so features separate
    img = img.filter(ImageFilter.UnsharpMask(radius=4, percent=180, threshold=2))  # crisper edges
    rows = int(img.height / img.width * cols * 0.5)  # characters are ~2x taller than wide
    img = img.resize((cols, rows), Image.LANCZOS)
    return [
        "".join(RAMP[min(len(RAMP) - 1, (255 - img.getpixel((x, y))) * len(RAMP) // 256)] for x in range(cols))
        for y in range(rows)
    ]


def ascii_svg(cols=100):
    rows_text = portrait_rows(cols)
    rows = len(rows_text)
    font_w, font_h = 7, 14
    width, height = cols * font_w, rows * font_h
    lines = []
    for y, row in enumerate(rows_text):
        row = row.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        begin = f"{y * 0.05:.2f}s"
        lines.append(
            f'<text x="0" y="{(y + 1) * font_h}" xml:space="preserve" fill="{TEXT}" clip-path="url(#c{y})">{row}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{begin}" dur="0.01s" fill="freeze"/></text>'
        )
    clips = "".join(
        f'<clipPath id="c{y}"><rect x="0" y="{y * font_h}" width="0" height="{font_h}">'
        f'<animate attributeName="width" from="0" to="{width}" begin="{y * 0.05:.2f}s" dur="0.2s" fill="freeze"/>'
        f"</rect></clipPath>"
        for y in range(rows)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="monospace" font-size="12">\n'
        f"  <defs>{clips}</defs>\n  " + "\n  ".join(lines) + "\n</svg>\n"
    )


def info_card_svg():
    rows = [
        ("role", "Cloud & DevOps Engineer"),
        ("based", "Hyderabad, India"),
        ("stack", "AWS · Azure · Terraform · Docker · K8s"),
        ("cicd", "GitHub Actions · Jenkins · ArgoCD"),
        ("certs", "4× Oracle Cloud · AZ-900 · AI-900"),
        ("status", "Open to Cloud / DevOps / SRE roles"),
    ]
    lines = []
    for i, (key, value) in enumerate(rows):
        value = value.replace("&", "&amp;")
        lines.append(
            f'<text x="20" y="{50 + i * 26}" fill="{TEXT}" opacity="0">'
            f'<tspan fill="{ACCENT}">{key}</tspan>: {value}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{i * 0.3:.1f}s" dur="0.5s" fill="freeze"/></text>'
        )
    return window(490, 50 + len(rows) * 26, f"{USER} ~ neofetch", "\n  ".join(lines))


def main():
    out = ROOT / "assets"
    out.mkdir(exist_ok=True)
    days, total = fetch_days()
    (out / "contrib-heatmap.svg").write_text(heatmap_svg(days))
    (out / "stats-card.svg").write_text(stats_svg(days, total))
    (out / "avi-ascii.svg").write_text(ascii_svg())
    (out / "info-card.svg").write_text(info_card_svg())
    (out / "hero-typing.svg").write_text(typed_svg(
        ["Cloud & DevOps Engineer.", "I build AWS, Azure & Kubernetes platforms.", "CI/CD and GitOps that ship them."],
        cycle=False, path_width=520,
    ))
    (out / "intro-typing.svg").write_text(typed_svg(
        ["> Cloud & DevOps Engineer", "> AWS · Azure · Terraform", "> Kubernetes · GitOps · ArgoCD", "> Open to SRE roles"],
        cycle=True, path_width=420,
    ))
    print("wrote SVGs to", out, file=sys.stderr)


if __name__ == "__main__":
    main()

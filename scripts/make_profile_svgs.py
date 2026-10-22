"""Generate the animated SVGs embedded in the profile README.

Run daily by .github/workflows/update-profile.yml. The portrait and info card
are static inputs; only the contribution heatmap changes between runs.
"""
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from PIL import Image

USER = "SannidhiSriram-06"
ROOT = Path(__file__).resolve().parent.parent
PHOTO = ROOT / "IMG_20261010_114152.jpg"
RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

CELL, GAP, STEP = 11, 3, 14
LEVEL_COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]


def heatmap_svg():
    html = requests.get(f"https://github.com/users/{USER}/contributions", timeout=30).text
    days = BeautifulSoup(html, "html.parser").select("td.ContributionCalendar-day")
    # shortcut: no per-cell tooltips, the contribution count is only in the header, upgrade if needed
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)][-53:]
    width, height = 53 * STEP, 7 * STEP + 4
    cells = []
    for x, week in enumerate(weeks):
        for y, day in enumerate(week):
            level = int(day.get("data-level", 0))
            begin = f"{(x + y) * 0.02:.2f}s"
            cells.append(
                f'<rect x="{x * STEP}" y="{y * STEP}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{LEVEL_COLORS[level]}" opacity="0">'
                f'<animate attributeName="opacity" from="0" to="1" begin="{begin}" dur="0.4s" fill="freeze"/>'
                f"</rect>"
            )
    body = "\n  ".join(cells)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        f"  {body}\n</svg>\n"
    )


def ascii_svg(cols=100):
    img = Image.open(PHOTO).convert("L")
    rows = int(img.height / img.width * cols * 0.5)  # characters are ~2x taller than wide
    img = img.resize((cols, rows))
    font_w, font_h = 7, 14
    width, height = cols * font_w, rows * font_h
    lines = []
    for y in range(rows):
        row = "".join(RAMP[min(len(RAMP) - 1, (255 - img.getpixel((x, y))) * len(RAMP) // 256)] for x in range(cols))
        row = row.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        begin = f"{y * 0.05:.2f}s"
        lines.append(
            f'<text x="0" y="{(y + 1) * font_h}" xml:space="preserve" fill="#c9d1d9" clip-path="url(#c{y})">{row}'
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
        ("ai", "CrewAI · Groq · Azure OpenAI"),
        ("certs", "4× Oracle Cloud · AZ-900 · AI-900"),
        ("status", "Open to Cloud / DevOps / SRE roles"),
    ]
    width, height = 490, 40 + len(rows) * 26
    lines = []
    for i, (key, value) in enumerate(rows):
        y = 40 + i * 26
        begin = f"{i * 0.3:.1f}s"
        value = value.replace("&", "&amp;")
        lines.append(
            f'<text x="20" y="{y}" fill="#c9d1d9" opacity="0">'
            f'<tspan fill="#58a6ff">{key}</tspan>: {value}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{begin}" dur="0.5s" fill="freeze"/></text>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="monospace" font-size="14">\n'
        f'  <rect width="{width}" height="{height}" rx="8" fill="#0d1117" stroke="#30363d"/>\n'
        f'  <text x="20" y="24" fill="#8b949e">sannidhi@cloud ~ neofetch</text>\n  '
        + "\n  ".join(lines)
        + "\n</svg>\n"
    )


def main():
    out = ROOT / "assets"
    out.mkdir(exist_ok=True)
    (out / "contrib-heatmap.svg").write_text(heatmap_svg())
    (out / "avi-ascii.svg").write_text(ascii_svg())
    (out / "info-card.svg").write_text(info_card_svg())
    print("wrote SVGs to", out, file=sys.stderr)


if __name__ == "__main__":
    main()

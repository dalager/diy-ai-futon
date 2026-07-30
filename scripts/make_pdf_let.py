"""Generér en samlet PDF for LET-varianten:

    1. FreeCAD-renderinger (cad/screenshots/*.png) i toppen
    2. sengebund_let.md
    3. BOM_let.md

Markdown -> HTML (python-markdown, GFM-tabeller + fenced code) -> PDF (WeasyPrint).
Kræver pakkerne `markdown` og `weasyprint`. De ligger i pyenv-miljøet 3.12.3:

    ~/.pyenv/versions/3.12.3/bin/python scripts/make_pdf_let.py

Output: cad/seng_let_dokumentation.pdf
"""

import os
import sys

try:
    import markdown
    from weasyprint import HTML, CSS
except ModuleNotFoundError as e:  # pragma: no cover - miljø-hjælp
    sys.exit(
        f"Mangler pakke: {e.name}. Kør scriptet med et python der har "
        "'markdown' og 'weasyprint', fx:\n"
        "    ~/.pyenv/versions/3.12.3/bin/python scripts/make_pdf_let.py"
    )

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "cad", "screenshots")
OUT = os.path.join(ROOT, "cad", "seng_let_dokumentation.pdf")

DOC_TITLE = "Christians Sengebund"
DOC_SUBTITLE = "Futon 180 × 200 cm · ubehandlet fyr/gran · ben af afskær ♻️"

# Renderinger i toppen (fil, billedtekst). Rækkefølge = visningsrækkefølge.
RENDERINGS = [
    ("seng_let_01_iso.png", "Isometrisk"),
    ("seng_let_05_dimetrisk.png", "Dimetrisk"),
    ("seng_let_02_langside.png", "Langside (opstalt)"),
    ("seng_let_03_gavl.png", "Gavl (ende)"),
    ("seng_let_04_plan.png", "Plan (ovenfra)"),
    ("seng_let_07_understel.png", "Understel (lameller skjult)"),
    ("seng_let_06_detalje_hjoerne.png", "Hjørnedetalje"),
    ("seng_let_08_forsaenkning.png", "Ben m. de 4 bolthuller"),
]

MD_FILES = [
    ("sengebund_let.md", "Sengebund LET"),
    ("BOM_let.md", "Materialeliste (BOM)"),
]

# Tegninger (SVG) - én pr. side, bagest i dokumentet.
PLANS = [
    ("seng_let_tegning.svg", "Tegning — opstalt og plan"),
    ("seng_let_boreplan.svg", "Boreplan — bolte og skruer"),
    ("seng_let_liste_boreplan.svg", "Boreplan — støttelistens lamelhuller"),
    ("seng_let_drager_boreplan.svg", "Boreplan — midterdrager → endestykke (vinkelbeslag)"),
]

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]


def md_to_html(rel_path):
    with open(os.path.join(ROOT, rel_path), encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def renderings_html():
    figs = []
    for fn, caption in RENDERINGS:
        src = os.path.join(SHOTS, fn)
        if not os.path.exists(src):
            print(f"  ! mangler rendering: {src}", file=sys.stderr)
            continue
        figs.append(
            f'<figure class="shot"><img src="{src}" alt="{caption}"/>'
            f'<figcaption>{caption}</figcaption></figure>'
        )
    return (
        '<section class="renderings">'
        '<h2 class="section-title">FreeCAD-renderinger</h2>'
        f'<div class="grid">{"".join(figs)}</div>'
        "</section>"
    )


def plans_html():
    pages = []
    for fn, caption in PLANS:
        src = os.path.join(ROOT, "cad", fn)
        if not os.path.exists(src):
            print(f"  ! mangler tegning: {src}", file=sys.stderr)
            continue
        pages.append(
            f'<section class="plan"><h2 class="section-title">{caption}</h2>'
            f'<img src="{src}" alt="{caption}"/>'
            f'<div class="plan-src">{fn}</div></section>'
        )
    return "".join(pages)


STYLESHEET = """
@page {
    size: A4;
    margin: 16mm 15mm 18mm 15mm;
    @bottom-center {
        content: "Sengebund LET · side " counter(page) " / " counter(pages);
        font: 8pt "DejaVu Sans", sans-serif;
        color: #888;
    }
}
* { box-sizing: border-box; }
body {
    font-family: "DejaVu Sans", "Noto Color Emoji", sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
}

/* ---- title block ---- */
.cover-title { font-size: 24pt; font-weight: bold; margin: 0 0 2mm 0; }
.cover-sub   { font-size: 11pt; color: #555; margin: 0 0 6mm 0; }

/* ---- renderings grid ---- */
.section-title {
    font-size: 13pt; margin: 0 0 3mm 0; padding-bottom: 1.5mm;
    border-bottom: 2px solid #b99763; color: #6b4f2a;
}
.grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 4mm;
}
figure.shot { margin: 0; break-inside: avoid; }
figure.shot img {
    width: 100%; height: auto; border: 1px solid #ccc;
    background: #fff; border-radius: 2px;
}
figure.shot figcaption {
    font-size: 8.5pt; color: #555; text-align: center; margin-top: 1mm;
}

/* ---- tegninger (SVG), én pr. side ---- */
section.plan { break-before: page; }
section.plan img {
    display: block; width: 100%; height: auto;
    border: 1px solid #ddd; background: #fff; border-radius: 2px;
}
.plan-src {
    font-family: "DejaVu Sans Mono", monospace; font-size: 8pt;
    color: #999; text-align: right; margin-top: 1.5mm;
}

/* ---- document sections ---- */
.doc { break-before: page; }
h1 { font-size: 17pt; color: #6b4f2a; margin: 0 0 3mm 0;
     border-bottom: 2px solid #b99763; padding-bottom: 1.5mm; }
h2 { font-size: 13pt; color: #333; margin: 6mm 0 2mm 0; }
h3 { font-size: 11pt; color: #444; margin: 4mm 0 1.5mm 0; }
p { margin: 1.8mm 0; }
a { color: #1a5f9c; text-decoration: none; }

/* ---- tables ---- */
table {
    border-collapse: collapse; width: 100%; margin: 2.5mm 0;
    font-size: 9pt; break-inside: avoid;
}
th, td {
    border: 1px solid #ccc; padding: 1.4mm 2mm; text-align: left;
    vertical-align: top; word-break: break-word;
}
th { background: #efe7d3; color: #4a3a1e; font-weight: bold; }
tr:nth-child(even) td { background: #faf8f2; }

/* ---- code / ASCII art ---- */
pre {
    font-family: "DejaVu Sans Mono", "Noto Color Emoji", monospace;
    font-size: 8pt; line-height: 1.25;
    background: #f6f4ee; border: 1px solid #e0dccf; border-radius: 3px;
    padding: 2.5mm 3mm; white-space: pre; overflow: visible;
    break-inside: avoid;
}
code {
    font-family: "DejaVu Sans Mono", monospace; font-size: 9pt;
    background: #f0ede4; padding: 0 1mm; border-radius: 2px;
}
pre code { background: none; padding: 0; font-size: inherit; }
ul, ol { margin: 1.8mm 0 1.8mm 5mm; padding: 0; }
li { margin: 0.8mm 0; }
strong { color: #111; }
"""


def build_html():
    parts = [
        f'<div class="cover-title">{DOC_TITLE}</div>',
        f'<div class="cover-sub">{DOC_SUBTITLE}</div>',
        renderings_html(),
    ]
    for rel_path, _label in MD_FILES:
        parts.append(f'<div class="doc">{md_to_html(rel_path)}</div>')
    parts.append(plans_html())
    return (
        "<!doctype html><html><head><meta charset='utf-8'></head>"
        f"<body>{''.join(parts)}</body></html>"
    )


def main():
    html = build_html()
    HTML(string=html, base_url=ROOT).write_pdf(OUT, stylesheets=[CSS(string=STYLESHEET)])
    size_kb = os.path.getsize(OUT) / 1024
    print(f"SAVED {OUT} ({size_kb:.0f} kB)")


if __name__ == "__main__":
    main()

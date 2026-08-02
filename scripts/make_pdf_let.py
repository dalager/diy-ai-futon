"""Generér byggevejledningen som PDF (den udleveringsklare version):

    1. byggevejledning.md (renderinger ligger inline i markdown'en)
    2. de fire målsatte SVG-tegninger, én pr. side, bagest

Markdown -> HTML (python-markdown, GFM-tabeller + fenced code) -> PDF (WeasyPrint).
Kræver pakkerne `markdown` og `weasyprint`. De ligger i pyenv-miljøet 3.12.3:

    ~/.pyenv/versions/3.12.3/bin/python scripts/make_pdf_let.py

Output: docs/dokumentation.pdf

designnoter.md er arbejdsnote (konstruktionsvalg, statik, indkøb) og kommer *ikke* med i
PDF'en. Tidligere blev PDF'en bygget af sengebund_let.md + BOM_let.md, som overlappede
hinanden og gjorde dokumentet dobbelt så langt som nødvendigt.
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
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(DOCS, "dokumentation.pdf")

GUIDE = "byggevejledning.md"

DOC_SUBTITLE = "Byggevejledning · ubehandlet fyr/gran · ben af afskær ♻️"

# Tegninger (SVG) - én pr. side, bagest i dokumentet (afsnit 8 henviser til dem).
PLANS = [
    ("tegning.svg", "Tegning — mål, plan og opstalt"),
    ("boreplan.svg", "Boreplan — bolte og skruer"),
    ("liste_boreplan.svg", "Boreplan — støttelistens lamelhuller"),
    ("drager_boreplan.svg", "Boreplan — midterdrager → endestykke (vinkelbeslag)"),
]

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]


def md_to_html(rel_path):
    with open(os.path.join(ROOT, rel_path), encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text, extensions=MD_EXTENSIONS)
    # Undertitel lige under dokumentets h1 (forsiden).
    return html.replace("</h1>", f'</h1><p class="cover-sub">{DOC_SUBTITLE}</p>', 1)


def plans_html():
    pages = []
    for fn, caption in PLANS:
        src = os.path.join(DOCS, fn)
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
        content: "Sengebund til futon 180 × 200 cm · side " counter(page) " / " counter(pages);
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

/* ---- forside ---- */
h1 {
    font-size: 23pt; font-weight: bold; color: #6b4f2a;
    margin: 0 0 1.5mm 0; padding-bottom: 0; border: 0;
}
.cover-sub { font-size: 11pt; color: #555; margin: 0 0 5mm 0; }

/* ---- billedrækker (renderinger inline i markdown) ---- */
.figrow {
    display: grid; grid-template-columns: 1fr 1fr; gap: 4mm;
    margin: 3mm 0; break-inside: avoid;
}
.figrow.one { grid-template-columns: 62% ; justify-content: center; }
.figrow figure { margin: 0; break-inside: avoid; }
.figrow img {
    width: 100%; height: auto; border: 1px solid #ccc;
    background: #fff; border-radius: 2px;
}
.figrow figcaption {
    font-size: 8.5pt; color: #555; text-align: center; margin-top: 1mm;
}

/* ---- tegninger (SVG), én pr. side ---- */
section.plan { break-before: page; }
.section-title {
    font-size: 13pt; margin: 0 0 3mm 0; padding-bottom: 1.5mm;
    border-bottom: 2px solid #b99763; color: #6b4f2a;
}
section.plan img {
    display: block; width: 100%; height: auto;
    border: 1px solid #ddd; background: #fff; border-radius: 2px;
}
.plan-src {
    font-family: "DejaVu Sans Mono", monospace; font-size: 8pt;
    color: #999; text-align: right; margin-top: 1.5mm;
}

/* ---- afsnit ---- */
h2 {
    font-size: 14pt; color: #6b4f2a; margin: 7mm 0 2.5mm 0;
    padding-bottom: 1.5mm; border-bottom: 2px solid #b99763;
    break-after: avoid;
}
h2.newpage { break-before: page; margin-top: 0; }
h3 {
    font-size: 11.5pt; color: #333; margin: 5mm 0 1.5mm 0;
    break-after: avoid;
}
h3.newpage { break-before: page; margin-top: 0; }
p { margin: 1.8mm 0; }
a { color: #1a5f9c; text-decoration: none; }
.colophon {
    margin-top: 7mm; padding-top: 2mm; border-top: 1px solid #ddd;
    font-size: 8.5pt; color: #777;
}

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
    parts = [md_to_html(GUIDE), plans_html()]
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

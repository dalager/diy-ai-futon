"""Generate the ledger (stoetteliste) drilling sheet for the slat screws.

    python3 scripts/make_ledger_drill_let.py  ->  cad/seng_let_liste_boreplan.svg

The 34 lamel holes are drilled into the ledger's THIN 21 mm underside, so this
sheet gives their positions measured from one end of the 1770 mm ledger:

  A  Listens underside, fuld laengde i to halvdele - alle 34 huller
  B  Snit gennem samlingen (2:1) - hullets placering i de 21 mm
  C  Maalskema - alle 34 afstande fra listens venstre ende
  D  De 6 vandrette liste->vange huller i listens inderside

Geometry mirrors build_bed_let.py; keep the parameters below in sync with it.
"""

import os

_CAD = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cad")

# ---- parameters (mirror build_bed_let.py) ----------------------------------
rail_t = 45.0
leg = 70.0
outer_len = 2000.0
ledger_t, ledger_h = 21.0, 45.0
slat_t = 45.0
n_slats = 17
pair_dx = 12.0                                     # slat holes +/- from centre

led_x0 = rail_t + leg                              # 115  (listens venstre ende, absolut)
led_len = (outer_len - rail_t - leg) - led_x0      # 1770
pitch = (led_len - slat_t) / (n_slats - 1)         # 107.8125

# hole centres relative to the ledger's own left end
xc = [i * pitch + slat_t / 2.0 for i in range(n_slats)]
holes = [(c - pair_dx, c + pair_dx) for c in xc]
ledger_screws_rel = [x - led_x0 for x in (190, 520, 850, 1180, 1510, 1840)]

svg = []


def rect(x, y, w, h, fill="none", stroke="#222", sw=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(x1, y1, x2, y2, stroke="#222", sw=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
               f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def circ(x, y, r, fill="#fff", stroke="#c0392b", sw=1.3, cross=True):
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" '
               f'stroke="{stroke}" stroke-width="{sw}"/>')
    if cross:
        line(x - r - 2, y, x + r + 2, y, "#c0392b", 0.6)
        line(x, y - r - 2, x, y + r + 2, "#c0392b", 0.6)


def text(x, y, s, size=13, anchor="middle", fill="#111", weight="normal", family=None):
    fam = family or "Helvetica,Arial,sans-serif"
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" '
               f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
               f'fill="{fill}">{s}</text>')


def tick(x, y):
    line(x - 3, y + 3, x + 3, y - 3, "#c0392b", 1.2)


def dim_h(x1, x2, y, label, above=True, size=11):
    line(x1, y, x2, y, "#c0392b", 0.8)
    tick(x1, y); tick(x2, y)
    text((x1 + x2) / 2, y - 5 if above else y + 14, label, size, "middle", "#c0392b")


def dim_v(y1, y2, x, label, left=True, size=11):
    line(x, y1, x, y2, "#c0392b", 0.8)
    tick(x, y1); tick(x, y2)
    text(x - 6 if left else x + 6, (y1 + y2) / 2 + 4, label,
         size, "end" if left else "start", "#c0392b")


def mm(v):
    """1 decimal, komma som decimaltegn, uden overfloedig ,0"""
    s = f"{v:.1f}".replace(".", ",")
    return s[:-2] if s.endswith(",0") else s


C_LEDGER, C_SLAT, C_RAIL = "#c9b487", "#efe7d3", "#d8c9a8"

# ============================================================= Panel A
# listens underside i to halvdele; laengden i skala, de 21 mm overdrevet
sA = 0.95
split = led_len / 2.0                    # 885
band_h = 34.0                            # px, IKKE i skala (21 mm)
AX = 140


def strip(y_top, off, label):
    """Draw one half of the ledger underside starting at offset `off` mm."""
    w = split * sA
    rect(AX, y_top, w, band_h, C_LEDGER, "#222", 1.0)
    text(AX - 8, y_top + band_h / 2 + 4, label, 11, "end", "#555")
    ymid = y_top + band_h / 2
    for i, (h1, h2) in enumerate(holes):
        for h in (h1, h2):
            if off <= h < off + split:
                circ(AX + (h - off) * sA, ymid, 4.5)
        c = xc[i]
        if off - 20 <= c < off + split + 20:
            text(AX + (c - off) * sA, y_top + band_h + 15, f"L{i}", 10, "middle", "#555")
    return ymid


text(AX - 10, 92, "A · Støttelistens UNDERSIDE (21 × 1770) — 34 lamelhuller, Ø5 gennemgang",
     15, "start", "#111", "bold")
text(AX - 10, 112, "Længden er i skala ca. 1:1 · de 21 mm er overdrevet i højden. "
     "Begge lister bores ens.", 11, "start", "#555")

yA1 = 185
dim_h(AX + xc[0] * sA, AX + xc[1] * sA, yA1 - 46, f"{mm(pitch)}  (c/c lameller)")
dim_h(AX + holes[0][0] * sA, AX + holes[0][1] * sA, yA1 - 20, "24")
strip(yA1, 0.0, "0 →")
dim_h(AX, AX + holes[0][0] * sA, yA1 + band_h + 32, mm(holes[0][0]), above=False)

yA2 = 320
strip(yA2, split, "885 →")
_last = holes[-1][1]
dim_h(AX + (_last - split) * sA, AX + split * sA, yA2 + band_h + 32,
      mm(led_len - _last), above=False)
text(AX + split * sA + 10, yA2 + band_h / 2 + 4, "← 1770", 11, "start", "#555")
text(AX, yA2 + band_h + 78, "Lamelhullerne ligger symmetrisk om listens midte (10,5 mm inde i begge ender), "
     "men vange-hullerne i panel D gør IKKE —", 11, "start", "#333")
text(AX, yA2 + band_h + 95, "vend derfor begge lister samme vej: 0-enden mod samme gavl.",
     11, "start", "#333")

# ============================================================= Panel B
# tvaersnit i Y-Z: y = 0 ved vangens yderside, z = 200 ved rammens underkant
sB = 2.4
BX0, BZ0 = 215, 800                       # px for y=0 og z=200
text(130, 512, "B · Snit gennem samlingen (ca. 2,5:1) — hvor i de 21 mm sidder hullet",
     15, "start", "#111", "bold")


def pY(y):
    return BX0 + y * sB


def pZ(z):
    return BZ0 - (z - 200.0) * sB


# vange 45 x 95 (y 0..45, z 200..295)
rect(pY(0), pZ(295), 45 * sB, 95 * sB, C_RAIL, "#222", 1.0)
text(pY(22.5), pZ(268), "vange", 11, "middle", "#333")
text(pY(22.5), pZ(255), "45 × 95", 10, "middle", "#777")
# stoetteliste 21 x 45 (y 45..66, z 205..250)
rect(pY(45), pZ(250), ledger_t * sB, ledger_h * sB, C_LEDGER, "#222", 1.2)
# lamel 45 x 45 hviler paa listens overkant (y 45.., z 250..295)
rect(pY(45), pZ(295), 75 * sB, 45 * sB, C_SLAT, "#555", 1.0)
text(pY(70), pZ(276), "lamel — 45 mm høj,", 11, "start", "#333")
text(pY(70), pZ(264), "løber på tværs →", 11, "start", "#333")
# gulvlinje-kote
line(pY(-14), pZ(200), pY(100), pZ(200), "#bbb", 1.0, dash="4,3")
text(pY(102), pZ(200) + 4, "kote 200 (rammens underkant)", 10, "start", "#999")
line(pY(-14), pZ(295), pY(-2), pZ(295), "#bbb", 1.0)
text(pY(-16), pZ(295) + 4, "295 = soveflade", 10, "end", "#999")

hc = pY(45 + ledger_t / 2.0)              # hulcenterlinje, midt i de 21 mm
# Ø5 gennem listens 45 mm hoejde
rect(hc - 2.5 * sB, pZ(250), 5 * sB, 45 * sB, "#fff", "#c0392b", 1.3)
# Ø3 pilot 25 mm op i lamellen
rect(hc - 1.5 * sB, pZ(265), 3 * sB, 15 * sB, "#fff", "#c0392b", 1.2, dash="4,3")
# Ø10 forsaenkning i listens underside
line(hc - 5 * sB, pZ(205), hc - 2.5 * sB, pZ(205) - 11, "#c0392b", 1.4)
line(hc + 5 * sB, pZ(205), hc + 2.5 * sB, pZ(205) - 11, "#c0392b", 1.4)

dim_h(pY(45), hc, pZ(205) + 40, "10,5", above=False)
dim_h(hc, pY(66), pZ(205) + 40, "10,5", above=False)
dim_h(pY(45), pY(66), pZ(205) + 64, "21 (listens tykkelse)", above=False)
dim_v(pZ(250), pZ(205), pY(45) - 30, "45")
dim_v(pZ(265), pZ(250), pY(132), "15", left=False)
text(pY(132), pZ(280), "Ø3 pilot 20 mm", 10, "start", "#c0392b")
text(hc + 5 * sB + 8, pZ(228), "Ø5", 12, "start", "#c0392b", "bold")
text(hc, pZ(205) + 22, "Ø10 forsænk", 10, "middle", "#c0392b")
text(pY(75), pZ(222), "støtteliste 21 × 45", 11, "start", "#333")

TX = 640
text(TX, 545, "Skruen er 4,5 × 60 spånskrue, LODRET op:", 12, "start", "#111", "bold")
for i, s in enumerate([
        "45 mm gennem listens HØJDE + 15 mm op i lamellen = 60.",
        "Den bryder altså ikke ud i sovefladen ved kote 295.",
        "",
        "Hullet ligger midt i de 21 mm → 8 mm træ til hver side af",
        "et Ø5-hul. Bor derfor LODRET (borelære/søjleboremaskine):",
        "en skæv Ø5 gennem 45 mm bryder ud i listens side.",
        "",
        "Bor listen FØR den skrues på vangen — de forborede huller",
        "er selv afstands-jiggen, der placerer lamellerne.",
        "",
        "Lamellen HVILER på listens overkant, så skruen bærer ingen",
        "vægt; den er ren lås mod at lamellen løfter sig."]):
    text(TX, 570 + i * 19, s, 11.5, "start", "#333")

# ============================================================= Panel D
DX, DY = 140, 930
text(DX - 10, DY - 22, "D · Støttelistens INDERSIDE (45 × 1770) — de 6 vandrette huller til vangen",
     15, "start", "#111", "bold")
sD = 0.50
rect(DX, DY, led_len * sD, ledger_h * sD, C_LEDGER, "#222", 1.0)
for x in ledger_screws_rel:
    circ(DX + x * sD, DY + ledger_h * sD / 2, 4)
dim_h(DX, DX + ledger_screws_rel[0] * sD, DY + ledger_h * sD + 20, mm(ledger_screws_rel[0]), above=False)
dim_h(DX + ledger_screws_rel[0] * sD, DX + ledger_screws_rel[1] * sD,
      DY + ledger_h * sD + 20, "330 (c/c)", above=False)
dim_h(DX, DX + led_len * sD, DY - 10, f"{led_len:.0f} (liste)")
dim_v(DY, DY + ledger_h * sD, DX - 16, "45")
text(DX, DY + ledger_h * sD + 54,
     f"Spånskrue 4,5 × 50 (IKKE 60/70 — 21 + 45 = 66 mm stak). Ø5 gennem listen, Ø3 i vangen, "
     f"Ø10 forsænk. Højde: midt i de 45 = 22,5 mm.", 11, "start", "#333")
_clash, _ca, _cb = min((abs(a - b), a, b)
                       for a in ledger_screws_rel for hp in holes for b in hp)
text(DX, DY + ledger_h * sD + 72,
     f"⚠ Vange-hullet ved {mm(_ca)} mm og lamelhullet ved {mm(_cb)} mm ligger kun "
     f"{mm(_clash)} mm fra hinanden — ca. {mm(_clash - 5)} mm træ mellem de to Ø5-huller. "
     f"Bor begge, før du skruer.", 11, "start", "#c0392b")

# ============================================================= Panel C
CX, CY = 140, 1085
text(CX - 10, CY - 22, "C · Målskema — afstand fra listens VENSTRE ende (mm)",
     15, "start", "#111", "bold")
text(CX - 10, CY - 4, "Mål alle 34 fra samme ende med båndmål — step ikke 107,8 af 16 gange, "
     "fejlen hober sig op. Afrunding til hele mm er rigeligt.", 11, "start", "#555")

MONO = "DejaVu Sans Mono,Menlo,Consolas,monospace"
col_w, row_h = 300, 23
rows = 9                                   # 9 + 8
for c in range(2):
    x0 = CX + c * (col_w + 60)
    y0 = CY + 24
    rect(x0, y0, col_w, row_h * (rows + 1), "#fbf8f1", "#c0392b", 1.0)
    line(x0, y0 + row_h, x0 + col_w, y0 + row_h, "#c0392b", 1.0)
    for hx, lab in ((x0 + 46, "lamel"), (x0 + 165, "hul 1"), (x0 + 260, "hul 2")):
        text(hx, y0 + 16, lab, 11.5, "middle", "#111", "bold")
    for r in range(rows):
        i = c * rows + r
        if i >= n_slats:
            break
        yy = y0 + row_h * (r + 1) + 16
        if r % 2:
            rect(x0 + 1, yy - 17, col_w - 2, row_h, "#f2ead8", "none", 0)
        text(x0 + 46, yy, f"L{i}", 11.5, "middle", "#333", family=MONO)
        text(x0 + 165, yy, f"{holes[i][0]:.0f}", 11.5, "middle", "#111", "bold", family=MONO)
        text(x0 + 260, yy, f"{holes[i][1]:.0f}", 11.5, "middle", "#111", "bold", family=MONO)

_ty = CY + 24 + row_h * (rows + 1) + 28
text(CX, _ty, f"34 huller pr. liste · 2 lister = 68 huller i alt. Parret sidder 24 mm fra hinanden, "
     f"centreret på lamellens 45 mm fod.", 11.5, "start", "#333")
text(CX, _ty + 18, f"Kontrolmål: første hul {mm(holes[0][0])} og sidste hul {mm(holes[-1][1])} — "
     f"begge {mm(holes[0][0])} mm fra hver sin ende. Rammer det ikke, er listen skåret forkert "
     f"(skal være {led_len:.0f} mm).", 11.5, "start", "#333")
text(CX, _ty + 36, f"Midterste lamel (L8) sidder præcis på {xc[8]:.0f} mm = listens midte.",
     11.5, "start", "#333")

W, H = 1120, 1460
out = os.path.join(_CAD, "seng_let_liste_boreplan.svg")
body = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>',
        f'<text x="{W/2}" y="42" font-family="Helvetica,Arial,sans-serif" font-size="21" '
        f'font-weight="bold" text-anchor="middle" fill="#111">'
        f'Støtteliste — boreplan for lamelhuller (2 stk, ens · mål i mm)</text>']
body += svg
body.append('</svg>')
with open(out, "w") as f:
    f.write("\n".join(body))
print("SAVED", out, W, "x", H)
print(f"pitch={pitch:.4f} led_len={led_len:.0f} foerste={holes[0][0]:.2f} sidste={holes[-1][1]:.2f}")

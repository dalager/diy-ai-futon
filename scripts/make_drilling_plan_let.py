"""Generate a dimensioned drilling plan (SVG) for the screw holes.

    python3 scripts/make_drilling_plan.py  ->  cad/seng_boreplan.svg

Three detail panels:
  A  Lamelhuller (plan)        - slat->ledger holes, pitch & pair spacing
  B  Stoetteliste -> vange     - ledger->rail holes along the length
  C  Hjoerne (gavl-snit)       - frame->leg holes and their heights
"""

import os

_CAD = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cad")

# ---- parameters (mirror build_bed.py) --------------------------------------
slat_t, slat_h = 45.0, 45.0
gap = 62.8
pitch = 107.8
ledger_t, ledger_h = 21.0, 45.0
clearance = 200.0
z_vange = (clearance + 30.0, clearance + 75.0)   # vange bolt heights (rail=95)
z_ende = (clearance + 15.0, clearance + 50.0)    # endestykke bolts (below the slats)
ledger_screws_x = [190, 520, 850, 1180, 1510, 1840]
led_start = 115.0
pair_dx = 12.0                    # slat holes +/- from centre

svg = []


def rect(x, y, w, h, fill="none", stroke="#222", sw=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(x1, y1, x2, y2, stroke="#222", sw=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
               f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def circ(x, y, r, fill="#fff", stroke="#c0392b", sw=1.3):
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" '
               f'stroke="{stroke}" stroke-width="{sw}"/>')
    line(x - r - 2, y, x + r + 2, y, "#c0392b", 0.6)
    line(x, y - r - 2, x, y + r + 2, "#c0392b", 0.6)


def text(x, y, s, size=13, anchor="middle", fill="#111", weight="normal"):
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica,Arial,sans-serif" '
               f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
               f'fill="{fill}">{s}</text>')


def tick(x, y):
    line(x - 3, y + 3, x + 3, y - 3, "#c0392b", 1.2)


def dim_h(x1, x2, y, label, above=True):
    line(x1, y, x2, y, "#c0392b", 0.8)
    tick(x1, y); tick(x2, y)
    text((x1 + x2) / 2, y - 5 if above else y + 14, label, 12, "middle", "#c0392b")


def dim_v(y1, y2, x, label, left=True):
    line(x, y1, x, y2, "#c0392b", 0.8)
    tick(x, y1); tick(x, y2)
    text(x - 6 if left else x + 6, (y1 + y2) / 2 + 4, label,
         12, "end" if left else "start", "#c0392b")


C_SLAT, C_LEDGER, C_LEG, C_RAIL = "#efe7d3", "#c9b487", "#b99763", "#d8c9a8"

# ============================================================= Panel A
sa = 0.85
ax, ay = 130, 150
text(ax, ay - 40, "A · Lamelhuller — plan (op gennem støttelisten)", 15, "start", "#111", "bold")
slat_top_y = ay
slat_len = 150
led_y = ay + 78
led_h_px = ledger_t * sa
cx = [ax + 70 + i * pitch * sa for i in range(3)]
# ledger band behind
rect(ax, led_y, (cx[2] - ax) + 70, led_h_px, C_LEDGER, "#222", 0.7)
text(ax + 6, led_y + led_h_px + 16, f"liste {ledger_t:.0f}", 11, "start", "#555")  # kort, ellers dækker lamel 0 den
# slats + holes
for i, x in enumerate(cx):
    rect(x - slat_t * sa / 2, slat_top_y, slat_t * sa, slat_len, C_SLAT, "#555", 0.8)
    for dx in (-pair_dx, pair_dx):
        circ(x + dx * sa, led_y + led_h_px / 2, 4)
    text(x, slat_top_y + slat_len + 16, f"lamel {i}", 11, "middle", "#555")
# dims
dim_h(cx[0], cx[1], slat_top_y - 12, f"{pitch:.0f}  (c/c lameller)")
dim_h(cx[1] - pair_dx * sa, cx[1] + pair_dx * sa, led_y + led_h_px + 34, "24", above=False)
dim_h(cx[2] - slat_t * sa / 2, cx[2] + slat_t * sa / 2, slat_top_y - 12, "45")
dim_h(cx[1] + slat_t * sa / 2, cx[2] - slat_t * sa / 2, slat_top_y + slat_len + 34, f"{gap:.0f}", above=False)
text(ax, ay + 210, "2 spånskruer 4,5 × 60 pr. ende — lodret gennem listens 45 mm HØJDE + 15 mm op i lamellen.",
     11, "start", "#333")
text(ax, ay + 227, "Ø5 GENNEMGANG i listen (= afstands-jig) · Ø3 pilot 20 mm i lamellen · Ø10 forsænk under listen.",
     11, "start", "#c0392b")

# ============================================================= Bordiametre (legende)
lx, ly = 690, 105
LEGEND_H = 398
rect(lx, ly, 345, LEGEND_H, "#fbf8f1", "#c0392b", 1.0)
text(lx + 16, ly + 24, "BORDIAMETRE — fyr/gran, spånskruer", 13, "start", "#111", "bold")
for i, (_d, _s) in enumerate([
        ("Ø5", "gennemgang, 4,5 mm skruer — altid"),
        ("Ø5,5", "gennemgang, de 6 stk. 5 mm skruer"),
        ("Ø3", "pilot i den FJERNE del (4,5 mm skruer)"),
        ("Ø3,5", "pilot i ENDETRÆ (5 mm skruer), 40 mm"),
        ("Ø10", "forsænk, 4,5-hoveder (Ø9)"),
        ("Ø11", "forsænk, 5,0-hoveder (Ø10)"),
        ("Ø2,5", "pilot til vinkelbeslagets korte skruer"),
        ("Ø12", "boltehul, M10×160 på vange-aksen"),
        ("Ø10", "boltehul, M8×100 på endestykke-aksen")]):
    _y = ly + 50 + i * 19
    text(lx + 16, _y, _d, 11.5, "start", "#c0392b", "bold")
    text(lx + 56, _y, _s, 11.5, "start", "#333")
text(lx + 16, ly + 224, "Gennemgang = skruediameter + 0,5 mm · pilot ≈ 65 % af Ø.", 10.5, "start", "#555")
text(lx + 16, ly + 241, "Uden gennemgangshul griber gevindet i den nære del og jækker", 10.5, "start", "#555")
text(lx + 16, ly + 256, "delene fra hinanden i stedet for at spænde dem sammen.", 10.5, "start", "#555")
text(lx + 16, ly + 276, "Forsænk med ÉN kegleforsænker 90° Ø16: Ø16 er keglens", 10.5, "start", "#555")
text(lx + 16, ly + 291, "største mål, ikke hullets — Ø10/Ø11 er to dybder.", 10.5, "start", "#555")
text(lx + 16, ly + 313, "Længder: 4,5×60 til lamellerne · 4,5×50 KUN til", 10.5, "start", "#111", "bold")
text(lx + 16, ly + 329, "støtteliste→vange · 5×80 til de 6 i ENDETRÆ.", 10.5, "start", "#111", "bold")
text(lx + 16, ly + 351, "BOR-LÆNGDER (gennemgang/pilot-dybde):", 10.5, "start", "#1f6f9c", "bold")
text(lx + 16, ly + 366, "Ø5 21–45 · Ø5,5 45 · Ø3 20–35 · Ø3,5 40 · Ø2,5 ≈15 (mm)", 10.5, "start", "#1f6f9c")
text(lx + 16, ly + 381, "Ø10 90 mm gennem · Ø12 140 mm gennem — kræver LANGT bor!", 10.5, "start", "#c0392b", "bold")

# ============================================================= Panel B
sb = 0.135
bx, by = 130, 430
led_len_mm = 1770.0
text(bx, by - 22, "B · Støtteliste → vange — huller langs listen (6 stk)", 15, "start", "#111", "bold")
rect(bx, by, led_len_mm * sb, 20, C_LEDGER, "#222", 0.8)
hx = [bx + (x - led_start) * sb for x in ledger_screws_x]
for x in hx:
    circ(x, by + 10, 4)
dim_h(bx, hx[0], by + 40, "190")          # label over stregen, ellers støder den ind i "330 (c/c)"
dim_h(hx[0], hx[1], by + 40, "330 (c/c)", above=False)
dim_h(bx, bx + led_len_mm * sb, by - 8, f"{led_len_mm:.0f} (liste)")
text(bx, by + 66, "6 × spånskrue 4,5 × 50 fra listens inderside vandret ind i vangen (skjult under lamellerne).",
     11, "start", "#333")
text(bx, by + 83, "IKKE 70 her: 21 mm liste + 45 mm vange = 66 mm stak — en 70'er stikker 4 mm ud på vangens yderside.",
     11, "start", "#c0392b")
text(bx, by + 100, "Ø5 GENNEMGANG i listen · Ø3 pilot 35 mm i vangen · Ø10 forsænk i listens inderside.",
     11, "start", "#c0392b")

# ============================================================= Panel C (bolt)
scc = 0.62
Cx0, floorC = 210, 786           # px of Y=0 and Z=0


def cX(y):
    return Cx0 + y * scc


def cZ(z):
    return floorC - z * scc


ftop = clearance + 95.0          # frame/rail top (light variant)
text(Cx0 - 60, cZ(ftop) - 44, "C · Hjørne (vange-akse) — bolt gennem 45+95 mm ben",
     15, "start", "#111", "bold")
# vange cross-section (Y 0..45) and 45x95 leg (Y 45..140, Z 0..ftop)
rect(cX(0), cZ(ftop), 45 * scc, (ftop - clearance) * scc, C_RAIL, "#222", 1.0)
text(cX(22), cZ(ftop - 8), "vange", 10, "middle", "#333")
rect(cX(45), cZ(ftop), 95 * scc, ftop * scc, C_LEG, "#222", 1.0)
text(cX(92), cZ(clearance * 0.5), "ben 45×95", 11, "middle", "#333")
# floor
line(cX(-18), floorC, cX(175), floorC, "#111", 1.6)
text(cX(-16), floorC + 15, "gulv", 10, "start", "#555")
# 2 through-bolts (Ø12) through vange(45) + leg(95) = 140 mm; M10x160 -> 20 mm ude
for z in z_vange:
    line(cX(-8), cZ(z), cX(162), cZ(z), "#c0392b", 1.8)   # bolt shank, M10x160
    circ(cX(-8), cZ(z), 5, "#f3d6d6", "#c0392b")          # dome head (outside)
    # skive + moetrik + kontramoetrik UDEN paa benets inderside (y 140..158,5)
    rect(cX(140), cZ(z) - 7, 18.5 * scc, 14, "#dbeaf2", "#1f6f9c", 1.2)
text(cX(140) + 8, cZ(z_vange[1]) - 4, "skive + møtrik", 10, "start", "#1f6f9c")
text(cX(140) + 8, cZ(z_vange[1]) + 9, "+ kontramøtrik", 10, "start", "#1f6f9c")
text(cX(140) + 8, cZ(z_vange[1]) + 22, "INGEN forsænkning", 10, "start", "#c0392b")
# dims
dim_v(cZ(z_vange[0]), floorC, cX(-8) - 16, f"{z_vange[0]:.0f}")
dim_v(cZ(z_vange[1]), floorC, cX(-8) - 46, f"{z_vange[1]:.0f}")
dim_v(cZ(z_vange[0]), cZ(clearance), cX(-8) - 76, "30")
dim_v(cZ(z_vange[1]), cZ(z_vange[0]), cX(-8) - 104, "45")
dim_v(cZ(clearance), floorC, cX(175) + 22, f"{clearance:.0f}", left=False)
dim_h(cX(0), cX(140), cZ(ftop) - 14, "Ø12 hul gennem 140 mm (45+95)")
text(Cx0 - 60, floorC + 40, "VANGE-AKSE: M10×160 bolt gennem vange (45) + ben (95) = 140 mm træ. "
     "Der stikker 20 mm ud på benets inderside:", 11, "start", "#333")
text(Cx0 - 60, floorC + 58, "skive 2,5 + møtrik 8 + KONTRAMØTRIK 8 = 18,5 mm — reelt plant. INGEN forsænkning "
     "(en M10×140 har nul gevind til møtrikken).", 11, "start", "#333")
text(Cx0 - 60, floorC + 78, "ENDESTYKKE-AKSE (vinkelret): M8×100 i Ø10-hul gennem endestykke (45) + ben (45) = 90 mm "
     "— møtrik + STOR skive fladt, INGEN forsænkning", 11, "start", "#333")
text(Cx0 - 60, floorC + 96, "(en 140 mm bolt ville stritte ~50 mm ind under lamellen). Højder 15/50, "
     f"forskudt fra vange-boltene ({z_vange[0]:.0f}/{z_vange[1]:.0f}).", 11, "start", "#333")

# ============================================================= Panel C2 (bolt, endestykke-akse)
# Samme gulvlinje og skala som Panel C, sat ved siden af i den ledige kolonne
# under BORDIAMETRE-boksen (ingen ny raekke -> ingen ekstra sidehoejde).
scc2 = scc
Cx0_2, floorC2 = 830, floorC


def cX2(y):
    return Cx0_2 + y * scc2


def cZ2(z):
    return floorC2 - z * scc2


text(700, cZ2(ftop) - 58, "C2 · Hjørne (endestykke-akse)", 13, "start", "#111", "bold")
text(700, cZ2(ftop) - 42, "bolt gennem 45+45 mm ben", 11, "start", "#111", "bold")
# endestykke cross-section (X 0..45) and 45x45-side leg (X 45..90, Z 0..ftop)
rect(cX2(0), cZ2(ftop), 45 * scc2, (ftop - clearance) * scc2, C_RAIL, "#222", 1.0)
text(cX2(22), cZ2(ftop - 8), "ende", 9, "middle", "#333")
rect(cX2(45), cZ2(ftop), 45 * scc2, ftop * scc2, C_LEG, "#222", 1.0)
text(cX2(67), cZ2(clearance * 0.5), "ben 45×95", 10, "middle", "#333")
line(cX2(-14), floorC2, cX2(112), floorC2, "#111", 1.6)
# 2 through-bolts (Ø10) through endestykke(45) + leg(45) = 90 mm; M8x100 -> 10 mm ude
for z in z_ende:
    line(cX2(-8), cZ2(z), cX2(100), cZ2(z), "#c0392b", 1.8)   # bolt shank, M8x100
    circ(cX2(-8), cZ2(z), 4.5, "#f3d6d6", "#c0392b")          # dome head (outside)
    rect(cX2(90), cZ2(z) - 6, 10 * scc2, 12, "#dbeaf2", "#1f6f9c", 1.2)  # skive + moetrik
text(cX2(90) + 6, cZ2(z_ende[1]) - 2, "skive + møtrik", 9, "start", "#1f6f9c")
text(cX2(90) + 6, cZ2(z_ende[1]) + 11, "INGEN forsænkning", 9, "start", "#c0392b")
# dims
dim_v(cZ2(z_ende[0]), floorC2, cX2(-8) - 14, f"{z_ende[0]:.0f}")
dim_v(cZ2(z_ende[1]), floorC2, cX2(-8) - 42, f"{z_ende[1]:.0f}")
dim_v(cZ2(z_ende[0]), cZ2(clearance), cX2(-8) - 70, "15")
dim_v(cZ2(z_ende[1]), cZ2(z_ende[0]), cX2(-8) - 98, "35")
dim_h(cX2(0), cX2(90), cZ2(ftop) - 14, "Ø10 gennem 90 mm (45+45)")
text(700, floorC2 + 15, "Se tekst ved Panel C: M8×100, INGEN forsænkning,", 9.5, "start", "#555")
text(700, floorC2 + 28, "forskudt 15/50 fra vange-boltene (kryds i benet).", 9.5, "start", "#555")

# ============================================================= Panel D
text(130, 930, "D · Boltplacering på vange og endestykke — opstalt udefra", 15, "start", "#111", "bold")
sd = 0.40
dxD = 130

# --- vange (2010 x 95), set udefra; hoejder maalt fra underkant
dyV = 1025


def vXp(x):
    return dxD + x * sd


def vZp(h):
    return dyV - h * sd


rect(vXp(0), vZp(95), 2000 * sd, 95 * sd, C_RAIL, "#222", 1.0)
text(vXp(1000), vZp(95) - 8, "VANGE udefra (2 stk, ens i begge ender)", 11, "middle", "#333")
for x in (67, 1933):
    for h in (30, 75):
        circ(vXp(x), vZp(h), 4)
dim_h(vXp(0), vXp(67), dyV + 16, "67", above=False)
dim_h(vXp(1933), vXp(2000), dyV + 16, "67", above=False)
dim_v(vZp(30), dyV, vXp(67) - 26, "30")
dim_v(vZp(75), vZp(30), vXp(67) - 54, "45")
text(vXp(1000), dyV + 40, "4 × M10×160 gennemgående pr. vange (gennem 45+95=140 mm træ). Højder fra underkant.",
     11, "middle", "#333")
text(vXp(1000), dyV + 58, "INGEN forsænkning: M10×160 stikker 20 mm ud på benets INDERSIDE til skive + 2 møtrikker.",
     11, "middle", "#c0392b")

# --- endestykke (1810 x 95) inkl. midterdrager-skruer
dyE = 1160


def eXp(y):
    return dxD + y * sd


def eZp(h):
    return dyE - h * sd


rect(eXp(0), eZp(95), 1710 * sd, 95 * sd, C_RAIL, "#222", 1.0)
text(eXp(855), eZp(95) - 8, "ENDESTYKKE udefra (2 stk)", 11, "middle", "#333")
for y in (47, 1663):
    for h in (15, 50):
        circ(eXp(y), eZp(h), 4)
for h in (23, 47):                       # midterdrager-skruer, midtfor
    circ(eXp(855), eZp(h), 3, "#fff", "#1f6f9c")
dim_h(eXp(0), eXp(47), dyE + 16, "47", above=False)
dim_h(eXp(1663), eXp(1710), dyE + 16, "47", above=False)
dim_h(eXp(0), eXp(855), dyE + 36, "855 (midt)", above=False)
dim_v(eZp(15), dyE, eXp(47) - 26, "15")
dim_v(eZp(50), eZp(15), eXp(47) - 54, "35")
text(eXp(855), dyE + 62, "M8×100 hjørnebolte i Ø10-hul, højde 15/50 (gennem 45+45=90 mm ben, møtrik + stor "
     "skive fladt, INGEN forsænkning).", 11, "middle", "#333")
text(eXp(855), dyE + 80, "Blå: 2 skruer 5×80 midtfor i højde 23/47 ind i midterdragerens ENDETRÆ "
     "(+ vinkelbeslag) — Ø5,5 gennemgang i endestykket, Ø3,5 pilot i endetræet.", 11, "middle", "#333")
text(eXp(855), dyE + 98, "Lamel → midterdrager: 1 skrue 4,5×60 lodret ned midt i hver lamel, langs "
     "dragerens centerlinje —", 11, "middle", "#333")
text(eXp(855), dyE + 116, "Ø5 gennem lamellen, forsænk 2–3 mm UNDER sovefladen. Midterdrager → midterben: "
     "2 skruer 5×80 lodret ned, Ø3,5 pilot i benets endetræ (kun 7,5 mm til kanten!).", 11, "middle", "#333")

W, H = 1060, 1330
out = os.path.join(_CAD, "seng_let_boreplan.svg")
body = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>',
        f'<text x="{W/2}" y="40" font-family="Helvetica,Arial,sans-serif" font-size="21" '
        f'font-weight="bold" text-anchor="middle" fill="#111">'
        f'Boreplan — LET variant, futon 200 × 180 cm (mål i mm)</text>']
body += svg
body.append('</svg>')
with open(out, "w") as f:
    f.write("\n".join(body))
print("SAVED", out, W, "x", H)

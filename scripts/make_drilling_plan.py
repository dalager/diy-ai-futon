"""Generate a dimensioned drilling plan (SVG) for the screw holes.

    python3 scripts/make_drilling_plan.py  ->  cad/seng_boreplan.svg

Three detail panels:
  A  Lamelhuller (plan)        - slat->ledger holes, pitch & pair spacing
  B  Stoetteliste -> vange     - ledger->rail holes along the length
  C  Hjoerne (gavl-snit)       - frame->leg holes and their heights
"""

# ---- parameters (mirror build_bed.py) --------------------------------------
slat_t, slat_h = 45.0, 70.0
gap = 58.4
pitch = 103.44
ledger_t, ledger_h = 21.0, 45.0
clearance = 200.0
z_vange = (clearance + 25.0, clearance + 80.0)   # vange bolt heights
z_ende = (clearance + 55.0, clearance + 110.0)   # endestykke bolt heights (staggered)
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
text(ax + 6, led_y + led_h_px + 16, f"støtteliste ({ledger_t:.0f} bred)", 11, "start", "#555")
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
text(ax, ay + 180, "2 skruer 4,5 × 70 pr. ende · Ø4 forbor i listen (= afstands-jig) · forbor lamel 3 mm",
     11, "start", "#333")

# ============================================================= Panel B
sb = 0.135
bx, by = 130, 430
led_len_mm = 1780.0
text(bx, by - 22, "B · Støtteliste → vange — huller langs listen (6 stk)", 15, "start", "#111", "bold")
rect(bx, by, led_len_mm * sb, 20, C_LEDGER, "#222", 0.8)
hx = [bx + (x - led_start) * sb for x in ledger_screws_x]
for x in hx:
    circ(x, by + 10, 4)
dim_h(bx, hx[0], by + 40, "190", above=False)
dim_h(hx[0], hx[1], by + 40, "330 (c/c)", above=False)
dim_h(bx, bx + led_len_mm * sb, by - 8, "1780 (liste)")
text(bx, by + 66, "Skru fra listens inderside vandret ind i vangen (skjult under lamellerne).",
     11, "start", "#333")

# ============================================================= Panel C (bolt)
scc = 0.62
Cx0, floorC = 210, 786           # px of Y=0 and Z=0


def cX(y):
    return Cx0 + y * scc


def cZ(z):
    return floorC - z * scc


ftop = clearance + 120.0         # frame/rail top
text(Cx0 - 60, cZ(ftop) - 26, "C · Hjørne (gavl-snit) — M10 gennemgående bræddebolt",
     15, "start", "#111", "bold")
# rail cross-section (Y 0..45, Z clearance..ftop) and leg (Y 45..115, Z 0..ftop)
rect(cX(0), cZ(ftop), 45 * scc, (ftop - clearance) * scc, C_RAIL, "#222", 1.0)
text(cX(22), cZ(ftop - 8), "vange", 10, "middle", "#333")
rect(cX(45), cZ(ftop), 70 * scc, ftop * scc, C_LEG, "#222", 1.0)
text(cX(80), cZ(clearance * 0.5), "ben", 11, "middle", "#333")
# floor
line(cX(-18), floorC, cX(150), floorC, "#111", 1.6)
text(cX(-16), floorC + 15, "gulv", 10, "start", "#555")
# 2 through-bolts (Ø11) all the way through rail + leg
for z in z_vange:
    line(cX(-8), cZ(z), cX(115), cZ(z), "#c0392b", 1.8)   # bolt shank
    circ(cX(-8), cZ(z), 5, "#f3d6d6", "#c0392b")          # dome head (outside)
    # washer + nut on the inner face (X=115), in the slat-inset gap
    rect(cX(115), cZ(z) - 6, 16 * scc, 12 * scc, "#dbeaf2", "#1f6f9c", 1.2)
text(cX(115) + 16 * scc + 4, cZ(z_vange[1]), "møtrik + skive", 10, "start", "#1f6f9c")
# dims
dim_v(cZ(z_vange[0]), floorC, cX(-8) - 16, f"{z_vange[0]:.0f}")
dim_v(cZ(z_vange[1]), floorC, cX(-8) - 46, f"{z_vange[1]:.0f}")
dim_v(cZ(clearance), floorC, cX(150) + 22, f"{clearance:.0f}", left=False)
dim_h(cX(0), cX(115), cZ(ftop) - 12, "Ø11 hul gennem 115 mm")
text(Cx0 - 60, floorC + 40, "Ø11 boltehul lige igennem ramme (45) + ben (70). Bræddebolt-hoved "
     "udenpå, møtrik + skive på indersiden i lamel-mellemrummet. Endestykke→ben "
     f"er magen til, men bolte forskudt i højderne {z_ende[0]:.0f}/{z_ende[1]:.0f}, så de ikke krydser.",
     11, "start", "#333")

W, H = 1060, 860
out = "/home/dalager/projects/seng/cad/seng_boreplan.svg"
body = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>',
        f'<text x="{W/2}" y="40" font-family="Helvetica,Arial,sans-serif" font-size="21" '
        f'font-weight="bold" text-anchor="middle" fill="#111">'
        f'Boreplan — sengebund futon 200 × 180 cm (mål i mm, Ø4,5 huller)</text>']
body += svg
body.append('</svg>')
with open(out, "w") as f:
    f.write("\n".join(body))
print("SAVED", out, W, "x", H)

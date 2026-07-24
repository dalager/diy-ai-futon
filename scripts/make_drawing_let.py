"""Generate a dimensioned technical drawing (SVG) of the bed from the same
parameters used by build_bed.py. Pure Python, no FreeCAD needed.

    python3 scripts/make_drawing.py
"""

# ------------------------------------------------------------- parameters (mm)
clearance = 200.0
rail_h = 95.0                            # slimmer frame (light variant)
rail_t = 45.0
outer_len = 2000.0                       # udvendig laengde 200 cm (= madras)
inner_w = 1710.0                         # -> outer_w = 1800 (udvendig bredde 180 cm)
leg = 70.0                               # corner clearance -> slat field start (led_x0)
leg_sx, leg_sy = 45.0, 95.0              # hjørneben fra afskær (X x Y)
cleg_sx, cleg_sy = 45.0, 45.0            # midterben fra drager-afskær (45x45)
ledger_t = 21.0
ledger_h = 45.0
slat_t = 45.0
slat_h = 45.0                            # square slats (light variant)
n_slats = 17
drager_t = 45.0                          # centre beam width (Y)
drager_h = 45.0                          # centre beam height (Z) -- samme profil som lameller
mat_l, mat_w, mat_h = 2000.0, 1800.0, 150.0

outer_w = inner_w + 2 * rail_t          # 1800
frame_top = clearance + rail_h          # 295 (rail/end top)
slat_top = frame_top                    # 295 sovflade -- lameller flugter med rammen
ledger_top = slat_top - slat_h          # 250 ledger top supports slat bottom
led_x0 = rail_t + leg                    # 115 (ledger start)
led_len = (outer_len - rail_t - leg) - led_x0    # 1780 (ledger length)
SLAT_INSET = 0.0
slat_x0 = led_x0 + SLAT_INSET            # 115 (slats start at the leg)
slat_field = led_len - 2 * SLAT_INSET    # 1700
pitch = (slat_field - slat_t) / (n_slats - 1)
gap = pitch - slat_t
Zmax = slat_top + mat_h                  # 450
beam_z = ledger_top - drager_h           # centre beam underside (=200)
beam_y0 = (outer_w - drager_t) / 2.0     # centre beam Y start
cx_len = outer_len / 2.0                 # centre leg X centre

S = 0.30  # px per mm

svg = []


def rect(x, y, w, h, fill="none", stroke="#222", sw=1.0, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} {extra}/>')


def line(x1, y1, x2, y2, stroke="#222", sw=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
               f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def text(x, y, s, size=13, anchor="middle", fill="#111", weight="normal"):
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica,Arial,sans-serif" '
               f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
               f'fill="{fill}">{s}</text>')


def tick(x, y):
    line(x - 3, y + 3, x + 3, y - 3, "#c0392b", 1.2)


def dim_h(x1, x2, y, label, above=True):
    """Horizontal dimension between px x1..x2 at height y."""
    line(x1, y, x2, y, "#c0392b", 0.8)
    tick(x1, y); tick(x2, y)
    ty = y - 5 if above else y + 14
    text((x1 + x2) / 2, ty, label, 12, "middle", "#c0392b")


def dim_v(y1, y2, x, label, left=True):
    line(x, y1, x, y2, "#c0392b", 0.8)
    tick(x, y1); tick(x, y2)
    anchor = "end" if left else "start"
    tx = x - 6 if left else x + 6
    text(tx, (y1 + y2) / 2 + 4, label, 12, anchor, "#c0392b")


C_RAIL = "#d8c9a8"
C_LEG = "#b99763"
C_SLAT = "#efe7d3"
C_LEDGER = "#c9b487"
C_BEAM = "#c2a266"

# ============================================================ TOP VIEW (plan)
tx, ty = 130, 120
svg.append(f'<g transform="translate({tx},{ty})">')
fx = lambda X: X * S
fy = lambda Y: Y * S
text(fx(outer_len) / 2, -18, "PLAN (set oppefra)", 15, "middle", "#111", "bold")
# ledgers (under slats)
rect(fx(led_x0), fy(rail_t), led_len * S, ledger_t * S, C_LEDGER, "#222", 0.6)
rect(fx(led_x0), fy(outer_w - rail_t - ledger_t), led_len * S, ledger_t * S, C_LEDGER, "#222", 0.6)
# centre beam (under the slats) + centre leg
rect(fx(rail_t), fy(beam_y0), (outer_len - 2 * rail_t) * S, drager_t * S, C_BEAM, "#222", 0.6)
rect(fx(cx_len - cleg_sx / 2), fy((outer_w - cleg_sy) / 2), cleg_sx * S, cleg_sy * S, "none", "#666", 0.7, "3,3")
text(fx(cx_len), fy(beam_y0) - 4, "midterdrager", 11, "middle", "#7a5")
# slats
for i in range(n_slats):
    x = slat_x0 + i * pitch
    rect(fx(x), fy(rail_t), slat_t * S, inner_w * S, C_SLAT, "#555", 0.5)
# side + end rails
rect(0, 0, outer_len * S, rail_t * S, C_RAIL, "#222", 1.0)
rect(0, fy(outer_w - rail_t), outer_len * S, rail_t * S, C_RAIL, "#222", 1.0)
rect(0, fy(rail_t), rail_t * S, inner_w * S, C_RAIL, "#222", 1.0)
rect(fx(outer_len - rail_t), fy(rail_t), rail_t * S, inner_w * S, C_RAIL, "#222", 1.0)
# legs (45x95 corner)
for lx in (rail_t, outer_len - rail_t - leg_sx):
    for ly in (rail_t, outer_w - rail_t - leg_sy):
        rect(fx(lx), fy(ly), leg_sx * S, leg_sy * S, C_LEG, "#222", 0.8)
# mattress outline
rect(fx((outer_len - mat_l) / 2), fy((outer_w - mat_w) / 2), mat_l * S, mat_w * S,
     "none", "#2a6", 1.0, "6,4")
text(fx(outer_len / 2), fy(outer_w / 2) + 4, "madras 2000 x 1800", 12, "middle", "#2a6")
# dimensions
dim_h(0, fx(outer_len), fy(outer_w) + 34, f"{outer_len:.0f}")
dim_v(0, fy(outer_w), -22, f"{outer_w:.0f}")
dim_v(fy(rail_t), fy(outer_w - rail_t), fx(outer_len) + 22, f"{inner_w:.0f} (indv.)", left=False)
# slat pitch between slat 5 and 6
xa = fx(slat_x0 + 5 * pitch); xb = fx(slat_x0 + 6 * pitch)
dim_h(xa, xb, -8, f"{pitch:.0f}")
xg1 = fx(slat_x0 + 6 * pitch + slat_t); xg2 = fx(slat_x0 + 7 * pitch)
dim_h(xg1, xg2, fy(outer_w) + 12, f"spalte {gap:.0f}", above=False)
svg.append('</g>')

# ============================================================ SIDE VIEW (length)
sx, sy = 130, 120 + outer_w * S + 130
svg.append(f'<g transform="translate({sx},{sy})">')
gx = lambda X: X * S
gy = lambda Z: (Zmax - Z) * S
text(gx(outer_len) / 2, -14, "OPSTALT (langside)", 15, "middle", "#111", "bold")
line(-10, gy(0), gx(outer_len) + 10, gy(0), "#111", 1.4)          # floor
# ledger (behind)
rect(gx(led_x0), gy(ledger_top), led_len * S, ledger_h * S, C_LEDGER, "#999", 0.5, "3,3")
# side rail
rect(0, gy(frame_top), outer_len * S, rail_h * S, C_RAIL, "#222", 1.0)
# centre beam (under slats) + centre leg
rect(gx(rail_t), gy(ledger_top), (outer_len - 2 * rail_t) * S, drager_h * S, C_BEAM, "#222", 0.8)
rect(gx(cx_len - cleg_sx / 2), gy(beam_z), cleg_sx * S, beam_z * S, C_LEG, "#222", 0.9)
# slats on edge
for i in range(n_slats):
    x = slat_x0 + i * pitch
    rect(gx(x), gy(slat_top), slat_t * S, slat_h * S, C_SLAT, "#555", 0.5)
# legs (45 mm seen from the long side)
for lx in (rail_t, outer_len - rail_t - leg_sx):
    rect(gx(lx), gy(frame_top), leg_sx * S, frame_top * S, C_LEG, "#222", 0.9)
# mattress
rect(gx((outer_len - mat_l) / 2), gy(slat_top + mat_h), mat_l * S, mat_h * S,
     "none", "#2a6", 1.0, "6,4")
# dims
dim_h(0, gx(outer_len), gy(0) + 30, f"{outer_len:.0f}")
dim_v(gy(clearance), gy(0), -18, f"{clearance:.0f}", left=True)
dim_v(gy(frame_top), gy(clearance), -18, f"{rail_h:.0f}", left=True)
dim_v(gy(0), gy(slat_top), gx(outer_len) + 20, f"{slat_top:.0f}", left=False)
svg.append('</g>')

# ============================================================ END VIEW (width)
ex, ey = 130, sy + Zmax * S + 120
svg.append(f'<g transform="translate({ex},{ey})">')
ux = lambda Y: Y * S
uy = lambda Z: (Zmax - Z) * S
text(ux(outer_w) / 2, -14, "ENDE (set fra fodenden)", 15, "middle", "#111", "bold")
line(-10, uy(0), ux(outer_w) + 10, uy(0), "#111", 1.4)           # floor
# slat (seen along length)
rect(ux(rail_t), uy(slat_top), inner_w * S, slat_h * S, C_SLAT, "#555", 0.6)
# ledgers
rect(ux(rail_t), uy(ledger_top), ledger_t * S, ledger_h * S, C_LEDGER, "#222", 0.7)
rect(ux(outer_w - rail_t - ledger_t), uy(ledger_top), ledger_t * S, ledger_h * S, C_LEDGER, "#222", 0.7)
# side rails (section)
rect(ux(0), uy(frame_top), rail_t * S, rail_h * S, C_RAIL, "#222", 1.0)
rect(ux(outer_w - rail_t), uy(frame_top), rail_t * S, rail_h * S, C_RAIL, "#222", 1.0)
# centre beam (section) + centre leg
rect(ux(beam_y0), uy(ledger_top), drager_t * S, drager_h * S, C_BEAM, "#222", 0.9)
rect(ux((outer_w - cleg_sy) / 2), uy(beam_z), cleg_sy * S, beam_z * S, C_LEG, "#222", 0.9)
# legs (95 mm seen from the end)
for ly in (rail_t, outer_w - rail_t - leg_sy):
    rect(ux(ly), uy(frame_top), leg_sy * S, frame_top * S, C_LEG, "#222", 0.9)
# mattress
rect(ux((outer_w - mat_w) / 2), uy(slat_top + mat_h), mat_w * S, mat_h * S,
     "none", "#2a6", 1.0, "6,4")
# dims
dim_h(0, ux(outer_w), uy(0) + 30, f"{outer_w:.0f}")
dim_v(uy(clearance), uy(0), -18, f"{clearance:.0f}", left=True)
dim_v(uy(slat_top), uy(slat_top - slat_h), ux(outer_w) + 20, f"{slat_h:.0f}", left=False)
svg.append('</g>')

# ============================================================ cut list panel
cx = 130 + outer_len * S + 90
cy = 120
rows = [
    ("Del", "Antal", "Dimension", "Længde"),
    ("Vange (langside)", "2", f"{rail_t:.0f} x {rail_h:.0f}", f"{outer_len:.0f}"),
    ("Endestykke", "2", f"{rail_t:.0f} x {rail_h:.0f}", f"{inner_w:.0f}"),
    ("Ben (hjørne, afskær)", "4", "45 x 95", f"{frame_top:.0f}"),
    ("Midterdrager", "1", f"{drager_t:.0f} x {drager_h:.0f}", f"{outer_len - 2 * rail_t:.0f}"),
    ("Midterben (afskær)", "1", "45 x 45", f"{beam_z:.0f}"),
    ("Støtteliste", "2", f"{ledger_t:.0f} x {ledger_h:.0f}", f"{led_len:.0f}"),
    ("Lamel", str(n_slats), f"{slat_t:.0f} x {slat_h:.0f}", f"{inner_w:.0f}"),
]
svg.append(f'<g transform="translate({cx},{cy})">')
text(0, -18, "STYKLISTE (mm, fyr)", 15, "start", "#111", "bold")
rh = 26
colx = [0, 175, 235, 340]
for r, row in enumerate(rows):
    y = r * rh
    if r == 0:
        rect(-8, y - 16, 400, rh, "#333", "none")
    elif r % 2:
        rect(-8, y - 16, 400, rh, "#f0ece2", "none")
    for c, val in enumerate(row):
        col = "#fff" if r == 0 else "#111"
        w = "bold" if r == 0 else "normal"
        anchor = "start" if c < 2 else ("middle" if c == 2 else "end")
        xx = colx[c] if c != 2 else colx[c]
        if c == 3:
            xx = 392
        text(xx, y, val, 12, anchor, col, w)
notes = [
    "",
    f"Frihøjde under ramme: {clearance:.0f} mm (til støvsugning)",
    f"Sovehøjde (top af lameller): {slat_top:.0f} mm",
    f"Lamel c/c: {pitch:.0f} mm — spalte {gap:.0f} mm — åbning ~{gap/pitch*100:.0f}%",
    "Let variant: 45x45 lameller + midterdrager",
    "på ét midterben (halverer lamelspændet).",
    "Ben af afskær (45x95) — ubehandlet, ingen lim.",
    "Vange-bolt: møtrik i Ø20 forsænkning i benet.",
]
for i, nline in enumerate(notes):
    text(0, len(rows) * rh + 14 + i * 18, nline, 12, "start", "#333")
svg.append('</g>')

W, H = 1240, int(ey + Zmax * S + 90)
out = "/home/dalager/projects/seng/cad/seng_let_tegning.svg"
header = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
          f'width="{W}" height="{H}">')
body = [header, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>',
        f'<text x="{W/2}" y="46" font-family="Helvetica,Arial,sans-serif" font-size="22" '
        f'font-weight="bold" text-anchor="middle" fill="#111">'
        f'Sengebund til futon 200 x 180 cm — LET variant — mål i mm</text>']
body += svg
body.append('</svg>')
with open(out, "w") as f:
    f.write("\n".join(body))
print("SAVED", out, "size", W, "x", H)

"""Headless FreeCAD build of the LIGHT futon bed base (200 x 180 cm).

Lighter variant: slimmer 45x95 frame, square 45x45 slats, a longitudinal
centre beam (midterdrager) on one centre leg so the slats only span ~905 mm.

Run with:  freecad.cmd scripts/build_bed_let.py   ->  cad/seng_let.FCStd + .step
Coordinate system:  X = length, Y = width, Z = up.  All mm.
"""

import os
import FreeCAD as App
import Part
from collections import defaultdict

P = dict(
    clearance=200.0,     # 20 cm free height
    rail_h=95.0,         # slimmer frame (was 120)
    rail_t=45.0,
    outer_len=2010.0,
    inner_w=1810.0,
    leg=70.0,
    ledger_t=21.0,
    ledger_h=45.0,
    slat_t=45.0,         # square slat -> no tipping, needs centre support
    slat_h=45.0,
    n_slats=17,
    drager_t=45.0,       # centre beam width (Y)
    drager_h=70.0,       # centre beam height (Z)
    mattress_l=2000.0, mattress_w=1800.0, mattress_h=150.0,
)

rt, lg = P["rail_t"], P["leg"]
outer_w = P["inner_w"] + 2 * rt                    # 1900
frame_top = P["clearance"] + P["rail_h"]           # 295
slat_top = frame_top + 20.0                        # 315 sleeping surface
ledger_top = slat_top - P["slat_h"]                # 270 slat underside
ledger_z = ledger_top - P["ledger_h"]              # 225
beam_z = ledger_top - P["drager_h"]                # 200 (= clearance)
beam_y0 = (outer_w - P["drager_t"]) / 2.0          # 927.5
cx_len = P["outer_len"] / 2.0                       # 1005

OUT_DIR = "/home/dalager/projects/seng/cad"
FCSTD = os.path.join(OUT_DIR, "seng_let.FCStd")
STEP = os.path.join(OUT_DIR, "seng_let.step")

doc = App.newDocument("seng_let")
parts = []
box_group = {}

g_frame = doc.addObject("App::DocumentObjectGroup", "Ramme")
g_legs = doc.addObject("App::DocumentObjectGroup", "Ben")
g_ledger = doc.addObject("App::DocumentObjectGroup", "Stoettelister")
g_slats = doc.addObject("App::DocumentObjectGroup", "Lameller")
g_beam = doc.addObject("App::DocumentObjectGroup", "Midterdrager")
g_ref = doc.addObject("App::DocumentObjectGroup", "Reference")


def box(name, x, y, z, dx, dy, dz, group=None):
    o = doc.addObject("Part::Box", name)
    o.Length, o.Width, o.Height = dx, dy, dz
    o.Placement = App.Placement(App.Vector(x, y, z), App.Rotation())
    o.Label = name
    parts.append(o)
    if group is not None:
        group.addObject(o)
        box_group[o.Name] = group
    return o


# --- frame
box("Vange_A", 0, 0, P["clearance"], P["outer_len"], rt, P["rail_h"], g_frame)
box("Vange_B", 0, outer_w - rt, P["clearance"], P["outer_len"], rt, P["rail_h"], g_frame)
box("Endestykke_1", 0, rt, P["clearance"], rt, P["inner_w"], P["rail_h"], g_frame)
box("Endestykke_2", P["outer_len"] - rt, rt, P["clearance"], rt, P["inner_w"], P["rail_h"], g_frame)

# --- corner legs: 45x95 from vange/endestykke afskaer (loesning B, no glue).
# 45 mm faces the length (X, flush with endestykke), 95 mm the width (Y, flush
# with vange). Leg X-extent (45) stays clear of the slat field at x=115.
leg_sx, leg_sy = 45.0, 95.0
LX = [rt, P["outer_len"] - rt - leg_sx]            # [45, 1920]
LY = [rt, outer_w - rt - leg_sy]                   # [45, 1760]
for i, lx in enumerate(LX):
    for j, ly in enumerate(LY):
        box(f"Ben_{i}{j}", lx, ly, 0, leg_sx, leg_sy, frame_top, g_legs)

# --- centre beam (midterdrager) + centre leg (45x70 from drager afskaer)
box("Midterdrager", rt, beam_y0, beam_z, P["outer_len"] - 2 * rt, P["drager_t"], P["drager_h"], g_beam)
cleg_sx, cleg_sy = 70.0, 45.0                       # 70 (X) x 45 (Y, matches drager)
box("Midterben", cx_len - cleg_sx / 2, beam_y0, 0, cleg_sx, cleg_sy, beam_z, g_legs)

# --- ledgers
led_x0 = rt + lg                                   # 115
led_len = (P["outer_len"] - rt - lg) - led_x0      # 1780
box("Stoetteliste_A", led_x0, rt, ledger_z, led_len, P["ledger_t"], P["ledger_h"], g_ledger)
box("Stoetteliste_B", led_x0, outer_w - rt - P["ledger_t"], ledger_z,
    led_len, P["ledger_t"], P["ledger_h"], g_ledger)

# --- slats (square), full width, resting on two ledgers + the centre beam
n, st = P["n_slats"], P["slat_t"]
slat_x0 = led_x0
pitch = (led_len - st) / (n - 1)
for i in range(n):
    x = slat_x0 + i * pitch
    box(f"Lamel_{i:02d}", x, rt, ledger_top, st, P["inner_w"], P["slat_h"], g_slats)

# --- mattress reference
mat = doc.addObject("Part::Box", "Madras_ref")
mat.Length, mat.Width, mat.Height = P["mattress_l"], P["mattress_w"], P["mattress_h"]
mat.Placement = App.Placement(App.Vector((P["outer_len"] - P["mattress_l"]) / 2,
                              (outer_w - P["mattress_w"]) / 2, slat_top), App.Rotation())
mat.Label = "Madras_ref"
g_ref.addObject(mat)

# ---------------------------------------------------------------- holes
R = 2.25
holes = defaultdict(list)


def O(l):
    return doc.getObjectsByLabel(l)[0]


def screw(members, start, axis, length, r=R):
    cyl = Part.makeCylinder(r, length, App.Vector(*start), App.Vector(*axis))
    for m in members:
        holes[id(m)].append((m, cyl))


VA, VB = O("Vange_A"), O("Vange_B")
E1, E2 = O("Endestykke_1"), O("Endestykke_2")
B00, B01, B10, B11 = O("Ben_00"), O("Ben_01"), O("Ben_10"), O("Ben_11")
LA, LB = O("Stoetteliste_A"), O("Stoetteliste_B")
DR, MB = O("Midterdrager"), O("Midterben")

# corner M10 through-bolts (Ø11).
#   vange bolt  : gennem vange(45) + ben(95) = 140 mm -> moetrik i Ø20 forsaenkning
#   endestykke  : gennem endestykke(45) + ben(45) = 90 mm -> moetrik direkte, ingen forsaenkning
BOLT_R = 5.5                       # Ø11
CB_R = 10.0                        # Ø20 forsaenkning t. moetrik + skive
CB_DEPTH = 15.0                    # dybde ind i benet fra inderfladen
C = P["clearance"]
Z_V = (C + 30, C + 75)             # 230 / 275
Z_E = (C + 15, C + 50)             # 215 / 250 (below slats, staggered)


def vbolt(leg, vange, xc, y_inner, ydir):
    # runs in Y through vange + 95 mm leg; counterbore the nut at the inner face
    y0 = -2.0 if ydir > 0 else outer_w + 2.0
    for z in Z_V:
        screw([vange, leg], (xc, y0, z), (0, ydir, 0), rt + leg_sy + 10, BOLT_R)
        cb0 = y_inner - ydir * CB_DEPTH
        screw([leg], (xc, cb0, z), (0, ydir, 0), CB_DEPTH + 8, CB_R)


def ebolt(leg, ende, yc, xdir):
    # runs in X through endestykke + 45 mm leg; no counterbore needed
    x0 = -2.0 if xdir > 0 else P["outer_len"] + 2.0
    for z in Z_E:
        screw([ende, leg], (x0, yc, z), (xdir, 0, 0), rt + leg_sx + 10, BOLT_R)


# leg inner faces:  front y=rt+leg_sy(140)  back y=outer_w-rt-leg_sy(1760)
yF, yB = rt + leg_sy, outer_w - rt - leg_sy
xcL, xcR = rt + leg_sx / 2.0, P["outer_len"] - rt - leg_sx / 2.0     # 67.5 / 1942.5
ycF, ycB = rt + leg_sy / 2.0, outer_w - rt - leg_sy / 2.0            # 92.5 / 1807.5
vbolt(B00, VA, xcL, yF, 1);   ebolt(B00, E1, ycF, 1)
vbolt(B10, VA, xcR, yF, 1);   ebolt(B10, E2, ycF, -1)
vbolt(B01, VB, xcL, yB, -1);  ebolt(B01, E1, ycB, 1)
vbolt(B11, VB, xcR, yB, -1);  ebolt(B11, E2, ycB, -1)

# ledger -> vange
z_led_mid = ledger_z + P["ledger_h"] / 2.0
for x in (190, 520, 850, 1180, 1510, 1840):
    screw([LA, VA], (x, 69, z_led_mid), (0, -1, 0), 55)
    screw([LB, VB], (x, 1831, z_led_mid), (0, 1, 0), 55)

# lamel -> ledger (2 per end) + lamel -> centre beam (1 mid)
z_j4 = ledger_z - 5.0
ybeam = beam_y0 + P["drager_t"] / 2.0
for i in range(n):
    xc = slat_x0 + i * pitch + st / 2.0
    Li = O("Lamel_%02d" % i)
    for dx in (-12, 12):
        screw([Li, LA], (xc + dx, 56, z_j4), (0, 0, 1), 72)
        screw([Li, LB], (xc + dx, 1844, z_j4), (0, 0, 1), 72)
    # down through slat into the centre beam
    screw([Li, DR], (xc, ybeam, slat_top + 2), (0, 0, -1), 75)

# centre beam -> endestykker (2 screws each end)
for dz in (-12, 12):
    screw([E1, DR], (-2, ybeam, 235 + dz), (1, 0, 0), 70)
    screw([E2, DR], (P["outer_len"] + 2, ybeam, 235 + dz), (-1, 0, 0), 70)
# centre beam -> centre leg (2 screws down)
for dx in (-15, 15):
    screw([DR, MB], (cx_len + dx, ybeam, ledger_top + 2), (0, 0, -1), 90)

# ---------------------------------------------------------------- cut holes
n_holes = 0
final = []
for o in list(parts):
    entry = holes.get(id(o))
    if not entry:
        final.append(o)
        continue
    shapes = [c for (_m, c) in entry]
    n_holes += len(shapes)
    g = box_group.get(o.Name)
    orig = o.Label
    o.Label = o.Label + "_raw"
    tool = doc.addObject("Part::Feature", o.Name + "_holes")
    tool.Shape = Part.makeCompound(shapes)
    cut = doc.addObject("Part::Cut", o.Name + "_d")
    cut.Base = o
    cut.Tool = tool
    cut.Label = orig
    if g is not None:
        try:
            g.removeObject(o)
        except Exception:
            pass
        g.addObject(cut)
    final.append(cut)
parts = final

doc.recompute()
doc.saveAs(FCSTD)
Part.export(parts, STEP)

vol = sum(o.Shape.Volume for o in parts) / 1e9      # m3
print("=== BUILD OK (LET) ===")
print(f"rail_h={P['rail_h']:.0f} slat={st:.0f}x{P['slat_h']:.0f} n_slats={n} "
      f"pitch={pitch:.1f} gap={pitch-st:.1f}")
print(f"clearance={C:.0f} sleeping={slat_top:.0f} frame_top={frame_top:.0f}")
print(f"parts={len(parts)} screw_holes={n_holes}")
for rho in (450, 470, 500):
    print(f"  vaegt @ {rho} kg/m3: {vol*rho:.1f} kg (trae)")
print(f"SAVED_FCSTD {FCSTD} {os.path.getsize(FCSTD)}")
App.closeDocument("seng_let")

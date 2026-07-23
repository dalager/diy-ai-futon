"""Headless FreeCAD build of the futon bed base (200 x 180 cm).

Run with:  freecad.cmd /home/dalager/projects/seng/scripts/build_bed.py

Builds every part as a separate Part::Feature solid, saves a .FCStd document
and exports a STEP assembly. All coordinates in millimetres.

Coordinate system:  X = length (200 cm), Y = width (180 cm), Z = up.
"""

import os
import FreeCAD as App
import Part

# ---------------------------------------------------------------- parameters
P = dict(
    clearance=200.0,     # free height under frame (vacuuming) = 20 cm
    rail_h=120.0,        # rail height (Z)
    rail_t=45.0,         # rail thickness
    outer_len=2010.0,    # frame outer length (X)  -> side rails 201 cm
    inner_w=1810.0,      # clear width between side rails (Y) = 1800 mattress + 10
    leg=70.0,            # leg cross-section (70 x 70)
    ledger_t=21.0,       # ledger protrusion from rail (Y) - 21x45 liste
    ledger_h=45.0,       # ledger height (Z)
    slat_t=45.0,         # slat width (X) - planed 45 mm batten
    slat_h=70.0,         # slat height on edge (Z) -> aspect 1.6:1, tip-stable
    n_slats=17,
    mattress_l=2000.0,
    mattress_w=1800.0,
    mattress_h=150.0,
)

outer_w = P["inner_w"] + 2 * P["rail_t"]          # 1900
frame_top = P["clearance"] + P["rail_h"]          # 280 (rail top)
slat_top = frame_top + 20.0                       # sleeping surface (slats 20 mm proud)
ledger_top = slat_top - P["slat_h"]               # ledger top supports slat bottom
ledger_z = ledger_top - P["ledger_h"]             # ledger underside (>= clearance)

OUT_DIR = "/home/dalager/projects/seng/cad"
FCSTD = os.path.join(OUT_DIR, "seng.FCStd")
STEP = os.path.join(OUT_DIR, "seng.step")

doc = App.newDocument("seng")
parts = []

# model-tree groups (App-level, work headless)
g_frame = doc.addObject("App::DocumentObjectGroup", "Ramme")
g_legs = doc.addObject("App::DocumentObjectGroup", "Ben")
g_ledger = doc.addObject("App::DocumentObjectGroup", "Stoettelister")
g_slats = doc.addObject("App::DocumentObjectGroup", "Lameller")
g_ref = doc.addObject("App::DocumentObjectGroup", "Reference")

box_group = {}   # obj.Name -> owning group (survives Part::Cut re-parenting)


def box(name, x, y, z, dx, dy, dz, group=None):
    """Add a parametric Part::Box (min corner at x,y,z) so its Length/Width/
    Height show up directly in the FreeCAD Data panel when selected."""
    obj = doc.addObject("Part::Box", name)
    obj.Length = dx   # X
    obj.Width = dy    # Y
    obj.Height = dz   # Z
    obj.Placement = App.Placement(App.Vector(x, y, z), App.Rotation())
    obj.Label = name
    parts.append(obj)
    if group is not None:
        group.addObject(obj)
        box_group[obj.Name] = group
    return obj


rt = P["rail_t"]
# --- side rails (vanger) along X, at the two long edges
box("Vange_A", 0, 0, P["clearance"], P["outer_len"], rt, P["rail_h"], g_frame)
box("Vange_B", 0, outer_w - rt, P["clearance"], P["outer_len"], rt, P["rail_h"], g_frame)

# --- end rails (endestykker) along Y, fitting between the side rails
box("Endestykke_1", 0, rt, P["clearance"], rt, P["inner_w"], P["rail_h"], g_frame)
box("Endestykke_2", P["outer_len"] - rt, rt, P["clearance"], rt, P["inner_w"], P["rail_h"], g_frame)

# --- legs (ben) in the four inner corners, floor -> frame top
lg = P["leg"]
leg_x = [rt, P["outer_len"] - rt - lg]            # 45, 1895
leg_y = [rt, outer_w - rt - lg]                   # 45, 1785
for i, lx in enumerate(leg_x):
    for j, ly in enumerate(leg_y):
        box(f"Ben_{i}{j}", lx, ly, 0, lg, lg, frame_top, g_legs)

# --- ledgers (stoettelister) on inner face of each side rail, between the legs
led_x0 = rt + lg                                  # 115
led_len = (P["outer_len"] - rt - lg) - led_x0     # 1780
box("Stoetteliste_A", led_x0, rt, ledger_z, led_len, P["ledger_t"], P["ledger_h"], g_ledger)
box("Stoetteliste_B", led_x0, outer_w - rt - P["ledger_t"], ledger_z,
    led_len, P["ledger_t"], P["ledger_h"], g_ledger)

# --- slats (lameller) on edge, spanning the width, resting on the ledgers.
# Inset from the legs so the corner through-bolt nuts have clearance.
SLAT_INSET = 40.0
slat_x0 = led_x0 + SLAT_INSET
slat_field = led_len - 2 * SLAT_INSET
n = P["n_slats"]
st = P["slat_t"]
pitch = (slat_field - st) / (n - 1)               # centre-to-centre
for i in range(n):
    x = slat_x0 + i * pitch
    box(f"Lamel_{i:02d}", x, rt, ledger_top, st, P["inner_w"], P["slat_h"], g_slats)

# --- mattress reference (not part of the build)
mat = doc.addObject("Part::Box", "Madras_ref")
mat.Length = P["mattress_l"]
mat.Width = P["mattress_w"]
mat.Height = P["mattress_h"]
mat.Placement = App.Placement(
    App.Vector((P["outer_len"] - P["mattress_l"]) / 2,
               (outer_w - P["mattress_w"]) / 2, slat_top), App.Rotation())
mat.Label = "Madras_ref"
g_ref.addObject(mat)

# ---------------------------------------------------------------- screw holes
# One Ø4.5 hole per screw, cut from each member the screw passes through.
from collections import defaultdict

R = 2.25            # Ø4.5 clearance/representation
holes = defaultdict(list)


def O(label):
    return doc.getObjectsByLabel(label)[0]


def screw(members, start, axis, length, r=R):
    cyl = Part.makeCylinder(r, length, App.Vector(*start), App.Vector(*axis))
    for m in members:
        holes[id(m)].append((m, cyl))


VA, VB = O("Vange_A"), O("Vange_B")
E1, E2 = O("Endestykke_1"), O("Endestykke_2")
B00, B01, B10, B11 = O("Ben_00"), O("Ben_01"), O("Ben_10"), O("Ben_11")
LA, LB = O("Stoetteliste_A"), O("Stoetteliste_B")

# J1 + J2  ramme -> ben : M10 through-bolts (bræddebolt), nut on the inner
#   face. Ø11 clearance hole straight through rail + leg. Vange bolts (Y) and
#   endestykke bolts (X) are staggered in height so they don't cross in the leg.
BOLT_R = 5.5                     # Ø11 for M10
C = P["clearance"]
Z_V = (C + 25, C + 80)           # vange bolt heights (offsets up the rail)
Z_E = (C + 55, C + 110)          # endestykke bolt heights (staggered)
THRU = rt + P["leg"] + 8         # through rail (45) + leg (70) + a little


def vbolt(leg, vange, xc, ydir):
    y0 = -2.0 if ydir > 0 else outer_w + 2.0
    for z in Z_V:
        screw([vange, leg], (xc, y0, z), (0, ydir, 0), THRU, BOLT_R)


def ebolt(leg, ende, yc, xdir):
    x0 = -2.0 if xdir > 0 else P["outer_len"] + 2.0
    for z in Z_E:
        screw([ende, leg], (x0, yc, z), (xdir, 0, 0), THRU, BOLT_R)


vbolt(B00, VA, 80, 1);     ebolt(B00, E1, 80, 1)
vbolt(B10, VA, 1930, 1);   ebolt(B10, E2, 80, -1)
vbolt(B01, VB, 80, -1);    ebolt(B01, E1, 1820, 1)
vbolt(B11, VB, 1930, -1);  ebolt(B11, E2, 1820, -1)

# J3  stoetteliste -> vange  (horizontal, Y), from inside face into rail
z_led_mid = ledger_z + P["ledger_h"] / 2.0
for x in (190, 520, 850, 1180, 1510, 1840):
    screw([LA, VA], (x, 69, z_led_mid), (0, -1, 0), 55)
    screw([LB, VB], (x, 1831, z_led_mid), (0, 1, 0), 55)

# J4  lamel -> stoetteliste  (vertical, up), 2 screws across the 45 mm foot
z_j4 = ledger_z - 5.0
for i in range(n):
    xc = slat_x0 + i * pitch + st / 2.0
    for dx in (-12, 12):
        Li = O("Lamel_%02d" % i)
        screw([Li, LA], (xc + dx, 56, z_j4), (0, 0, 1), 72)
        screw([Li, LB], (xc + dx, 1844, z_j4), (0, 0, 1), 72)

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
    orig_label = o.Label
    o.Label = o.Label + "_raw"           # free up the clean label for the Cut
    tool = doc.addObject("Part::Feature", o.Name + "_holes")
    tool.Shape = Part.makeCompound(shapes)
    cut = doc.addObject("Part::Cut", o.Name + "_d")
    cut.Base = o
    cut.Tool = tool
    cut.Label = orig_label
    if g is not None:
        try:
            g.removeObject(o)   # take the raw box out of the group ...
        except Exception:
            pass
        g.addObject(cut)        # ... and put the holed part in its place
    final.append(cut)
parts = final

doc.recompute()
doc.saveAs(FCSTD)
Part.export(parts, STEP)   # structural parts only, without mattress

gap = pitch - st
print("=== BUILD OK ===")
print(f"outer_len={P['outer_len']:.0f}  outer_w={outer_w:.0f}  frame_top={frame_top:.0f}")
print(f"slat pitch={pitch:.1f}  gap={gap:.1f}  n_slats={n}")
print(f"clearance under frame={P['clearance']:.0f}  sleeping surface (top of slats)={slat_top:.0f}")
print(f"parts={len(parts)}  screw_holes={n_holes}")
print(f"SAVED_FCSTD {FCSTD} {os.path.getsize(FCSTD)}")
print(f"SAVED_STEP {STEP} {os.path.getsize(STEP)}")
App.closeDocument("seng")

"""Add TechDraw drawing pages to cad/seng.FCStd (headless).

Page 1  "Tegning_maalsat"  - the verified dimensioned SVG (cad/seng_tegning.svg)
                             embedded as a symbol -> permanent dimensions.
Page 2  "Projektioner_3D"  - native 1:20 projected views (front/plan/end/iso),
                             3D-linked, ready to dimension interactively.

Run AFTER build_bed.py and make_drawing.py:
    freecad.cmd scripts/add_drawing_page.py
Re-runnable: it removes any existing TechDraw objects first.
"""

import FreeCAD as App

FCSTD = "/home/dalager/projects/seng/cad/seng_let.FCStd"
SVG = "/home/dalager/projects/seng/cad/seng_let_tegning.svg"
SVG_BORE = "/home/dalager/projects/seng/cad/seng_let_boreplan.svg"
TMPL_DIR = App.getResourceDir() + "Mod/TechDraw/Templates/ISO"
TMPL_BLANK = TMPL_DIR + "/A3_Landscape_blank.svg"
TMPL_TITLE = TMPL_DIR + "/A3_Landscape_TD.svg"

doc = App.openDocument(FCSTD)

# --- clean any previous TechDraw objects (re-runnable) -------------------
td = [o for o in doc.Objects if o.TypeId.startswith("TechDraw::")]
order = {"DrawViewDimension": 0, "DrawViewPart": 1, "DrawViewSymbol": 1,
         "DrawSVGTemplate": 2, "DrawPage": 3}
for o in sorted(td, key=lambda o: order.get(o.TypeId.split("::")[1], 1)):
    try:
        doc.removeObject(o.Name)
    except Exception:
        pass

# structural = top-level members of the build groups (Part::Box or Part::Cut
# once screw holes have been cut)
structural = []
for g in doc.Objects:
    if g.TypeId == "App::DocumentObjectGroup" and g.Name in (
            "Ramme", "Ben", "Stoettelister", "Lameller", "Midterdrager"):
        structural += list(g.Group)

# ======================================================= Page 1: dimensioned
with open(SVG) as f:
    svg_content = f.read()

page1 = doc.addObject("TechDraw::DrawPage", "Tegning_maalsat")
page1.Label = "Tegning (maalsat)"
t1 = doc.addObject("TechDraw::DrawSVGTemplate", "Skabelon_maalsat")
t1.Template = TMPL_BLANK
page1.Template = t1

sym = doc.addObject("TechDraw::DrawViewSymbol", "Maalsat_SVG")
sym.Symbol = svg_content
sym.Scale = 0.20            # 1240x1300 px -> ~248x260 mm on A3
sym.X = 210.0              # centre of A3 landscape (420 x 297)
sym.Y = 150.0
page1.addView(sym)

# ------------------------------------------------------- Page 1b: drilling plan
with open(SVG_BORE) as f:
    bore_content = f.read()

page_b = doc.addObject("TechDraw::DrawPage", "Boreplan")
page_b.Label = "Boreplan"
tb = doc.addObject("TechDraw::DrawSVGTemplate", "Skabelon_boreplan")
tb.Template = TMPL_BLANK
page_b.Template = tb

symb = doc.addObject("TechDraw::DrawViewSymbol", "Boreplan_SVG")
symb.Symbol = bore_content
symb.Scale = 0.21           # 1060x1250 px -> ~223x263 mm on A3
symb.X = 210.0
symb.Y = 150.0
page_b.addView(symb)

# ======================================================= Page 2: projections
page2 = doc.addObject("TechDraw::DrawPage", "Projektioner_3D")
page2.Label = "Projektioner (3D-linket)"
t2 = doc.addObject("TechDraw::DrawSVGTemplate", "Skabelon_proj")
t2.Template = TMPL_TITLE
page2.Template = t2

SC = 0.05  # 1:20

# (direction, xdirection, scale, page-X, page-Y)   -- A3 landscape 420 x 297
VIEWS = {
    "Langside": ((0, -1, 0), (1, 0, 0), SC, 115, 235),    # length x height
    "Plan":     ((0, 0, 1), (1, 0, 0), SC, 115, 135),     # length x width
    "Gavl":     ((-1, 0, 0), (0, 1, 0), SC, 300, 235),    # width x height
    "Iso":      ((1, -1, 1), None, 0.030, 310, 110),      # pictorial
}

made = {}
for name, (direction, xdir, scale, x, y) in VIEWS.items():
    v = doc.addObject("TechDraw::DrawViewPart", name)
    v.Source = structural
    v.Direction = App.Vector(*direction)
    if xdir:
        v.XDirection = App.Vector(*xdir)
    v.ScaleType = "Custom"
    v.Scale = scale
    page2.addView(v)
    made[name] = v

# first recompute builds the projected geometry ...
doc.recompute()
# ... THEN position the views (X/Y only stick after geometry exists)
for name, v in made.items():
    v.X = float(VIEWS[name][3])
    v.Y = float(VIEWS[name][4])

# optional: fill title block fields if the template exposes them
try:
    t2.setEditableText("Title", "Sengebund til futon 200 x 180 cm")
    t2.setEditableText("Scale", "1:20")
except Exception:
    pass

doc.recompute()
doc.save()

pages = [o.Label for o in doc.Objects if o.TypeId == "TechDraw::DrawPage"]
views = [o.Name for o in doc.Objects if o.TypeId == "TechDraw::DrawViewPart"]
print("PAGES", pages)
print("VIEWS", views)
print("SYMBOL_bytes", len(svg_content))
print("SAVED", FCSTD)
App.closeDocument(doc.Name)

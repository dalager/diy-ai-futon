# Sengebund — LET variant (futon 180 × 200 cm)

Parametrisk CAD-projekt for en let, ubehandlet **futon-sengebund**: slank 45×95-ramme,
17 kvadratiske 45×45-lameller der flugter med rammens overkant, og en langsgående
midterdrager (45×45) på ét midterben. Ben skæres af afskær (45×95) — ingen
trykimprægneret stolpe, ingen lim. Udvendige mål = madrasmålet (180 × 200 cm), så
madrassen ligger plant af med kanten.

Hele modellen bygges headless i **FreeCAD** fra ét parametersæt, og tegninger,
boreplan, renderinger og en samlet PDF genereres af scripts.

| Isometrisk | Understel (lameller skjult) |
|:---:|:---:|
| ![Isometrisk](cad/screenshots/seng_let_01_iso.png) | ![Understel](cad/screenshots/seng_let_07_understel.png) |

## Kort specifikation

| | |
|---|---|
| Udvendige mål | 180 × 200 cm (= madras, flush) |
| Vægt | ~48 kg (fyr/gran) |
| Ramme | 45 × 95, boltet i hjørnerne (M10) |
| Lameller | 17 × 45×45, flugter med rammens overkant |
| Midtersupport | drager 45×45 + ét midterben |
| Frihøjde | 200 mm under ramme / 205 mm under drager (robotstøvsuger) |
| Ben | 4 × 45×95 af **afskær** ♻️ (ubehandlet, ingen lim) |
| Pris (Silvan, jul. 2026) | ~1.631 kr |

## Dokumenter

- **[sengebund_let.md](sengebund_let.md)** — konstruktion, statik, samlinger, højder.
- **[BOM_let.md](BOM_let.md)** — materialeliste, skæreplan, indkøb og forbehold.
- **[cad/seng_let_dokumentation.pdf](cad/seng_let_dokumentation.pdf)** — samlet PDF med
  renderinger øverst + begge dokumenter (genereres, se nedenfor).

## Projektstruktur

```
seng/
├── sengebund_let.md              # hoveddokument (konstruktion + statik)
├── BOM_let.md                    # materialeliste / indkøb
├── scripts/
│   ├── build_bed_let.py          # bygger 3D-modellen -> .FCStd + .step
│   ├── make_drawing_let.py       # målsat tegning -> seng_let_tegning.svg
│   ├── make_drilling_plan_let.py # boreplan -> seng_let_boreplan.svg
│   ├── add_drawing_page_let.py   # TechDraw-sider ind i .FCStd
│   └── make_pdf_let.py           # samlet PDF (renderinger + begge .md)
└── cad/
    ├── seng_let.FCStd            # FreeCAD-model (parametrisk, med huller)
    ├── seng_let.step             # neutral CAD-udveksling
    ├── seng_let_tegning.svg      # målsat tegning
    ├── seng_let_boreplan.svg     # boreplan
    ├── seng_let_dokumentation.pdf
    └── screenshots/              # 8 FreeCAD-renderinger (.png)
```

## Genopbygning af hele kæden

Alt afledes af parametrene øverst i `scripts/build_bed_let.py` (mål, antal lameller,
profiler). Ret dem og genkør kæden i rækkefølge:

```bash
# 1. Byg 3D-modellen (headless FreeCAD) -> cad/seng_let.FCStd + .step
freecad.cmd scripts/build_bed_let.py

# 2. Målsat tegning (ren Python) -> cad/seng_let_tegning.svg
python3 scripts/make_drawing_let.py

# 3. Boreplan (ren Python) -> cad/seng_let_boreplan.svg
python3 scripts/make_drilling_plan_let.py

# 4. TechDraw-sider ind i .FCStd (headless FreeCAD)
freecad.cmd scripts/add_drawing_page_let.py

# 5. Samlet PDF (renderinger + begge .md)
~/.pyenv/versions/3.12.3/bin/python scripts/make_pdf_let.py
```

### Renderinger (FreeCAD GUI)

De 8 screenshots i `cad/screenshots/` tages i FreeCAD-GUI'en (via freecad-MCP), fordi
farver og kamera kræver et grafisk miljø. Efter en headless genopbygning (trin 1)
skal modellen genindlæses i GUI'en, træfarverne påføres pr. byggegruppe, filen gemmes,
og de 8 views eksporteres med `View3DInventor.saveImage(...)`.

Farvepaletten (matcher tegningerne):

| Del | Farve |
|-----|-------|
| Ramme | `#d8c9a8` |
| Ben (inkl. midterben) | `#b99763` |
| Støttelister | `#c9b487` |
| Lameller | `#efe7d3` |
| Midterdrager | `#c2a266` |

## Afhængigheder

- **FreeCAD** (snap: `freecad.cmd` til headless build; GUI til renderinger).
- **freecad-mcp** ([neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp)) —
  renderingstrinnet styres via FreeCAD-MCP-serveren, så en agent/klient kan genindlæse
  modellen, sætte farver og kalde `saveImage(...)` i den kørende FreeCAD-GUI.
  **Serveren er ikke checket ind i dette repo** (ligger i `deps/freecad-mcp`, som er
  git-ignoreret) — klon den fra upstream og konfigurér den i `.mcp.json`; FreeCAD-GUI'en
  skal køre med MCP-addon'et aktivt:
  ```bash
  git clone https://github.com/neka-nat/freecad-mcp.git deps/freecad-mcp
  ```
  (Selve build- og tegningsscriptene kræver **ikke** MCP — kun de 8 screenshots i
  `cad/screenshots/`.)
- **Python** til tegningerne (kun standardbibliotek).
- **PDF:** `markdown`, `pymdown-extensions` og `weasyprint` — installeret i pyenv-miljøet
  `~/.pyenv/versions/3.12.3`. Kør `make_pdf_let.py` med netop den python. Fonte:
  DejaVu Sans Mono (ASCII-diagrammer) + Noto Color Emoji (♻️ ✅ ⚠️).

## Noter

- **Træfarver er ikke persistente over en headless genopbygning:** trin 1 skriver et
  nyt `.FCStd` uden ViewObject-farver (headless FreeCAD kan ikke sætte dem). Påfør dem
  igen i GUI'en efter genopbygning, før du tager screenshots.
- **Midterdrager 45×45** er et bevidst valg: den flush lamel ville med en 45×70-drager
  kun give 180 mm frihøjde under midten; 45×45 bevarer 205 mm og bruger samme profil
  som lamellerne. Til gengæld er drageren et grænsetilfælde omkring L/300 — se
  statik-afsnittet i [sengebund_let.md](sengebund_let.md).

## Licens

[MIT](LICENSE) © 2026 Christian Dalager

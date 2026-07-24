# Sengebund LET variant — futon 200 × 180 cm

Let udgave af [sengebund_med_stoetteliste.md](sengebund_med_stoetteliste.md):
slankere 45×95-ramme, kvadratiske 45×45-lameller og en langsgående **midterdrager
på ét midterben**, der halverer lamelspændet. **~54 kg** mod standarddesignets
~72 kg. CAD: `cad/seng_let.FCStd`, tegninger `cad/seng_let_tegning.svg` +
`cad/seng_let_boreplan.svg`, indkøb i [BOM_let.md](BOM_let.md).

## Konstruktionsprincip

```
      ← 200 cm (længde) →
   ┌────────────────────────────┐   ┐
   │ ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪ │   │  ← 45×45 lameller (17 stk)
   │ ═══════ midterdrager ══════ │   │     spænder tværs, hviler på
   │ ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪  ▪ │   │     3 punkter: liste-drager-liste
   └────────────────────────────┘   ┘  180 cm (bredde)
   ▙             ▪              ▟
   ben        midterben         ben
```

- **To vanger 45×95** med 4 hjørneben + **to endestykker** = stiv ramme (som
  standarddesignet, blot 25 mm lavere profil).
- **Midterdrager 45×70 på højkant** løber i længderetningen, centreret, båret af
  ét **midterben** og fastgjort til endestykkerne. Lamellernes frie spænd falder
  fra ~1780 mm til ~860 mm.
- **Lameller 45×45**: det halverede spænd gør den lille kvadratiske profil stiv
  nok — og kvadratisk tværsnit (slankhed 1:1) kan ikke vælte. Ingen indeslutning
  af madrassen.

## Højde og frihøjde (20 cm til støvsugning)

```
   top af lameller      315 mm  ┄┄┄┄ (sovefladen, før madras)
   top af ramme         295 mm  ─────┐
   lamel-underkant      270 mm       │  vange 95 mm
   underkant ramme      200 mm  ─────┘  ← 20 cm FRIHØJDE
   underkant drager     200 mm  ─────   ← drageren flugter med rammens underkant
   gulv                   0 mm  ▂▂▂▂▂▂
```

- **Hjørneben = 200 + 95 = 295 mm. Midterben = 200 mm** (drageren 200→270,
  overkant flugter med støttelisternes overkant i kote 270).
- Frihøjden er præcis 200 mm overalt — også under drageren. Bemærk: **nul
  margin**; på ujævnt gulv kan en robotstøvsuger på præcis 20 cm strejfe.
- Sovehøjde ≈ 31,5 cm (bund) + 15–18 cm futon = **ca. 47–50 cm**
  (2,5 cm lavere end standarddesignet).

## Materialeliste (fyr/gran, høvlet)

| Del | Antal | Dimension | Længde |
|-----|-------|-----------|--------|
| Vanger (langsider) | 2 | 45 × 95 mm | 201 cm |
| Endestykker | 2 | 45 × 95 mm | 181 cm |
| Lameller | 17 | 45 × 45 mm | 181 cm |
| Midterdrager | 1 | 45 × 70 mm | 192 cm |
| Støttelister | 2 | 21 × 45 mm | 178 cm |
| Hjørneben | 4 | 70 × 70 mm | 29,5 cm |
| Midterben | 1 | 70 × 70 mm | 20 cm |

Drageren (192 cm) løber mellem endestykkernes indersider. Alle 5 ben skæres af
én 70×70×2100-stolpe (4 × 295 + 1 × 200 = 1380 mm). Mål som bygget i
CAD-modellen (`cad/seng_let.FCStd`).

## Lamelafstand og udluftning

- **Lamel 45 mm + mellemrum ~63 mm → c/c 108,4 mm** giver 17 lameller, der
  starter lige ved benene (end-gab 70 mm = benets bredde, symmetrisk).
  Åbningsareal ~58 % = god udluftning nedefra — samme spalte som
  standarddesignet, uproblematisk for en futon.
- Vil du justere: `n_slats` i `scripts/build_bed_let.py` + genkør scriptsættet
  (16 lameller sparer ~1,7 kg og giver ~71 mm spalte — i den brede ende for en
  blød futon).

## Holder det til to personer?

Kort statik-tjek (fyr, E ≈ 10 GPa), verificeret mod CAD-modellens geometri:

- **Lameller 45 × 45, frit spænd 862 mm** (støtteliste → drager): 50 kg
  punktlast midt på ét fag giver ~2 mm nedbøjning (grænse L/300 ≈ 2,9 mm).
  Lamellen er kontinuert over drageren, hvilket reelt gør den stivere endnu.
- **Vælte-stabilitet:** 45 × 45 er kvadratisk (slankhed 1:1) — domino-problemet
  fra høje tynde lameller findes ikke. Skruerne i enderne er kun lås.
- **Midterdrager 45 × 70 på højkant, 2 fag à ~935 mm:** bærer ~halvdelen af
  totallasten; nedbøjning < 1 mm pr. fag.
- **Vanger 45 × 95, spænd ~178 cm:** nedbøjning 1–2 mm ved fuld last. Den lette
  ramme er marginalt mere "levende" end 45×120 — drageren kompenserer i midten.

## Samlinger og stabilitet

### Fastgørelsesskema (alle huller er lagt ind i CAD-modellen)

| Samling | Type | Antal | Placering |
|---------|------|-------|-----------|
| Lamel → støtteliste | skrue 4,5 × 70 | 17 × 2 × 2 = 68 | lodret op, 2 på tværs af foden |
| Lamel → midterdrager | skrue 4,5 × 70 | 17 × 1 = 17 | lodret ned gennem lamel midtfor |
| Støtteliste → vange | skrue 4,5 × 70 | 2 × 6 = 12 | vandret, fra listens inderside |
| Midterdrager → endestykke | skrue 4,5 × 70 + **vinkelbeslag** | 4 + 2 beslag | vandret gennem endestykke i dragerens endetræ; beslag tager lasten |
| Midterdrager → midterben | **vinkelbeslag** | 2 beslag | på dragerens sider ned på benet |
| Vange → ben | **M10 bræddebolt, gennemgående** | 4 × 2 = 8 | Ø11, højde 230/275, møtrik på inderside |
| Endestykke → ben | **M10 bræddebolt, gennemgående** | 4 × 2 = 8 | Ø11, højde 215/250 (under lamellerne) |

**Hjørnerne boltes** som i standarddesignet: M10 × 140 lige gennem ramme (45) +
ben (70) = 115 mm, bræddebolt-hoved udenpå, skive + møtrik på indersiden.
Endestykke-boltene sidder under lamel-underkanten (270), så møtrikkerne går fri
af første/sidste lamel.

### To ting man skal vide, før man borer/skruer

1. **Boltkryds i benene:** vange- og endestykke-boltene krydser hinanden
   vinkelret inde i benet med kun **15 mm lodret afstand** (4 mm træ mellem
   Ø11-hullerne, parret 230/215). Bor vinkelret — borelære eller
   søjleboremaskine — og bor alle 4 huller i et ben, **før** boltene sættes i.
2. **Ingen lodrette 70 mm-skruer i midterbenet:** drageren er selv 70 mm høj,
   så en 4,5 × 70 ovenfra får 0 mm fat i benet. Brug vinkelbeslag (eller
   2 stk. 6 × 120 — modellens lodrette huller ved midterbenet passer til den
   løsning).

## Forskelle fra standarddesignet — hurtig oversigt

| | Standard (~72 kg) | Let (~54 kg) |
|---|---|---|
| Ramme | 45 × 120 | 45 × 95 |
| Lameller | 17 × 45×70 på højkant | 17 × 45×45 kvadratisk |
| Midtersupport | ingen | drager 45×70 + midterben |
| Sovehøjde (bund) | 340 mm | 315 mm |
| Spalte | ~63 mm | ~63 mm |
| Pris (Silvan, jul. 2026) | ~1.590 kr | ~1.690 kr |

Vægtbesparelsen (~18 kg) er gevinsten — prisen er ~100 kr højere, fordi 45×45
er dyr pr. bræt. Se [BOM_let.md](BOM_let.md) for indkøbsliste og forbehold.

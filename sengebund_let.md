# Sengebund LET variant — futon 200 × 180 cm

Let, ubehandlet sengebund til en futon: slank 45×95-ramme, kvadratiske
45×45-lameller og en langsgående **midterdrager på ét midterben**, der halverer
lamelspændet. Ben skæres af afskær (45×95), ingen lim, ingen trykimprægneret træ.
**Vægt ~52 kg.** CAD: `cad/seng_let.FCStd`, tegninger `cad/seng_let_tegning.svg` +
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

- **To vanger 45×95** med 4 hjørneben + **to endestykker** = stiv ramme.
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
- Sovehøjde ≈ 31,5 cm (bund) + 15–18 cm futon = **ca. 47–50 cm**.

## Materialeliste (fyr/gran, høvlet)

| Del | Antal | Dimension | Længde |
|-----|-------|-----------|--------|
| Vanger (langsider) | 2 | 45 × 95 mm | 201 cm |
| Endestykker | 2 | 45 × 95 mm | 181 cm |
| Lameller | 17 | 45 × 45 mm | 181 cm |
| Midterdrager | 1 | 45 × 70 mm | 192 cm |
| Støttelister | 2 | 21 × 45 mm | 178 cm |
| Hjørneben (af afskær) | 4 | 45 × 95 mm | 29,5 cm |
| Midterben (af afskær) | 1 | 45 × 70 mm | 20 cm |

Drageren (192 cm) løber mellem endestykkernes indersider. **Benene købes ikke —
de skæres af afskær** ♻️: de fire hjørneben (45×95) af vange-/endestykke-afskærene
(390/390/590/590 mm), midterbenet (45×70) af drager-afskæret (480 mm). Ingen
trykimprægneret stolpe, ingen lim. Hjørnebenet vender med 45 mm-fladen mod
endestykket og 95 mm-fladen mod vangen. Mål som bygget i CAD-modellen
(`cad/seng_let.FCStd`).

## Lamelafstand og udluftning

- **Lamel 45 mm + mellemrum ~63 mm → c/c 108,4 mm** giver 17 lameller, der
  starter 70 mm inde fra endestykket (symmetrisk hjørnezone i begge ender).
  Åbningsareal ~58 % = god udluftning nedefra — uproblematisk for en futon.
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
- **Vanger 45 × 95, spænd ~178 cm:** nedbøjning 1–2 mm ved fuld last —
  drageren afstiver desuden i midten.

## Samlinger og stabilitet

### Fastgørelsesskema (alle huller er lagt ind i CAD-modellen)

| Samling | Type | Antal | Placering |
|---------|------|-------|-----------|
| Lamel → støtteliste | skrue 4,5 × 70 | 17 × 2 × 2 = 68 | lodret op, 2 på tværs af foden |
| Lamel → midterdrager | skrue 4,5 × 70 | 17 × 1 = 17 | lodret ned gennem lamel midtfor |
| Støtteliste → vange | skrue 4,5 × 70 | 2 × 6 = 12 | vandret, fra listens inderside |
| Midterdrager → endestykke | skrue 4,5 × 70 + **vinkelbeslag** | 4 + 2 beslag | vandret gennem endestykke i dragerens endetræ; beslag tager lasten |
| Midterdrager → midterben | **vinkelbeslag** | 2 beslag | på dragerens sider ned på benet |
| Vange → ben (95mm-akse) | **M10×140 bræddebolt + Ø20 forsænket møtrik** | 4 × 2 = 8 | Ø11, højde 230/275, møtrik i Ø20-lomme i benets inderside |
| Endestykke → ben (45mm-akse) | **M10×100 bræddebolt, gennemgående** | 4 × 2 = 8 | Ø11, højde 215/250 (under lamellerne), møtrik fladt, ingen forsænkning |

**Hjørnerne boltes.** Fordi benet er 45×95 af afskær, er de to akser forskellige:
- **Vange-aksen:** M10 × 140 gennem vange (45) + ben (**95**) = 140 mm. Da bolten
  præcis fylder hullet, sidder skive + møtrik i en **Ø20 forsænkning (~15 mm dyb)**
  boret i benets inderflade. (Vil du undgå forsænkning: brug M10 × 160 her.)
- **Endestykke-aksen:** M10 × **100** gennem endestykke (45) + ben (**45**) = 90 mm —
  møtrik sidder fladt på indersiden, ingen forsænkning. **Brug ikke M10×140 her** —
  den ville stritte ~50 mm bar gevind ind under lamellen (rammer den lige akkurat
  ikke, men er grim og formålsløs). Boltene sidder under lamel-underkanten (270),
  så møtrikkerne går fri af første/sidste lamel.

### To ting man skal vide, før man borer/skruer

1. **Boltkryds i benene:** vange- og endestykke-boltene krydser hinanden
   vinkelret inde i benet med kun **15 mm lodret afstand** (4 mm træ mellem
   Ø11-hullerne, parret 230/215). Bor vinkelret — borelære eller
   søjleboremaskine — og bor alle 4 huller (+ de 2 Ø20-forsænkninger på
   vange-aksen) i et ben, **før** boltene sættes i.
2. **Ingen lodrette 70 mm-skruer i midterbenet:** drageren er selv 70 mm høj,
   så en 4,5 × 70 ovenfra får 0 mm fat i benet. Brug vinkelbeslag (eller
   2 stk. 6 × 120 — modellens lodrette huller ved midterbenet passer til den
   løsning).

## Kort specifikation

| | |
|---|---|
| Vægt | ~52 kg |
| Ramme | 45 × 95 |
| Lameller | 17 × 45×45 kvadratisk |
| Midtersupport | drager 45×70 + midterben |
| Ben | 4 × 45×95 af **afskær** ♻️ (ubeh., ingen lim) |
| Sovehøjde (bund) | 315 mm |
| Spalte | ~63 mm |
| Pris (Silvan, jul. 2026) | ~1.623 kr |

Benene er 100 % ubehandlede afskær (ingen trykimprægneret stolpe, ingen lim). Se
[BOM_let.md](BOM_let.md) for indkøbsliste og forbehold.

# Sengebund med støtteliste — futon 200 × 180 cm

Minimalistisk sengebund: to vanger med ben + tværgående lameller på højkant.
En af de stiveste og mest luftige måder at lave en sengebund på, når det gøres
rigtigt. Beregnet til at bære to voksne uden midterben.

## Konstruktionsprincip

```
      ← 200 cm (længde) →
   ┌────────────────────────────┐   ┐
   │ ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮ │   │  ← lameller på højkant
   │ ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮  ▮ │   │     (spænder tværs, 180 cm)
   └────────────────────────────┘   ┘  180 cm (bredde)
   ▙                            ▟
   ben                          ben        vange = bærende side m. ben
```

- **To vanger** (langsider) løber i sengens længde (200 cm) og bærer hele lasten
  ned i **4 ben** i hjørnerne.
- **To endestykker** binder vangerne sammen til en stiv rektangulær ramme
  (vigtigt — uden dem kan sengen "skæve"/parallelforskyde sig sideværts).
- **Lameller på højkant** ligger tværs, hviler på en **støtteliste** skruet
  indvendigt på hver vange, og skrues fast i begge ender. På højkant giver træet
  langt størst stivhed pr. kg — derfor kan bunden være let uden midterben.

## Højde og frihøjde (20 cm til støvsugning)

Kravet er **20 cm fri højde under sengen** til støvsuger-/robotmundstykke.
Det laveste hængende element er vangens (og støttelistens) underkant — den skal
derfor sidde 200 mm over gulv.

```
   top af lameller     ~340 mm  ┄┄┄┄ (sovefladen, før madras)
   top af vange         320 mm  ─────┐
                                     │  vange 120 mm
   underkant vange      200 mm  ─────┘  ← 20 cm FRIHØJDE
                                     │  ben (frihøjde-del) 200 mm
   gulv                   0 mm  ▂▂▂▂▂▂
```

- **Benlængde = 200 mm frihøjde + 120 mm vangehøjde = 320 mm.**
- **Frihøjden (200 mm) sættes af benene/vangen**, ikke af støttelisten. Støttelisten
  sidder så dens overkant bærer lamellernes underkant i kote 270 mm (så sovefladen
  bliver 340 mm med 70 mm lameller). Dens underkant ligger dermed ~225 mm over gulv
  — altså stadig godt over de 20 cm frihøjde.
- **Fastgørelse af lameller:** to skruer 4,5 × 70 mm **op gennem støttelisten** ind i
  hver lamelende (forbor Ø4 i listen ved hver lamelmidte, c/c 103 mm — hullerne bliver
  samtidig din afstands-skabelon). Forbor lamellen 3 mm. To skruer på tværs af den
  45 mm brede fod låser lamellen mod at vælte.
- Sovehøjde ≈ 34 cm (bund) + 15–18 cm futon = **ca. 49–52 cm**. Vil du højere/
  lavere: justér kun benlængden — frihøjden er de 20 cm så længe rammens underkant
  er 200 mm over gulv.

## Materialeliste (fyr/gran, høvlet)

| Del | Antal | Dimension | Længde |
|-----|-------|-----------|--------|
| Vanger (langsider) | 2 | 45 × 120 mm | 201 cm |
| Endestykker | 2 | 45 × 120 mm | 181 cm |
| Lameller (på højkant) | 17 | 45 × 70 mm | 181 cm |
| Støttelister | 2 | 21 × 45 mm | 178 cm |
| Ben | 4 | 70 × 70 mm | 32 cm |

Endestykker og lameller har længden **181 cm** = indvendigt lysmål mellem vangerne
(180 cm madras + 1 cm slør). Støttelisterne (178 cm) løber mellem benene, så de
ikke støder ind i benene i hjørnerne. Mål er som bygget i CAD-modellen
(`cad/seng.FCStd`).

## Lamelafstand og udluftning

- **Lamel 45 mm + mellemrum ~58 mm → c/c ca. 103 mm** giver 17 lameller. Feltet er
  rykket 40 mm ind fra benene i hver ende, så hjørneboltenes møtrikker har plads.
  Åbningsareal ~56 % = god udluftning nedefra, hvilket er vigtigt for en futon
  (den kan ellers samle fugt/mug mod en tæt bund).
- 60 mm mellemrum er uproblematisk for en fast, tyk futon — den "hænger" ikke ned
  i mellemrummene.
- Vil du have det tættere/blødere: gå ned mod 40 mm mellemrum (flere lameller,
  lidt tungere). Vil du spare vægt: gå op mod 90 mm — stadig fint bæremæssigt,
  blot lidt større spring i støtten.

## Holder det til to personer?

Kort statik-tjek (fyr, E ≈ 10 GPa):

- **Lameller 45 × 70 på højkant, spænd 180 cm:** ved to voksne (regnet 250–300 kg)
  er nedbøjningen ~4 mm (grænse L/300 ≈ 6 mm), og sikkerhedsmargin på brudstyrke er
  rigelig. Højkant-orienteringen er nøglen — samme lamel lagt fladt ville være
  ~2,4× blødere.
- **Vælte-stabilitet:** 45 × 70 har slankhed **1,6 : 1** (mod 4,3 : 1 for en
  22 × 95). En høj, tynd lamel på højkant er ellers en dominobrik, der kan lægge sig
  ned ved ensrettet/cyklisk vandret tryk fra madrassen. Den brede 45 mm fod (med to
  skruer på tværs pr. ende) gør den stabil — uden at madrassen skal indesluttes.
- **Vanger 45 × 120, spænd 200 cm mellem benene:** nedbøjning ~1 mm, spænding langt
  under det tilladte. Kunne principielt gøres slankere (45 × 95), men 120 mm giver
  et roligt, ikke-fjedrende leje.

Altså rigelig kapacitet uden at være overdimensioneret.

## Samlinger og stabilitet

- **Hjørner (ramme):** brug sengebolte/kryds-beslag eller lange konstruktionsskruer
  i forboret træ — gør den stiv og evt. adskillelig.
- **Ben:** skru/bolt i hjørnet, gerne med et lille hjørneknæ (gusset) indvendigt
  mod vridning.
- **Lameller skrues i begge ender** ned i støttelisten (to skruer pr. ende, se
  Højde-afsnittet) — låser dem mod at vælte.

### Fastgørelsesskema (alle huller er lagt ind i CAD-modellen)

| Samling | Type | Antal | Placering |
|---------|------|-------|-----------|
| Lamel → støtteliste | skrue 4,5 × 70, Ø4,5 | 17 × 2 × 2 = 68 | lodret op, 2 på tværs af 45 mm-foden |
| Støtteliste → vange | skrue 4,5 × 70, Ø4,5 | 2 × 6 = 12 | vandret, fra listens inderside |
| Vange → ben | **M10 bræddebolt, gennemgående** | 4 × 2 = 8 | Ø11 gennem vange + ben, møtrik på inderside, højde 225/280 |
| Endestykke → ben | **M10 bræddebolt, gennemgående** | 4 × 2 = 8 | Ø11 gennem endestykke + ben, møtrik på inderside, højde 255/310 (forskudt) |

**Hjørnerne boltes, ikke skrues** — de optager al vridning og skal kunne efterspændes
og adskilles. Boltene (M10 × 140) går **lige igennem** ramme (45) + ben (70) = 115 mm;
bræddebolt-hovedet sidder udenpå, spændeskive + møtrik på indersiden. Vange- og
endestykkebolte er forskudt i højden, så de ikke krydser inde i benet, og lamelfeltet
er rykket 40 mm ind, så møtrikkerne har plads. Forbor lamel/liste 3 mm mod flækning.
- Vil du helt undgå enhver fjedring i midten: en enkelt **langsgående midterdrager
  (45 × 70) med ét midterben** halverer lamelspændet og lader dig gøre alt endnu
  slankere/lettere. Ikke nødvendigt med ovenstående mål — det er et valg, ikke et
  krav. (Bemærk: et midterben skal også respektere de 16 cm frihøjde til gulvet.)

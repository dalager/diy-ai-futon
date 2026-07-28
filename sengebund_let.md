# Sengebund LET variant — futon 200 × 180 cm

Let, ubehandlet sengebund til en futon: slank 45×95-ramme, kvadratiske
45×45-lameller der **flugter med rammens overkant**, og en langsgående
**midterdrager (45×45) på ét midterben**, der halverer lamelspændet. Udvendige mål
**180 × 200 cm = madrasmålet** (madrassen ligger plant af med kanten, ingen liste
op om). Ben skæres af afskær (45×95), ingen lim, ingen trykimprægneret træ.
**Vægt ~48 kg.** CAD: `cad/seng_let.FCStd`, tegninger `cad/seng_let_tegning.svg` +
`cad/seng_let_boreplan.svg` + `cad/seng_let_liste_boreplan.svg`, indkøb i
[BOM_let.md](BOM_let.md).

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
- **Midterdrager 45×45** løber i længderetningen, centreret, båret af ét
  **midterben** og fastgjort til endestykkerne. Lamellernes frie spænd falder
  fra ~1710 mm til ~810 mm.
- **Lameller 45×45** flugter med rammens overkant (top i kote 295): det halverede
  spænd gør den lille kvadratiske profil stiv nok — og kvadratisk tværsnit
  (slankhed 1:1) kan ikke vælte. Madrassen hviler plant på ramme + lameller i
  samme kote, ingen indeslutning.

## Højde og frihøjde (20 cm til støvsugning)

```
   top af lameller = top af ramme  295 mm  ┄┄┄┄ (sovefladen — lameller flugter med rammen)
   lamel-underkant                 250 mm  ─────┐
   støtteliste-overkant            250 mm       │  vange 95 mm
   underkant ramme                 200 mm  ─────┘  ← 20 cm FRIHØJDE
   underkant drager (45×45)        205 mm  ─────   ← 5 mm over rammens underkant
   gulv                              0 mm  ▂▂▂▂▂▂
```

- **Hjørneben = 200 + 95 = 295 mm. Midterben = 205 mm** (drageren 45×45 sidder
  205→250, overkant flugter med støttelisternes overkant i kote 250, som bærer
  lamellerne).
- Frihøjden er 200 mm under rammen og **205 mm under drageren** (5 mm margin — en
  robotstøvsuger på 20 cm går fri overalt, også under midterdrageren).
- Sovehøjde ≈ 29,5 cm (bund) + 15–18 cm futon = **ca. 44–48 cm**.

## Materialeliste (fyr/gran, høvlet)

| Del | Antal | Dimension | Længde |
|-----|-------|-----------|--------|
| Vanger (langsider) | 2 | 45 × 95 mm | 200 cm |
| Endestykker | 2 | 45 × 95 mm | 171 cm |
| Lameller | 17 | 45 × 45 mm | 171 cm |
| Midterdrager | 1 | 45 × 45 mm | 191 cm |
| Støttelister | 2 | 21 × 45 mm | 177 cm |
| Hjørneben (af afskær) | 4 | 45 × 95 mm | 29,5 cm |
| Midterben (af afskær) | 1 | 45 × 45 mm | 20,5 cm |

Drageren (191 cm) løber mellem endestykkernes indersider. **Benene købes ikke —
de skæres af afskær** ♻️: de fire hjørneben (45×95) af vange-/endestykke-afskærene
(400/400/690/690 mm), midterbenet (45×45) af drager-afskæret (490 mm). Ingen
trykimprægneret stolpe, ingen lim. Hjørnebenet vender med 45 mm-fladen mod
endestykket og 95 mm-fladen mod vangen. Mål som bygget i CAD-modellen
(`cad/seng_let.FCStd`).

## Lamelafstand og udluftning

- **Lamel 45 mm + mellemrum ~63 mm → c/c 107,8 mm** giver 17 lameller, der
  starter 70 mm inde fra endestykket (symmetrisk hjørnezone i begge ender).
  Åbningsareal ~58 % = god udluftning nedefra — uproblematisk for en futon.
- Vil du justere: `n_slats` i `scripts/build_bed_let.py` + genkør scriptsættet
  (16 lameller sparer ~1,7 kg og giver ~71 mm spalte — i den brede ende for en
  blød futon).

## Holder det til to personer?

Kort statik-tjek (fyr, E ≈ 10 GPa), verificeret mod CAD-modellens geometri:

- **Lameller 45 × 45, frit spænd ~810 mm** (støtteliste → drager): 50 kg
  punktlast midt på ét fag giver ~1,7 mm nedbøjning (grænse L/300 ≈ 2,7 mm).
  Lamellen er kontinuert over drageren, hvilket reelt gør den stivere endnu.
- **Vælte-stabilitet:** 45 × 45 er kvadratisk (slankhed 1:1) — domino-problemet
  fra høje tynde lameller findes ikke. Skruerne i enderne er kun lås.
- **Midterdrager 45 × 45, 2 fag à ~955 mm:** bærer ~halvdelen af totallasten.
  Kvadratisk 45×45 (mod den tidligere 45×70 på højkant) giver ~3–4 mm nedbøjning
  pr. fag ved fuld last — **et grænsetilfælde omkring L/300 (~3,2 mm)**, men
  uproblematisk under en eftergivende futon. Vil du have mere margin: sæt drageren
  på højkant som 45×70 igen (koster 20 mm frihøjde under midten) eller tilføj et
  andet midterben.
- **Vanger 45 × 95, spænd ~191 cm:** nedbøjning 1–2 mm ved fuld last —
  drageren afstiver desuden i midten.

## Samlinger og stabilitet

### Fastgørelsesskema (alle huller er lagt ind i CAD-modellen)

| Samling | Type | Antal | Placering |
|---------|------|-------|-----------|
| Lamel → støtteliste | spånskrue 4,5 × 60 | 17 × 2 × 2 = 68 | lodret op gennem listens 45 mm højde → 15 mm i lamellen, 2 på tværs af foden |
| Lamel → midterdrager | spånskrue 4,5 × 60 | 17 × 1 = 17 | lodret ned gennem lamel midtfor → 15 mm i drageren |
| Støtteliste → vange | spånskrue 4,5 × **50** | 2 × 6 = 12 | vandret, fra listens inderside → 29 mm i vangen |
| Midterdrager → endestykke | spånskrue **5 × 80** + **vinkelbeslag** | 4 + 2 beslag | vandret gennem endestykke → 35 mm i dragerens endetræ; beslag tager lasten |
| Midterdrager → midterben | spånskrue **5 × 80** lodret ned | 2 | ned gennem 45 mm drager → 35 mm i benets endetræ |
| Vange → ben (95mm-akse) | **M10×160 bræddebolt + skive + møtrik + kontramøtrik** | 4 × 2 = 8 | Ø12, højde 230/275, 20 mm gevind ude på benets inderside — **ingen forsænkning** |
| Endestykke → ben (45mm-akse) | **M8×100 bræddebolt, gennemgående** | 4 × 2 = 8 | **Ø10**, højde 215/250 i endetræet (fri af lamellerne ved x≥115), møtrik + stor skive fladt, ingen forsænkning |

### Tre skruelængder — og hvorfor

Alle skruer er **spånskruer (universalskruer), undersænket hoved, Torx, delgevind**.
Elforzinket rækker fint til en ubehandlet indendørs seng; rustfri er kun nødvendig
udendørs. Undtagelsen er vinkelbeslagene, der skal have **beslagskruer** med fladt
hoved — en undersænket skrue trækker sig ned i beslagets hul og kan flække det.

| Længde | Antal | Hvor | Hvorfor lige den |
|--------|-------|------|------------------|
| **4,5 × 60** | 85 | lamel → liste, lamel → drager | 45 mm nær-del + 15 mm fat. Begge samlinger *hviler*, så skruen bærer nul vægt og er ren lås — 15 mm i sidetræ er rigeligt |
| **4,5 × 50** | 12 | støtteliste → vange | 21 + 45 = **66 mm stak**: en 70'er ville stikke 4 mm ud på vangens yderside. 50 giver 29 mm fat |
| **5 × 80** | 6 | drager → endestykke og → midterben | Eneste samlinger i **endetræ**, hvor holdeevnen er 50–75 % af sidetræs. 35 mm fat i stedet for 15 |

Bemærk at `lamel → støtteliste` går **lodret gennem listens 45 mm højde** (ikke gennem
de 21 mm) og derefter op i lamellen — skruen bryder altså ikke ud i sovefladen ved
kote 295. De 6 lange sidder i endetræ, hvor der er ubegrænset plads bagved (drageren
er 1910 mm, midterbenet 205 mm højt), så længden koster ingenting dér.

**Delgevind redder dig ikke — forboringen gør.** En 4,5 × 60 delgevind har kun ~20–25 mm
glat skaft, men skruen skal gennem 45 mm nær-del, så gevindet starter inde i nær-delen
alligevel. Det er **Ø5-gennemgangshullet**, der lader gevindet spille frit og hovedet
trække delene sammen. Delgevind er en fordel oveni, ikke en erstatning.

### Forboringsskema

Alle 103 skruesamlinger skal have **gennemgangshul i den nære del** — det er det, der
lader skruehovedet trække delene sammen. Pilothul i den fjerne del er obligatorisk
overalt hvor det er **endetræ** eller tæt på en ende/kant, hvilket her er alt undtagen
de 17 ned i drageren.

| Samling | Antal | Skrue | Gennemgang (nær del) | Pilot (fjern del) | Forsænk |
|---------|-------|-------|----------------------|-------------------|---------|
| Lamel → støtteliste | 68 | 4,5 × 60 | **Ø5** lodret gennem listens 45 mm højde | **Ø3** × 20 mm i lamel | Ø10 i listens underside |
| Lamel → midterdrager | 17 | 4,5 × 60 | **Ø5** gennem 45 mm lamel | Ø3 × 20 mm (kan undværes) | Ø10, sænk 2–3 mm **under** sovefladen |
| Støtteliste → vange | 12 | 4,5 × 50 | **Ø5** vandret gennem 21 mm liste | **Ø3** × 35 mm i vange | Ø10 i listens inderside |
| Midterdrager → endestykke | 4 | **5 × 80** | **Ø5,5** gennem 45 mm endestykke | **Ø3,5** × 40 mm i dragerens **endetræ** | **Ø11** på gavlens yderside |
| Midterdrager → midterben | 2 | **5 × 80** | **Ø5,5** gennem 45 mm drager | **Ø3,5** × 40 mm i benets **endetræ** | **Ø11** i dragerens overkant |
| Vange → ben | 8 bolte | **M10×160** | **Ø12** gennem 45+95 | — | ingen — 20 mm gevind ude |
| Endestykke → ben | 8 bolte | **M8×100** | **Ø10** gennem 45+45 | — | ingen — møtrik fladt |
| Vinkelbeslag | 2 stk. | beslagskruer | — | Ø2,5 | — |

Tommelfingerreglerne bag tallene, i fyr/gran: gennemgang = skruediameter + 0,5 mm;
pilot ≈ 65 % af skruediameteren (Ø3 til en 4,5, Ø3,5 til en 5); forsænkning Ø ≈ 2 ×
skruediameteren. **Forsænk dog til Ø11 for 5×80-skruerne** — deres hoved er Ø10, så en
Ø10-forsænkning er lige præcis for lille. De 4,5-skruer har Ø9-hoved, hvor Ø10 rækker.

**Bor du skal bruge:** Ø2,5 · Ø3 · Ø3,5 · Ø5 · Ø5,5 · **Ø10** · Ø12 · plus **én
kegleforsænker 90°, Ø16, HSS, sekskantskaft**. Ø3,5 og Ø5,5 er udelukkende til de 6
lange 5 mm-skruer; Ø10 kun til de 8 endestykke-bolte, Ø12 kun til de 8 vange-bolte.
(Ø9/Ø11 er den "rigtige" størrelse for M8/M10, men ikke altid til at få — Ø10/Ø12 er
næste almindelige størrelse op, se boltkryds-advarslen nedenfor.) **Ingen Ø20-forstner**
— den hørte til den forsænkede møtrik, som er droppet.

**Forsænkeren er ét bor, ikke to.** Ø16 er keglens største diameter, ikke hullets — du
styrer diameteren med dybden, så Ø10 og Ø11 er samme bor i to dybder. 90° er vinklen på
metriske træskruehoveder (82° er til metal og passer ikke). Bor hullet **først** og
forsænk bagefter, så keglen har noget at centrere sig i; kør 400–800 o/min med let tryk,
ellers hopper den og efterlader et trekantet hul. Prøv af på et afskær, og sæt tape på
boret i den rigtige dybde.

⚠️ **23 af de 103 forsænkninger er ikke valgfri:**
- **De 17 ned i midterdrageren** sidder i sovefladen — sænk dem **2–3 mm under**
  overfladen, ikke bare plant.
- **De 4 i gavlen** sidder på sengens synlige yderside.
- **De 2 ned i midterbenet** ligger ved x = 985 og 1015 i drageren, hvor **lamel 8
  hviler** (den dækker 977,5–1022,5). Stikker de hoveder 1 mm op, vipper lamellen.

De øvrige 80 sidder på støttelistens under- og inderside, hvor intet ses og intet
hviler. Dér er forsænkning pænt, men ikke nødvendigt.

⚠️ **De 2 skruer ned i midterbenet er det sted, hvor der er mindst træ.** De sidder
±15 mm fra benets midte (`build_bed_let.py:197`), og benet er kun 45×45 — så skruen er
**7,5 mm fra benets kant**, og det er endetræ. Med et Ø5,5-hul er der knap 5 mm træ ud
til fladen. Pilothullet er ikke valgfrit dér: en 5 mm skrue uden pilot i endetræ så tæt
på kanten flækker benet. Borer du alligevel i hånden, kan du frit rykke de to huller ind
til **±10 mm** fra midten (12,5 mm til kanten) — så skal gennemgangshullerne i drageren
bare flyttes tilsvarende. CAD-modellen har dem stadig på ±15.

**Hvor de 34 lamelhuller skal bores i støttelisten:** se det dedikerede ark
`cad/seng_let_liste_boreplan.svg`, der har alle 34 afstande målt fra listens ene ende.
Nøgletal: hullerne sidder **midt i listens 21 mm** (10,5 mm fra begge kanter), parvis
**24 mm fra hinanden**, med **107,8 mm c/c** mellem lamellerne. Første hul **10,5 mm**
inde, sidste **10,5 mm** fra den anden ende — mønsteret er symmetrisk om listens midte
(L8 sidder præcis på 885 mm). Mål alle 34 fra samme ende med båndmål; step ikke 107,8
af 16 gange, så hober fejlen sig op. Bor listen **før** den skrues på vangen — de
forborede huller er selv afstands-jiggen for lamellerne.

**Hjørnerne boltes.** Fordi benet er 45×95 af afskær, er de to akser forskellige:
- **Vange-aksen:** **M10 × 160** gennem vange (45) + ben (**95**) = 140 mm træ, så der
  stikker **20 mm** ud på benets inderflade: skive 2,5 + møtrik 8 + **kontramøtrik 8**
  = 18,5 mm, altså reelt plant. **Ingen forsænkning.** Brug ikke M10×140 her — den
  ender præcis plant med træet og har nul gevind til møtrikken. En Ø20-lomme i benet
  (som tidligere versioner foreskrev) løser det ikke: en M10-møtrik kræver en top på
  23–25 mm, og en større lomme bryder ind i endestykke-boltens hul 15 mm under.
  Kontramøtrikken er værd at have — ubehandlet fyr svinder det første år, og boltede
  træsamlinger løsner sig, når træet krymper.
- **Endestykke-aksen:** **M8 × 100** gennem endestykke (45) + ben (**45**) = 90 mm —
  møtrik + stor skive (Ø24) sidder fladt på indersiden, ingen forsænkning. Hul **Ø10**
  (Ø9 er den "rigtige" størrelse, men ikke altid til at få).
  Der er kun **1,5 mm til overs**, så ingen kontramøtrik og ingen nyloc på den akse —
  og hjørnet skal presses helt sammen, før møtrikken sættes på. **Brug ikke M10×140
  her** — den ville stritte ~50 mm bar gevind ind under lamellen (rammer den lige
  akkurat ikke, men er grim og formålsløs). Boltene sidder i endestykkets endetræ ved
  x < 90, mens første/sidste lamel starter ved x = 115, så møtrikkerne går fri.

**Hvorfor M8 rækker på den akse:** belastningen er ~2,3 kN fordelt på 4 hjørner, altså
~600 N pr. hjørne på 4 bolte. Grænsen sættes ikke af bolten (en M8 kan ~8,8 kN i
forskydning) men af **træets hulrandstyrke**: 8 mm × 45 mm × ~25 MPa ≈ 9 kN. M10 gav
11 kN. Begge ligger 15–30 gange over behovet, så de 2 mm diameter er uden betydning
her. **Til gengæld skal skiven være stor:** en M8-planskive er kun Ø16, og møtrikken
trækker sig ind i træet. Brug Ø20–24 karosseri-/firkantskive — den gør mere for
samlingen end boltdiameteren.

### Tre ting man skal vide, før man borer/skruer

1. **Boltkryds i benene:** vange- og endestykke-boltene krydser hinanden
   vinkelret inde i benet med kun **15 mm lodret afstand** — kun **4 mm** træ
   mellem Ø12- og Ø10-hullet (parret 230/215; var 5 mm ved Ø11/Ø9). Bor
   vinkelret — borelære eller søjleboremaskine — og bor alle 4 huller i et
   ben, **før** boltene sættes i. Marginen er blevet mindre, så dette er
   endnu vigtigere nu.
2. **Midterdrager → midterben skrues lodret ovenfra:** drageren er kun 45 mm
   høj, så en 5 × 80 ned gennem drageren får 35 mm fat i benet (2 skruer,
   modellens lodrette huller ved midterbenet). Ingen vinkelbeslag nødvendigt her —
   det var kun et krav dengang drageren var 70 mm høj.
3. **Hullerne i støttelisten skal være Ø5, ikke Ø4:** Ø4 er et *pilothul* — gevindet
   ville gribe i listen og jække de to dele fra hinanden i stedet for at spænde dem
   sammen, og med kun ~8 mm træ til hver side af hullet flækker en 21 mm tyk liste let
   langs åren. Bor derfor lodret og præcist. Til gengæld er det rigtigt at skrue
   lamellerne **nedefra og op**: den nære del (listen) skal have gennemgangshullet, og
   de forborede huller i listen virker som afstands-jig, så lamellerne automatisk
   lander på plads.

## Kort specifikation

| | |
|---|---|
| Vægt | ~48 kg |
| Udvendige mål | 180 × 200 cm (= madras, flush) |
| Ramme | 45 × 95 |
| Lameller | 17 × 45×45 kvadratisk, flugter med rammen |
| Midtersupport | drager 45×45 + midterben |
| Ben | 4 × 45×95 af **afskær** ♻️ (ubeh., ingen lim) |
| Sovehøjde (bund) | 295 mm |
| Spalte | ~63 mm |
| Pris (jul. 2026) | 1.376,40 kr træ (Silvan) + skruer/beslag + 159,80 kr bolte (jem&fix) |

Benene er 100 % ubehandlede afskær (ingen trykimprægneret stolpe, ingen lim). Se
[BOM_let.md](BOM_let.md) for indkøbsliste og forbehold.

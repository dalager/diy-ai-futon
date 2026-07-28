# Materialeliste (BOM) — LET variant, sengebund futon 200 × 180 cm

Til den lette variant (CAD: `cad/seng_let.FCStd`): slank 45×95 ramme, 17 kvadratiske
45×45 lameller der flugter med rammens overkant, midterdrager (45×45) på ét midterben.
Udvendige mål 180 × 200 cm (= madras, flush). **Ben skæres af afskær** (45×95) — ingen
trykimprægneret stolpe, ingen lim. **Vægt ~48 kg.**

**Status:** alt er købt hos Silvan bortset fra vange-boltene, der skal hentes hos
jem&fix. Priser fra Silvan.dk (juli 2026, ekskl. levering).

## ✔ Købt hos Silvan

### Træ (fyr/gran, ubehandlet, høvlet)

| Til | Vare | Antal | Pris/stk | I alt |
|-----|------|-------|----------|-------|
| Lameller (17 × 1710) | [Reglar 45×45×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-reglar-45x45x2400-mm-ubehandlet-hoevlet-7700-9804949) | 17 | 64,80 | 1101,60 |
| Vanger + endestykker | [Reglar 45×95×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-reglar-45x95x2400-mm-ubehandlet-hoevlet-7700-9804953) | 4 | 43,80 | 175,20 |
| Midterdrager (1910) | [Reglar 45×45×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-reglar-45x45x2400-mm-ubehandlet-hoevlet-7700-9804949) | 1 | 64,80 | 64,80 |
| Ben (4 hjørne + 1 midter) | **Skæres af afskær — købes ikke** ♻️ | 0 | — | 0 |
| Støttelister (2 × 1770) | [Forskalling 21×45×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-forskalling-21x45x2400-mm-ubehandlet-hoevlet-7700-9804930) | 2 | 17,40 | 34,80 |

**Træ i alt 1.376,40 kr** — ingen benstolpe, benene bliver af afskær. Drageren er
45×45 (samme profil som lamellerne), så der er kun ét reglar-tværsnit foruden
rammens 45×95.

### Skruer, bolte og beslag

| Til | Vare (som købt) | Pakke | Bruges |
|-----|-----------------|-------|--------|
| Lamel → liste, lamel → drager | Simpson **TTZNFS 4,5 × 60**, art. 74485 | 200 stk | 85 |
| Støtteliste → vange | Simpson **TTZNFS 4,5 × 50**, art. 74484 | 200 stk | 12 |
| Drager → endestykke og → midterben | Simpson **TTZNFS 5,0 × 80**, art. 76540 | 100 stk | 6 |
| Beslagskruer | Simpson **TTUFP 4,0 × 20**, art. 74519 | 200 stk | ~12 |
| Endestykke → ben | KRAM **bræddebolt M8 × 100** m/ møtrikker, varenr. 6774056 | 12 stk | 8 |
| Skiver, endestykke | KRAM **M8 spændeskive 8,4 × 24 × 2,0**, varenr. 6774773 | 30 stk | 8 |
| Skiver, vange | KRAM **M10 spændeskive 10,5 × 30 × 2,5**, varenr. 6774774 | 15 stk | 8 |
| Drager-samlinger | **Simpson AC35350** vinkelbeslag | 2 stk | 2 |

Skal noget genkøbes, er kravene: **spånskrue med undersænket hoved, Torx og delgevind**.
Delgevind er en fordel, men ikke afgørende — skruerne går gennem 45 mm nær-del, og en
4,5×60 har kun ~20–25 mm glat skaft, så det er **Ø5-gennemgangshullet**, der gør
klemmearbejdet. Impreg®+ er en udendørs-coating, altså mere end nødvendigt indendørs,
men uskadeligt; elforzinket rækker.

**Vinkelbeslagene er undtagelsen:** de skal have beslagskruer med **fladt** hoved
(TTUFP), ikke undersænkede spånskruer, som trækker sig ned i beslagets hul og kan
flække det.

⚠️ **De 5,0 × 80 har Ø10-hoved** — forsænk til **Ø11**, ikke Ø10, ellers går hovedet
ikke plant. De 4,5-skruer har Ø9-hoved, hvor Ø10 rækker.

## ⬜ Mangler — hentes hos jem&fix

| Til | Vare | Antal | Pris |
|-----|------|-------|------|
| Vange-bolte (gennem 140 mm) | NKT bræddebolt DIN 603 **M10 × 160**, 2-pak à 39,95 | 8 (4 pk) | **159,80 kr** |
| Kontramøtrikker, vange | Løse **M10-møtrikker** (bolten leverer selv den første) | 8 | ~25 kr |

⚠️ **De 8 M10×140, der allerede er købt, skal byttes** — de kan ikke bruges, se nedenfor.
jem&fix har ikke M10×160 i storpakke; 4 × 2-pak er den eneste vej til 8 stk. Der er
heller ikke noget mellem 140 og 160: en M10×120 når ikke gennem de 140 mm træ, og næste
trin op er M10×200, som ville stritte 60 mm ud.

**Ingen forsænkning — brug M10×160 på vange-aksen.** Vange-aksen går gennem 45+95 =
**140 mm**, så en M10×140 ender præcis plant med træet og har **nul** gevind til møtrik.
En tidligere version af denne BOM løste det med en Ø20-lomme i benets inderside; **det
virker ikke** — en M10-møtrik er 17 mm over fladerne og kræver en top på ~23–25 mm,
som aldrig kommer ned i Ø20. Lommen kan heller ikke bores større, for ved Ø25 bryder
den ind i endestykke-boltens hul 15 mm under. **Ø20-forstnerboret er derfor slettet fra
listen.**

Med M10×160 stikker der 20 mm ud på benets inderside:

```
20,0 mm  bolten stikker ud (160 − 140)
−2,5 mm  spændeskive
−8,0 mm  møtrik
−8,0 mm  kontramøtrik
─────────
 1,5 mm  til overs — reelt plant
```

**Brug kontramøtrikken.** Sengen er ubehandlet fyr, der svinder det første år, og
boltede træsamlinger løsner sig, når træet krymper. Alternativt en hattemøtrik, der
dækker gevindet helt.

**M8×100 på endestykke-aksen passer — men kun med 1,5 mm til overs.** Stakken er 90 mm,
der kommer 10 mm ud, og M8-møtrik (6,5) + Ø24-skive (2,0) bruger 8,5 af dem. Derfor:
**ingen kontramøtrik og ingen nyloc på den akse** (en M8 nyloc er ~8 mm høj og løber tør
for gevind), og **hjørnet skal presses helt sammen** — er der 2 mm luft mellem endestykke
og ben, når møtrikken ikke gevindet. Spænd vange-boltene først, så hjørnet er lukket.

**M8 rækker rigeligt dér:** grænsen sættes af træets hulrandstyrke (8 × 45 × ~25 MPa ≈
9 kN), ikke af bolten, og hvert hjørne bærer kun ~600 N. M10 gav 11 kN — begge er 15–30
gange over. Men **skiven skal være stor**: en M8-planskive er kun Ø16, og møtrikken
trækker sig ind i træet.

**Firkanthalsen bider IKKE i disse huller.** M10-halsen er ~11,9 mm og M8-halsen ~9,2 mm
— begge nu 1–2 mm mindre end hullerne (Ø12 hhv. Ø10), fordi Ø11/Ø9-bor ikke altid kan
skaffes. Uden den bidende pasning kan bolten snurre med, når du spænder møtrikken: hold
hovedet med en fastnøgle eller en tang.

## Skæreplan

| Emne | Køb | Skæres til | Afskær (genbruges til ben) |
|------|-----|------------|----------------------------|
| Lameller | 17 × 45×45×2400 | 1 à 1710 pr. stk | 17 × 45×45×690 |
| Vanger | 2 × 45×95×2400 | à 2000 | **2 × 45×95×400** |
| Endestykker | 2 × 45×95×2400 | à 1710 | **2 × 45×95×690** |
| Midterdrager | 1 × 45×45×2400 | à 1910 | **1 × 45×45×490** |
| Støttelister | 2 × 21×45×2400 | à 1770 | 2 × 21×45×630 |

### Ben af afskær (♻️ køb intet nyt træ)

| Ben | Antal | Af afskær | Skær til |
|-----|-------|-----------|----------|
| Hjørneben (45×95) | 4 | de fire 45×95-afskær (400, 400, 690, 690) | à 295 |
| Midterben (45×45) | 1 | 45×45-drager-afskæret (490) | à 205 |

Hjørnebenet vender med **45 mm-fladen mod endestykket** og **95 mm-fladen mod vangen**
(så de 45 mm holder sig fri af lamelfeltet ved x=115). Midterbenet har ingen bolte —
det skrues op i drageren med 2 lodrette 5×80 ovenfra, så orienteringen er ligegyldig.

## Fastgørelse (antal)

| Samling | Type | Antal |
|---------|------|-------|
| Lamel → støtteliste | spånskrue 4,5 × 60 | 68 |
| Lamel → midterdrager | spånskrue 4,5 × 60 | 17 |
| Støtteliste → vange | spånskrue 4,5 × **50** | 12 |
| Midterdrager → endestykke | spånskrue **5 × 80** **+ vinkelbeslag** | 4 + 2 beslag |
| Midterdrager → midterben | spånskrue **5 × 80** lodret ned (2 stk) | 2 |
| Vange → ben (95mm-akse) | **M10×160** bræddebolt + skive + møtrik + **kontramøtrik** | 8 |
| Endestykke → ben (45mm-akse) | **M8×100** bræddebolt (gennemgående, møtrik + stor skive fladt) | 8 |

Skruer i alt 103 i **tre længder**: **85 stk. 4,5×60** + **12 stk. 4,5×50**
(kun støtteliste → vange) + **6 stk. 5×80** (kun endetræ). Bolte: 16.
Vinkelbeslag: 2 (kun drager→endestykke). **Ingen møtrik-forsænkninger** — se boltafsnittet.

⚠️ **Brug ikke 60 mm til støtteliste → vange.** Det er den eneste samling, der går
**vandret** gennem listens 21 mm tykkelse: 21 + 45 mm vange = **66 mm stak**. En 70 mm
skrue stikker 4 mm ud på vangens yderside; en 60 mm efterlader kun 6 mm. 4,5×50 giver
29 mm fat og 16 mm margin. (`Lamel → støtteliste` går derimod **lodret** gennem listens
45 mm *højde* + 15 mm op i lamellen, så dér er 60 mm rigtig — og den bryder ikke ud i
sovefladen.)

⚠️ **De 6 i endetræ skal være 5×80.** Drager → endestykke og drager → midterben er de
eneste samlinger, der går i **endetræ**, hvor holdeevnen er 50–75 % af sidetræs. Med
60 mm ville de kun få 15 mm fat dér; 80 mm giver 35 mm. Der er ubegrænset plads bagved
(drageren er 1910 mm lang, midterbenet 205 mm højt), så længden koster ingenting.

## Forboring

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

**Bor du skal have:** Ø2,5 · Ø3 · **Ø3,5** · Ø5 · **Ø5,5** · **Ø10** · Ø12 · plus **én
kegleforsænker 90°, Ø16, HSS, sekskantskaft** (~60–100 kr). Ø20-forstneren er ikke
længere nødvendig. (Ø9/Ø11 er den "rigtige" gennemgangsstørrelse for M8/M10, men ikke
altid til at få — Ø10/Ø12 er næste almindelige størrelse op, se advarslen om
firkanthalsen og boltkrydset i benene nedenfor.)

**Køb ikke et kombineret undersænkbor.** De borer forhul og forsænker i én bevægelse med
én diameter — men her skal den nære del have Ø5 gennemgang og den fjerne Ø3 pilot, to
forskellige diametre i samme hul. En løs kegleforsænker er den rigtige.

**Ø16 er keglens største diameter, ikke hullets.** Du styrer diameteren med dybden, så
Ø10 og Ø11 er samme bor i to dybder. 90° er vinklen på metriske træskruehoveder — 82°
er til metal og passer ikke. Regel: gennemgang = skruediameter + 0,5 mm, pilot ≈ 65 % af
skruediameteren. Ø3,5 og Ø5,5 er udelukkende til de 6 lange 5 mm-skruer.

⚠️ **Forsænk til Ø11 for 5×80-skruerne.** Simpson TTZNFS 5,0 har et **Ø10-hoved**, så en
Ø10-forsænkning er lige præcis for lille til at hovedet går plant. De 4,5-skruer har
Ø9-hoved, så dér er Ø10 rigeligt.

⚠️ **Hullerne i støttelisten er Ø5 gennemgangshuller — ikke Ø4.** Med Ø4 griber gevindet
i listen og jækker delene fra hinanden i stedet for at spænde dem sammen, og en 21 mm
tyk liste flækker let langs åren. De to endetræs-samlinger (drager → endestykke og →
midterben) **skal** have Ø3,5 pilothul; en skrue i endetræ virker ellers som en kile.

⚠️ **Mindst træ af alle: de 2 skruer ned i midterbenet.** De sidder ±15 mm fra benets
midte, og benet er kun 45×45 — altså **7,5 mm fra kanten**, i endetræ. Med Ø5,5 er der
knap 5 mm træ ud til fladen, så pilothullet er kritisk dér. Borer du i hånden, kan du
frit rykke dem ind til ±10 mm (12,5 mm til kanten); så flyttes gennemgangshullerne i
drageren tilsvarende. CAD-modellen har dem på ±15.

✅ **Drager → midterben skrues lodret ovenfra**: drageren er kun 45 mm høj, så en
5×80 ned gennem drageren får 35 mm fat i benet (2 skruer). Det tidligere krav om
vinkelbeslag/6×120 gjaldt kun den gamle 70 mm-høje drager.

⚠️ **Ingen Ø20-forsænkning mere.** Tidligere versioner af dette dokument bad om en
Ø20-lomme ~15 mm dyb i benets inderside ved hvert vange-bolthul. **Bor den ikke** — en
M10-møtrik kan ikke spændes dernede, og lommen ville desuden bryde ind i endestykke-
boltens hul 15 mm under. M10×160 løser det uden lommer.

## Ærlige forbehold

- **Pris:** træet er 1.376,40 kr hos Silvan (prischecket). Skruer, bolte, skiver og
  beslag er også købt hos Silvan, men de faktiske priser er ikke registreret her.
  Udestående: **159,80 kr** for de 8 M10×160 hos jem&fix + ~25 kr for kontramøtrikker.
  Benene er gratis (afskær), men 45×45-lameller er dyre pr. bræt. Du får et 100 %
  ubehandlet, lim-frit design med genbrugte afskær.
- **Overskud fra pakkerne:** skruerne er købt i 100/200-pakker, så der bliver 115 stk.
  4,5×60, 188 stk. 4,5×50, 94 stk. 5,0×80 og ~188 beslagskruer tilovers. Det var det
  billigste — mindre pakker fandtes ikke i de længder.
- **Ben af afskær (♻️):** ingen trykimprægneret stolpe, ingen lim. Ben-tværsnittet
  er 45×95 (slankt, men rammen er en stiv boltet kasse, så benene står i ren tryk —
  rigeligt). Ingen firkantet ubehandlet stolpe fandtes hos jem&fix, Silvan eller
  Bauhaus; alle massive stolper er trykimprægneret eller malet.
- **Lamelspalte ~63 mm** — uproblematisk for en futon.
- **Midterdrager-samling:** drageren fastgøres til endestykkerne med skruer i
  endetræ + vinkelbeslag (endetræ alene er svagt). Til midterbenet skrues
  2 stk. 5×80 lodret ned ovenfra — den 45 mm høje drager giver 35 mm fat i benet.
  De 2 skruer sidder kun 7,5 mm fra benets kant i endetræ, så pilothullet er kritisk.
- **Drager 45×45 (grænsetilfælde):** den kvadratiske drager er blødere end den
  gamle 45×70 på højkant — ~3–4 mm nedbøjning pr. fag ved fuld last, lige omkring
  L/300. Uproblematisk under en eftergivende futon; vil du have mere stivhed, kan
  drageren sættes på højkant som 45×70 (koster 20 mm frihøjde under midten).
- **Boltkryds i benene:** vange- og endestykke-bolte passerer hinanden med kun
  15 mm lodret afstand — kun **4 mm** træ mellem Ø12- og Ø10-hullet (var 5 mm ved
  Ø11/Ø9). Bor vinkelret (borelære/søjleboremaskine) og bor alle 4 huller i et ben,
  før boltene monteres — marginen er blevet mindre, så det er endnu vigtigere nu.

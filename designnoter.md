# Designnoter — sengebund LET, futon 180 × 200 cm

Arbejdsnote til **hvorfor** sengen ser ud som den gør: konstruktionsvalg, statik,
dimensionering, forkastede løsninger og indkøbsregnskab.

**[byggevejledning.md](byggevejledning.md) er facit** for mål, hulplaceringer,
materialeliste og fremgangsmåde. Denne note gentager dem ikke — ret altid vejledningen
først, og skriv kun begrundelsen her. Selve geometrien kommer fra
`scripts/build_bed_let.py`, og CAD-modellen (`cad/seng_let.FCStd`) er sandheden om
hulplaceringer.

## Parametersæt

Alt afledes af `P` i `scripts/build_bed_let.py`:

| Parameter | Værdi | Bemærkning |
|-----------|-------|------------|
| `clearance` | 200 | frihøjde til gulv |
| `rail_h` / `rail_t` | 95 / 45 | rammens profil (var 120 i den tunge variant) |
| `outer_len` | 2000 | = madraslængden, flush |
| `inner_w` | 1710 | → udvendig bredde 1800 = madrasbredden |
| `ledger_t` / `ledger_h` | 21 / 45 | støtteliste, 45 mm står lodret |
| `slat_t` / `slat_h` | 45 / 45 | kvadratisk lamel |
| `n_slats` | 17 | → c/c 107,8 mm, spalte 62,8 mm |
| `drager_t` / `drager_h` | 45 / 45 | samme profil som lamellerne |

Afledte kotehøjder: soveflade og rammens overkant 295, lamel-underkant og
støtteliste-overkant 250, rammens underkant 200, dragerens underkant 205.

## Konstruktionsvalg

**Udvendige mål = madrasmålet.** Madrassen ligger plant af med kanten i stedet for at være
indelukket af en liste. Det gør rammen til det synlige møbel og sparer 90 mm i begge
retninger. Konsekvensen er, at lamellerne skal flugte med rammens overkant, ikke ligge nede
i den.

**Kvadratiske 45×45-lameller.** Slankhed 1:1 kan ikke vælte, så dominoeffekten fra høje,
tynde lameller findes ikke, og skruerne i enderne er ren lås uden at bære vægt. Prisen er,
at en 45×45 ikke kan spænde 1710 mm alene — den kræver midtersupport. Lamellerne er også
den dyreste post i materialelisten (45×45-reglar er dyre pr. bræt).

**Midterdrager på ét midterben.** Halverer det frie lamelspænd fra 1710 til ~810 mm, og
det er den ene ændring, der gør de kvadratiske lameller mulige. Lamellerne er kontinuerte
over drageren, hvilket gør dem stivere end to fritliggende fag.

**Drager 45×45 frem for 45×70 på højkant.** Kvadratisk drager holder frihøjden på 205 mm
under midten; en 45×70 med samme overkant ender i kote 180 og bryder altså 20 cm-kravet fra
robotstøvsugeren. Det koster stivhed — se statikken. Sidegevinst: kun to reglar-tværsnit i
hele projektet, 45×45 og 45×95.

**20 cm frihøjde** er sat af støvsugerrobotten, ikke af æstetikken. Dragerens underkant
ligger 5 mm over rammens underkant, så der er fri passage overalt.

**Ben af afskær.** Der fandtes ingen firkantet, ubehandlet stolpe hos jem&fix, Silvan eller
Bauhaus — alle massive stolper er trykimprægnerede eller malede. Afskærene fra vanger,
endestykker og drager giver præcis de fem ben, sengen skal have, og resultatet er 100 %
ubehandlet og lim-frit. Ben-tværsnittet 45×95 er slankt for et sengeben, men rammen er en
stiv boltet kasse, så benene står i ren tryk.

**Boltede hjørner, ikke skruede.** Fire gennemgående bolte pr. hjørne kan efterspændes,
når ubehandlet fyr svinder det første år. Skruer i endetræ kan ikke. Det er også derfor,
vange-aksen har kontramøtrik.

## Statik

Fyr, E ≈ 10 GPa, regnet på CAD-modellens geometri. Komfortgrænsen L/300:

| Del | Frit spænd | Nedbøjning ved fuld last | L/300 |
|-----|-----------|--------------------------|-------|
| Lamel 45×45 | 810 mm | ~1,7 mm (50 kg punktlast midt på ét fag) | 2,7 mm |
| Midterdrager 45×45 | 2 fag à 955 mm | ~3–4 mm pr. fag | ~3,2 mm |
| Vange 45×95 | 1910 mm | 1–2 mm | ~6,4 mm |

**Drageren er et grænsetilfælde** lige omkring L/300 — designets svageste punkt.
Vurderingen er, at det er uproblematisk under en eftergivende futon, men det er et bevidst
valg for at holde frihøjden. Vil man have margin: et ekstra midterben koster kun et hul og
ingen frihøjde; 45×70 på højkant er stivere, men sender frihøjden under midten ned på
180 mm.

Vangen er kraftigt overdimensioneret, og drageren afstiver den desuden på midten.

**Bolte:** totallasten er ~2,3 kN fordelt på fire hjørner = ~600 N pr. hjørne på to bolte.
Grænsen sættes ikke af bolten (en M8 tåler ~8,8 kN i forskydning) men af **træets
hulrandstyrke**: 8 mm × 45 mm × ~25 MPa ≈ 9 kN for M8, ~11 kN for M10. Begge ligger 15–30
gange over behovet, så de 2 mm boltdiameter er uden betydning. Det, der betyder noget, er
**skivens størrelse** — en M8-planskive er kun Ø16, og møtrikken trækker sig ind i træet.
Derfor Ø24 karosseri-/firkantskive på endestykke-aksen.

## Skruerne — hvorfor tre længder

103 skruesamlinger: **85 × 4,5×60**, **12 × 4,5×50**, **6 × 5×80**.

- **4,5 × 60** til lamel → liste og lamel → drager. 45 mm nær-del + 15 mm fat. Begge
  samlinger *hviler*, så skruen bærer nul vægt og er ren lås; 15 mm i sidetræ er rigeligt.
- **4,5 × 50** til støtteliste → vange. Den eneste samling, der går **vandret** gennem
  listens 21 mm: 21 + 45 = 66 mm stak, så en 70'er stikker 4 mm ud på vangens yderside, og
  en 60'er efterlader kun 6 mm. 50 giver 29 mm fat og 16 mm margin.
- **5 × 80** til drager → endestykke og drager → midterben. De eneste samlinger i
  **endetræ**, hvor holdeevnen er 50–75 % af sidetræs: 35 mm fat i stedet for 15. Der er
  ubegrænset plads bagved (drageren 1910 mm, midterbenet 205 mm), så længden koster
  ingenting.

**Forboringsreglerne** bag tallene i vejledningen, i fyr/gran: gennemgang = skruediameter
+ 0,5 mm; pilot ≈ 65 % af skruediameteren; forsænkning Ø ≈ 2 × skruediameteren.
Undtagelsen er 5×80-skruerne, hvis hoved er Ø10 — dér skal forsænkningen være Ø11, for en
Ø10-forsænkning er lige præcis for lille. 4,5-skruerne har Ø9-hoved, hvor Ø10 rækker.

**Delgevind redder ikke samlingen — forboringen gør.** En 4,5×60 delgevind har kun ~20–25
mm glat skaft, men skruen skal gennem 45 mm nær-del, så gevindet starter inde i nær-delen
alligevel. Det er Ø5-gennemgangshullet, der lader gevindet spille frit og hovedet trække
delene sammen. Delgevind er en fordel oveni, ikke en erstatning. Samme grund til at listens
huller **skal** være Ø5 og ikke Ø4: med Ø4 griber gevindet i listen og jækker de to dele
fra hinanden i stedet for at spænde dem sammen.

**Krav ved genkøb:** spånskrue/universalskrue, undersænket hoved, Torx, delgevind.
Elforzinket rækker indendørs; rustfri er kun nødvendigt udendørs, og Impreg®+ er en
udendørs-coating — mere end nødvendigt, men uskadeligt. Vinkelbeslagene er undtagelsen:
beslagskruer med **fladt** hoved, da en undersænket skrue trækker sig ned i beslagets hul
og kan flække det.

## Bolteakserne

Fordi hjørnebenet er 45×95 af afskær, er de to akser forskellige:

**Vange-aksen: M10 × 160** gennem vange (45) + ben (95) = 140 mm træ. Der stikker 20 mm ud
på benets inderflade, hvor skive 2,5 + møtrik 8 + kontramøtrik 8 = 18,5 mm — reelt plant,
ingen forsænkning. Kontramøtrikken er der, fordi ubehandlet fyr svinder, og boltede
træsamlinger løsner sig, når træet krymper. Alternativ: hattemøtrik, der dækker gevindet
helt.

**Endestykke-aksen: M8 × 100** gennem endestykke (45) + ben (45) = 90 mm. Møtrik + Ø24
skive sidder fladt på indersiden. Kun **1,5 mm gevind til overs**, så ingen kontramøtrik og
ingen nyloc på den akse (en M8 nyloc er ~8 mm høj og løber tør for gevind) — og hjørnet
skal presses helt sammen, før møtrikken sættes på. Boltene sidder ved x < 90, mens første
lamel starter ved x = 115, så møtrikkerne går fri af lamelfeltet.

**Hullerne er Ø12 og Ø10, ikke Ø11 og Ø9.** De "rigtige" størrelser er ikke altid til at
skaffe, så næste almindelige størrelse op blev valgt. To konsekvenser: bræddeboltens
firkanthals (M10 ~11,9 mm, M8 ~9,2 mm) **bider ikke** længere, så bolten skal holdes med en
tang, når møtrikken spændes — og marginen i boltkrydset faldt fra 5 til **4 mm** træ mellem
de to huller (de krydser vinkelret med 15 mm lodret afstand). Derfor kravet om vinkelret
boring og om at bore alle fire huller i et ben, før nogen bolt sættes i.

## Forkastede løsninger

Samlet her, så byggevejledningen ikke skal diskutere med sig selv:

| Forkastet | Erstattet af | Hvorfor |
|-----------|--------------|---------|
| Ramme 45×120 | 45×95 | vægt og udseende; 95 rækker statisk, når der er drager |
| Drager 45×70 på højkant | 45×45 | frihøjde 205 mm under midten; koster stivhed |
| Vinkelbeslag + 6×120 til midterbenet | 2 × 5×80 lodret ned | kravet gjaldt kun den 70 mm høje drager; den 45 mm høje giver 35 mm fat |
| M10 × 140 på vange-aksen | M10 × 160 | 140 mm bolt i 140 mm træ = nul gevind til møtrikken |
| Ø20-lomme i benets inderside | ingen forsænkning | en M10-møtrik kræver en top på 23–25 mm, som ikke kommer ned i Ø20; en større lomme bryder ind i endestykke-boltens hul 15 mm under. **Ø20-forstnerboret er derfor ude af værktøjslisten** |
| Ø11/Ø9 bolthuller | Ø12/Ø10 | kan ikke altid skaffes; koster 1 mm i boltkrydset og firkanthalsens greb |
| Trykimprægneret stolpe til ben | afskær 45×95 | ingen ubehandlet firkantstolpe fandtes; ubehandlet og lim-frit var kravet |
| Kombineret undersænkbor | løs kegleforsænker 90° Ø16 | nær-del og fjern-del skal have to forskellige diametre i samme hul |

Der findes intet mellem M10×140 og ×160: en ×120 når ikke gennem de 140 mm træ, og næste
trin op er ×200, som ville stritte 60 mm ud.

## Indkøbsregnskab

Priser fra Silvan.dk (juli 2026, ekskl. levering). Alt er købt hos Silvan bortset fra
vange-boltene.

### Træ — 1.376,40 kr

| Vare | Antal | Pris/stk | I alt |
|------|-------|----------|-------|
| [Reglar 45×45×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-reglar-45x45x2400-mm-ubehandlet-hoevlet-7700-9804949) | 18 | 64,80 | 1.166,40 |
| [Reglar 45×95×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-reglar-45x95x2400-mm-ubehandlet-hoevlet-7700-9804953) | 4 | 43,80 | 175,20 |
| [Forskalling 21×45×2400 ubeh.](https://www.silvan.dk/produkt/froeslev-forskalling-21x45x2400-mm-ubehandlet-hoevlet-7700-9804930) | 2 | 17,40 | 34,80 |
| Ben (4 hjørne + 1 midter) | 0 | — | 0 |

### Skruer, bolte og beslag — købt hos Silvan

| Vare | Varenr. | Pakke | Bruges | Tilovers |
|------|---------|-------|--------|----------|
| Simpson TTZNFS 4,5 × 60 | 74485 | 200 stk | 85 | 115 |
| Simpson TTZNFS 4,5 × 50 | 74484 | 200 stk | 12 | 188 |
| Simpson TTZNFS 5,0 × 80 | 76540 | 100 stk | 6 | 94 |
| Simpson TTUFP 4,0 × 20 beslagskruer | 74519 | 200 stk | ~16 | ~184 |
| KRAM bræddebolt M8 × 100 m/ møtrikker | 6774056 | 12 stk | 8 | 4 |
| KRAM spændeskive M8, 8,4 × 24 × 2,0 | 6774773 | 30 stk | 8 | 22 |
| KRAM spændeskive M10, 10,5 × 30 × 2,5 | 6774774 | 15 stk | 8 | 7 |
| Simpson AC35350 vinkelbeslag | — | 2 stk | 2 | 0 |

Overskuddet er stort, fordi skruerne ikke fandtes i mindre pakker i de længder. De faktiske
priser på skruer og beslag er ikke registreret.

### Mangler — hentes hos jem&fix

| Vare | Antal | Pris |
|------|-------|------|
| NKT bræddebolt DIN 603 M10 × 160, 2-pak à 39,95 | 8 stk (4 pk) | **159,80 kr** |
| Løse M10-møtrikker til kontramøtrik | 8 | ~25 kr |

**I alt ca. 1.650 kr** for en 100 % ubehandlet, lim-fri sengebund med ben af genbrugte
afskær.

## Åbne punkter

- **Vinkelbeslag:** Simpsons datablad anbefaler 2 beslag pr. samling (ét i hver side af
  drageren). Der er købt 2 i alt, altså ét pr. ende. To ekstra beslag koster lidt og øger
  sikkerhedsmarginen på den samling, hvis anbefalingen skal følges fuldt ud.
- **Dragerens nedbøjning** ligger på L/300-grænsen. Bør vurderes efter en sæsons brug.
- **De 2 skruer ned i midterbenet** sidder ±15 mm fra midten i CAD-modellen, altså 7,5 mm
  fra benets kant i endetræ. Bores der i hånden, kan de flyttes ind til ±10 mm — så skal
  dragerens gennemgangshuller flyttes tilsvarende.
- **Skruepriserne** er ikke prischecket, så totalen er et skøn.

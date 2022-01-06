# Eksam 2 (6. jaanuar 2022)

## Üldine

**Pärast lõpetamist näita õppejõule ette, et ta paneks su nime kirja.**

Kokku on eksamilt võimalik saada 400 punkti.

**Stiilipunktid lähevad arvesse!**

**Aine sooritamiseks peab eksami eest saama vähemalt 201 punkti ning aine eest kokku 501 punkti.**

**Eksami lahendused tuleb esitada eraldi GitLabi reposse** (mitte sinna, kuhu igapäevaselt ülesandeid lahendasid).

Kõik lahendused lähevad ühte faili. Gitis: ``EXAM/exam2/exam.py``

**Jälgi, et lahendus on korrektses kaustas ja fail õigesti nimetatud!**

Lubatud materjalid:

* Materjalid: https://pydoc.pages.taltech.ee/
* Pythoni ametlik dokumentatsioon: https://pydoc.pages.taltech.ee/py
* Gitlab: http://gitlab.cs.ttu.ee/
* Kursuse veeb: http://moodle.taltech.ee/

**Interneti kasutamine pole lubatud!**

Tulemusi vaata moodle.taltech.ee lehelt ülesande juurest (paremal submissions).

Vaata malli siitsamast kaustast: [exam.py](exam.py)

**Tähelepanu!** Eksami mallis on näited `assert` lausetena. `assert` lause töötab nii, et kui sellele järgnev avaldis on tõene (True), ei toimu midagi (konsoolis ei näidata midagi). Kui sellele järgnev avaldis on väär (False), siis tekib viga (koodi käivitamine lõppeb). Kes soovib, võib need asendada `print`-lausetega.

## Git ja PyCharm

Kui Gitiga ei saa ühendust, siis käivitada käsurealt: `git config --global http.sslVerify "false"`

Kooliarvutis PyCharmi kasutamiseks pead litsentsi küsima litsentsiserverilt. Kui klikkida *licence server*, peaks server automaatselt leitama (või kliki *discover*).

Giti kasutamiseks PyCharmis *checkout from version control* -> Git esilehelt või VCS -> *checkout from version control* -> Git

PyCarmis Giti seadistamiseks (kui antakse teade kloonimisel): File -> Settings -> Version Control -> Git. Seal `Path to Git executable` rea lõpus on kolm punkti. See avab kataloogipuu. Otsige üles `C:\Program files\git\bin\git.exe`.

Giti repo aadressi saad gitlabi lehelt. Selle kuju on üldiselt: ``https://gitlab.cs.ttu.ee/iti0102-2021/exams/iti0102-2021-exam2-UNIID.git``. Kus ``UNIID`` asenda enda uni-id-ga.

Kui PyCharmis pole Python seadistatud, siis saad lisada interpretaatori ``C:\Program Files\Python`` alt.

Te peaks nägema sellist olukorda, kus projekti all on kaust `EXAM`, selle all on kaust `exam1` ja selle sees fail `exam.py`.

Täiendav info Giti ja PyCharmi kasutamise kohta siin: https://pydoc.pages.taltech.ee/exam.html

# Ülesanded

## 01. `sum_of_digits` (30p)

Funktsioon saab sisendiks sõne. Funktsioon tagastab kõikide (ühekohaliste) numbrite summa sõnes. Kui ühtegi numbrit sõnes ei ole, on summa 0.

## 02. `range_with_count` (30p)

Fnktsioon saab sisendiks kolm täisarvu ja tagastab järjendi `start`-ist `stop`-ini, nii et lõpuks oleks `number` arv elemente järjendis.

## 03. `add_symbol` (30p)

Funktsioon saab sisendiks sõne ja sümbolid, mis näitavad milliseid tähti või numbreid tuleb tagastatavasse sõnesse lisada. 
Funktsioon tagastab lisatud sümbolitega sõne.

Kui sõnes olev täht on sümbolites olemas, siis peab see täht olema tagastatavas sõnes topelt.
Kui sõnes olev number on sümbolites olemas, siis peab see number olema tagastatavas sõnes kolmekordselt.

Kui mõni sümbol esineb sümbolite hulgas mitmekordselt, siis on see samaväärne ühe sümboli esinemisega.

## 04. `h_index` (30p)

Funktsioon saab sisendiks järjendi inimese artiklite viitamistest (iga järjendi element tähistab ühe artikli viitamiste arvu). 
Arvuta inimesele h-indeks.

H-indeks on suurim niisugune arv, kui palju leidub selliseid artikleid, mida on vähemalt selle arvu võrra viidatud. Ehk siis h-index N tähistab seda, et leidub vähemalt N sellist artiklit, mida on viidatud N või rohkem korda (ehk siis leidub vähemalt N sellist elementi, mille väärtus on N või suurem) - siin funktsioonis tuleb leida suurim võimalik N antud järjend jaoks.

Näiteks: sisendi [4, 2, 4] korral on h-indeks 2 (leidub vähemalt 2 artiklit, mida on viidatud 2 või enam korda). 3 enam ei sobiks (ei leidu kolme artiklit, mida on viidatud 3 või enam korda). Vaata täiendavaid näiteid mallist.

## 05. `count_pairs` (30p)

Kirjuta rekursiivne funktsioon, mis loendab kokku "paaride" koguse sõnes.

"Paar" antud ülesandes tähendab kahte sama sümbolit, mille vahel on omakorda sümbol. Näiteks sõnes `"axa"` a-tähed moodustavad paari.
Paarid võivad ka ülekattega olla. Näiteks sõnes `"axaxa"` on kolm paari: kaks tükki a-dega, üks x-dega.

Funktsioon peab olema rekursiivne, tsüklite kasutamine pole lubatud.

**Selle lahenduse vaatame käsitsi üle, et veenduda rekursiooni kasutamises.** Seega, kui isegi tester annab maksimumpunktid, aga tegemist pole rekursiooniga, võime punkti maha võtta.

## 06. `valid_parentheses` (50p)

Funktsioon saab sisendiks sõne, mis koosneb ainult järgmistest märkidest: `'('`, `')'`, `'{'`, `'}'`, `'['` ja `']'`.
Tuleb tagastada tõeväärtus, kas sõnes esinevad sulud on korrektsed või mitte. V.t näiteid.

## 07. Donut Factory (50p)

Teie ülesandeks on realiseerida lihtsustatud sõõrikuvabriku süsteem. Antud ülesande loogika käsitleb terve protsessi kõige
viimase etapi ehk sõõrikute (`Donut` klassi objektid) pakkimise osa, mis hakkab toimuma `DonutFactory` klassis. Kõik
sõõrikud erinevad teineteisest täidise ja glasuuri järgi.

**Klass Donut**

- `__init__(self, filling: str, icing: str)` - klassi konstruktor, mille sisendparameetriks on sõõriku täidis ja glasuur.
Täidise ja glasuuri nimetused antakse alati väikeste tähtedega.


**Klass DonutFactory**

- `__init__(self)` - klassi konstruktor.

- `add_donuts(self, donuts: list)` - meetod, mis lisab sõõrikud konveierile pakkimiseks.

- `get_donuts(self)` - meetod, mis tagastab listi kõikidest sõõrikutest, mis on praegu on konveieril.

- `pack_donuts_by_filling_and_icing(self)` - meetod, mis võimaldab pakkida sõõrikud täidise ja
glasuuri järgi. Tagastada tuleb sõnastik kujul `{(täidis, glasuur): [sõõrik1, sõõrik2]}`. Peale pakkimist peab konveier olema tühi (kõik sõõrikud tehases pakiti ära).

- `sort_donuts_by_icing_and_filling(self)` - meetod, mis peab tagastama sõõrikute listi, mis on sorteeritud kõigepealt
glasuuri järgi tähestiku järjekorras ning seejärel täidise järgi tähestiku järjekorras.

- `get_most_popular_donut(self)` - meetod peab tagastama sellise sõõriku glasuuri ja täidise, mille leidub kõige
**rohkem** konveieril praegusel hetkel. Sõnastik peab olema kujul `{'icing': sõõriku_glasuur, 'filling': sõõriku_täidis}`. 
NB! Glasuuri ja täidise kombinatsioon, mitte et leiad lihtsalt kõige populaarsema glasuuri ja pärast eraldi kõige 
populaarsema täidise! Kui populaarseid kombinatsioone on mitu, tagastada see, mille glasuur (*icing*) on tähestikus eespool (ehk siis "a" on prioriteetsem kui "b").

- `get_donuts_by_flavour(self, flavour: str)` - meetod peab tagastama nimekirja nendest sõõrikutest, mille glasuur või täidis on sama
nagu meetodi parameetris on etteantud. Parameeter antakse alati väikeste tähtedega.
    
## 08. Witcher (100p)

Realiseeri süsteem, mis simuleerib koletisi jahtivaid witcher'eid.

### Klass Species(Enum)
Species on enum.Enum klassi extend'iv klass, mis loetleb võimalikke koletise liike.
* Dragon
* Vampire
* Beast

### Klass: Monster

Monster on koletis, keda jahib Witcher.
* `__init__(self, species: Species, bounty: int)` - Konstruktor, mis annab koletisele liigi ja summa palju selle jahtimise eest saab.
* `get_species(self) -> Species` - Tagastab koletise liigi.
* `get_bounty(self) -> int` - Tagastab koletise eest saadava tasu.
* `is_alive(self) -> bool` - Kontrollib, kas koletis on elus või mitte. Kui koletis on jahitud, siis on witcher ta ära tapnud.
* `slay(self) -> bool` - Tapab koletise, kui koletis oli ennem elus, siis tagastab `True` kui koletis oli juba surnud, siis tagastab `False`.
* `__repr__(self) -> str` - Tagastab korrektselt vormistatud sõne kujul "A {Species} worth {bounty} coins" 
siin lauses peab olema liigi kohta ainult viimane osa, ehk kui tegu oleks Dragon liiki koletisega väärt 100, siis oleks tulemus:
`A Dragon worth 100 coins`

### Klass: Village

Village on küla, millele valmistavad probleeme koletised ja raha, millega tasuda witcher'ile.
Samuti on külas elanike arv, mis väheneb ühe võrra iga päev iga koletise kohta.
Elanike arv ei saa olla kunagi negatiivne.
Kui külas ei ole enam ühtegi elus olevat elanikku, siis ei saa witcher sealt ühtegi tööd.
Algselt on küla vanus 0.
Algselt on külal 100 münti. 

* `__init__(self, name: str, initial_population: int)` - Konstruktor, mis annab külale nime ja esialgse elanike arvu.
* `get_name(self) -> str` - Tagastab küla nime.
* `get_population(self) -> int` Tagastab küla hetke elanike arvu.
* `get_monsters(self) -> list` Tagastab list'i külale probleeme valmistavatest koletistest. Kui küla elanikke ei ole, siis ei valmista ükski koletis probleeme.
* `add_monster(self, monster: Monster) -> None` - Lisab külale probleeme valmistava koletise.
* `add_money(self, amount) -> None` - Lisa antud summa küla eelarvele.
* `advance_day(self) -> None` - Suurendab küla vanust päeva võrra.
* `pay(self, amount: int) -> bool` - Proovib maksta sobiva summa. Kui on piisavalt raha, siis küla raha väheneb ja tagastatakse `True`,
vastasel juhul tagastatakse `False` ja küla raha ei muutu.
* `__repr__(self) -> str` - Tagastab küla kirjeldava sõne "{name}, population {population}, age {age}"

### Klass: Witcher
Witcher on koletiste jahtija, kes otsib küladest tööd ja kogub selle eest raha

* `__init__(self, name: str, school: str)` - Konstruktor, mis loob vastava kooli witcher'i.
* `get_money(self) -> int` - Tagastab witcher'i hetke raha.
* `get_slain(self) -> list` - Tagastab nimekirja koletistest, kelle antud witcher on tapnud.
* `get_hunted_species(self) -> list` - Tagastab nimekirja koletise liikidest, keda antud witcher tapnud järjestatud tähestikulises järjekorras.
* `hunt_most_expensive(self, village: Village) -> bool` - Witcher jahib kõige väärtuslikuma koletise antud külast ja proovib saada tasu.
Koletis tapetakse igal juhul. Kui külal oli koletis, keda tappa ja piisavalt raha, et tasuda, siis tagastatakse `True` vastasel juhul `False`.
* `__repr__(self) -> str` - Tagastab korrektse witcher'it kirjeldava sõne kujul "{name} of {school} school with {number} monsters slain".
Näiteks `Geralt of Rivia of Wolf school with 7 monsters slain`
  
### Enum kasutamisest

Enumi kohta saab lugeda Pythoni dokumentatsioonist: https://pydoc.pages.taltech.ee/py/library/enum.html

Siin ülesandes on kasutusel enum `Species`. Seda saab kasutada nii:

1. Enumi loomine (ei ole siin ülesande lahenduses tegelikult vaja, aga näidetes on):

```python
godzilla = Monster(Species.Beast, 200)
```

2. Enumi kontrollimine (ei tohiks siin ülesandes vaja minna):

```python
print(godzilla.get_species() == Species.Beast)
```

3. Enumi teksti kättesaamine

```python
godzilla = Monster(Species.Beast, 200)
print(str(godzilla.get_species()))
```

4. Enum järjendis:

```python
species_list = [Species.Beast, Species.Vampire, Species.Beast]
print(species_list[0] == species_list[1])   # False
print(species_list[0] == species_list[2])   # True
```

Ehk siis kui võrrelda kahte enumi objekti (näiteks listis esimene ja kolmas element, siis need on võrdsed, kui need on samat tüüpi.

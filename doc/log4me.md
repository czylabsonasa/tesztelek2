## Módosítások


### 2020 dec 21-22
#### config_gen.py
* python -> python3 csere
#### evaluate.py
* az "integer hiba" nem volt jó -> fix
* float ellenőrzés -> 1e1 alak -> beépít
#### használat
* prog mód -> default -> help szövegben is kicserélve
* 
#### octave
* IO példák a használathoz

---

### 2020 dec 02
#### golang prog-módban [tesztelve](../problems/bday/doc/pexample.md)

---

### 2020 nov 30
#### func mód a javascript/node.js-hez [app.js](../problems/_apps/app.js)
#### megvalósítás: [Kántor Dániel](https://github.com/KDani-99)

---

### 2020 nov 21
#### cél: `python checker.py sol=bday.m` típusú használat
* a nyelv -> kiterjesztés (`m` az octave)
* a feladat -> fájlnév mínusz dot + kiterjesztés
* a mód -> `func` a default, a `prog` explicite meg kell adni
* sorrend: defaultargs -> guessargs -> parancssorban megadottak
  * tehát az utolsó a végleges

#### ez technikailag:
* `_defaultargs` módosít
* `_ext2lang` bevezet, dot kidob az ext-ből
  * win-es path-ok kezelése (pl: "c:\asd\bsd.py" )
* `getargs` átír
* `guessargs` függvény a `prepare.py`-be
* a `prepare` fv tevékenység átszervezése
  * `cmdline` kidob -> `validargs` bevezet (ezek a `cmdline`-ben voltak)

---

## Egyebek
* [itt](iss.md)
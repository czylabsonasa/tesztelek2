## módosítások/tervek

### 2020 nov 21
#### cél: `python checker.py sol=bday.m` típusú használat
* a nyelv -> kiterjesztés (`m` az octave)
* a feladat -> fájlnév mínusz dot + kiterjesztés
* a mód -> `func` a default, a `prog` explicite meg kell adni
* sorrend: defaultargs -> guessargs -> parancssorban megadottak
  * tehát az utolsó a végleges

#### technikailag megvalósítás:
* `_defaultargs` módosít
* `_ext2lang` bevezet, dot kidob az ext-ből
  * win-es path-ok kezelése (pl: "c:\asd\bsd.py" )
* `getargs` átír
* `guessargs` függvény a `prepare.py`-be
* a `prepare` fv tevékenység átszervezése
  * `cmdline` kidob -> `validargs` bevezet (ezek a `cmdline`-ben voltak)

#### elvileg: `done`

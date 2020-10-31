### Ez egy tesztelő

* Elkezdtem [ezt](https://github.com/czylabsonasa/tesztelek) de elégedetlen voltam vele,
  így mivel a brancsolás a fiataloknak való - átírtam erre. Ez már egy árnyalatnyival 
  jobban tetszik.
* Többféle nyelvet használhatsz. (python,matlab/octave,julia,c/c++)
* A feladatok közül választasz és megpróbálod megoldani.
* Jelenleg 2 féle megoldási módot támogat:
  * ```prog```: megírod a megoldást kedvenc nyelveden, ```stdin/stdout```-t használva a 
  kommunikációra. A rendszer input-fájlonként fogja a programodat letesztelni, 
  összehasonlítva a hivatalos megoldást a tieddel. A végén egy összefoglalást fogsz látni 
  az eredményekkel. Ez a módszer minden feladatnál támogatott.
  * ```func```: itt mindenképpen egy függvényt kell írnod (melynek a neve ```solve``` kell legyen, 
  mert az app azt hívja meg). Ez a fv. a tesztelő rendszertől 
  megkapja az aktuális input/output deszkriptorait, ezek(ből/be) intézed az 
  olvasást és írást. Ezt olyan környezeteknél érdemes használni, ahol a rendszer 
  felállási ideje magas (matlab,java(?)) - hiszen ennél a módnál csak egyszer indítjuk be. 
  Ez **nem** minden feladatnál elérhető - csak ahol a feladat könyvtárában megvan a megfelelő nyelven 
  egy ```app``` nevű program (egy szimbolikus link amit a win nem tamogat és a github-se teljesen, 
  de **remélem** nem gond).



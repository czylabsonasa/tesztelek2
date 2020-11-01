## Általános:
* a számokat legalább 12 jegyig írjuk ki a feladatoknál
* az input/output formáját tekintve a megadott példák a mérvadók
* jelölés:
  * (M): mintafeladat, megoldásokkal
  * (P) : pontos eredményt kell számolni
  * (S) : szimulációs feladat
* rövidítés:
  * valség = valószínűség
  * v.v. = valségi változó

---
### születésnap
#### [bday](bday/doc/desc.pdf)
* (M)
* a klasszikus születésnap probléma: M ember esetén mennyi az esélye 
hogy látunk születésnap megegyezést?
  * fontos **feltevés**: a születésnapok eloszlása egyenletes, azaz
olyan v.v.-t figyelünk meg mely egyforma valséggel vesz fel bármely számot az [1,365] intervallumból.
  * megoldás
    * [prog mód](bday/doc/pexample.md)
    * [func mód](bday/doc/fexample.md)


#### [bdaymin](bdaymin/doc/desc.pdf)
* (P)
* hány ember kell hogy legyen egy társaságban, hogy 
pl. 80%-nál nagyobb eséllyel legyen születésnap azonosság?


---


### kocka
#### [diesum3](diesum3/doc/desc.pdf)
* (M)
* 3 kockával dobva mennyi az esély hogy S a dobott számok összege?
  * megoldás
    * [prog mód](diesum3/doc/pexample.md)
    * [func mód](diesum3/doc/fexample.md)


#### [diesum](diesum/diesum.pdf)
* (P)
* n kockát feldobva mennyi a valsége, hogy a dobott számok összege S?

---



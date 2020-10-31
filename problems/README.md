## Általános:
* a számokat legalább 12 jegyig írjuk ki a feladatoknál
* az input/output formáját tekintve a megadott példák a mérvadók
* jelölés:
  * (M): mintafeladat, megoldásokkal
  * (Px) : pontos eredményt kell számolni, x-pontot ér
  * (Sx) : szimulációs feladat, x-pontot ér
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
  * [megoldás prog mód](bday/doc/pexample.md)
  * [megoldás func mód](bday/doc/fexample.md)

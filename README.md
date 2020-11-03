## [Mi ez?](doc/wtfit.md)
## [Használat](doc/usage.md)
## [Feladatsorok](problems/README.md)

## Problémák melyek felmerülhetnek:
* a ```problems/feladatneve/app.*``` fájlok szimbolikus linkek. Ezzel nem tudom mi történik ha 
win-es fájlrendszerre klónozol. A lényeg az lenne hogy valami fájl-féleség maradjon - azaz 
a python-os ```os.path.isfile/islink``` felismerje. Ha tudsz valamit jelezz!
* nincs kezelve az időtúllépés (nincsenek időkorlátok sem a feladatokhoz) - ez akkor jelenthet 
  problémát, ha órákig futna a programod az adott feladatra és csak vársz, vársz... A
  végén valahogy leállítod. Erre ```python@linux```-on vannak automatizálható eszközök, amik 
  sajnos win-en nem működnek. Ötlet?

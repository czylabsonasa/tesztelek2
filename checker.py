from prepare import prepare
from execute import execute
from evaluate import evaluate
from report import report

usage="""
======================================================================
    használat:
    python checker.py sol=fájl lang=nyelv problem=feladat mode=mód
      a paraméterek:
      sol: a megoldás elérési útja
      lang: a nyelv
      problem: a tesztelendő feladat rövid neve
      mode: 
        prog --> klasszikus program
        func --> csak egy függvény
======================================================================
"""



res=prepare(dict())
res=execute(res)
res=evaluate(res)
report(res)


print()
if res["prep"]["msg"]!="OK":
  print(usage)


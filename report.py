def report(res):
  from sys import stdout
  from auxiliaries import tabulate
  tab=[]
  pk=list(res["eval"].keys())
  n=len(pk)
  nok="0"
  at="n/a"
  if n>0:
    nok=0
    at=0.0
    pk.sort(key=lambda x:int(x))
    for k in pk:
      rk=res["eval"][k]
      tab.append([str(k), str(rk[0]), str(rk[1])])
      if rk[0]=="OK":
        nok+=1
        at+=rk[1]
    nok="{:.2f}%".format(100*nok/n)
    at="{:.4f}".format(at)


  print()
  print(tabulate(tab, \
    starter=["akció", "eredmény","idő"],\
    prepper=["előkészületek",res["prep"]["msg"],"n/a"],\
    ender=["összesen", nok , at])
  )
  print()
  stdout.flush()

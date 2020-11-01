def report(tab,res):
  from sys import stdout
  from tabulate import tabulate
  
  pk=list(res["eval"].keys())
  n=len(pk)
  if n>0:
    nok=0.0
    at=0.0
    pk.sort(key=lambda x:int(x))
    for k in pk:
      rk=res["eval"][k]
      tab.append([k, rk[0], rk[1]])
      if rk[0]=="OK":
        nok+=1
        at+=rk[1]
    tab.append(["*","*","*"])
    tab.append(["összesen", "{:.2f}%".format(100*nok/n), "{:.4f}".format(at)])
  

  print()
  print(tabulate(tab, headers=["akció", "eredmény","idő"]))
  print()
  stdout.flush()

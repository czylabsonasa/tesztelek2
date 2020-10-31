def report(tab,res):
  from sys import stdout
  from tabulate import tabulate
  
  pk=list(res["eval"].keys())
  if len(pk)>0:
    pk.sort(key=lambda x:int(x))
    for k in pk:
      rk=res["eval"][k]
      tab.append([k, rk[0], rk[1]])

  print()
  print(tabulate(tab, headers=["akció", "eredmény","idő"]))
  print()
  stdout.flush()

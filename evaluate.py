def evaluate(res):

  if res["prep"]["msg"]!="OK":
    res["eval"]=dict()
    return res

  from auxiliaries import tokensof
  from config_gen import FLOAT_TOL, INT_TOL
  from os import chdir, path
  from pathlib import Path

  # osszehasonlitja az aktualis es az elvart kimenetet
  # ezek mar tokenlistak
  def evalone(actual,official):
    if len(actual)!=len(official): # ez általában túl szigorú
      return("az output sok/kevés tokent tartalmaz")

    for sa,so in zip(actual,official):
      tip=str
      while True:
        try:
          float(so)
          if "." in so or "e" in so.lower(): # ddddéndzserasz 1e-1 2E-3 1.0 -> float
            tip=float
            break
        except:
          pass
        try:
          int(so)
          tip=int
          break
        except:
          pass
        break

      try: 
        tip(sa)
      except:
        return('hibás adat az outputban')

      va=tip(sa)
      vo=tip(so)

      while True:
        if tip==str:
          if va!=vo:
            return('sztring hiba')
        if tip==int:
          if abs(va-vo)>INT_TOL: # 
            return('integer hiba')
        if tip==float:
          if abs(va-vo)>FLOAT_TOL:
            return('lebegőpontos hiba')
        break
    return('OK')

  pth=Path().absolute()
  chdir(res["prep"]["TEST_DIR"])
  evald=dict()

  cnt=0
  while True:
    scnt=str(cnt)
    if not path.exists("io/"+scnt+".in"):
      break

    fd=open("act/"+scnt+".info","r")
    r,t=fd.read().split()
    fd.close()      

    r=int(r)
    t=float(t)
    if r==1:
      r=evalone(tokensof("act/"+scnt+".out"),tokensof("io/"+scnt+".out"))
    else:
      r="futás közbeni hiba"
    
    evald[scnt]=[r, t]
    cnt+=1
  
  chdir(pth)
  
  res["eval"]=evald
  return res

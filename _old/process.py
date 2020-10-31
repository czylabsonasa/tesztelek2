def process(prep):
  if prep["msg"] != "OK":
    return dict()

  from aux import tokensof
  from config_gen import FLOAT_TOL, INT_TOL
  from os import chdir, system, path

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
          "." in so
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
          if abs(sa-va)>INT_TOL or tip(va-vo)>INT_TOL:
            return('integer hiba')
        if tip==float:
          if abs(va-vo)>FLOAT_TOL:
            return('lebegőpontos hiba')
        break
    return('OK')

  # mivel minden feladatnal 0-max-ig mennek a nevek
  # igy 1xubb
  def runfunc():
    chdir(prep["TEST_DIR"])
    system(prep["cmd"])

  def runprog():
    


  def evaluate()
    proc=dict()
    cnt=0
    while True:
      scnt=str(cnt)
      if not path.exists("act/"+scnt+".info"):
        break
    
      fd=open("act/"+scnt+".info","r")
      r,t=fd.read().split()
      fd.close()      

      r=int(r)
      t=float(t)
      if r==1:
        r=comparethem(tokensof("act/"+scnt+".out"),tokensof("io/"+scnt+".out"))
      else:
        r="futás közbeni hiba"
    
      proc[scnt]=[r, t]
      cnt+=1
    return proc



import sys,os,glob, shutil
from konfig import *
from problemdb import *
####

def usage():
  return """
    használat:
    python checker.py prog=prog lang=nyelv problem=feladat mode=mód
      a paraméterek:
      prog: a programod neve (elérési úttal)
      lang: a nyelv (octave,python,julia)
      problem: a tesztelendő feladat (pl. bdaymin)
      mode: 
        prog --> klasszikus program
        func --> csak egy függvény
  """

def prepare():
  prep=dict()

  # egyszeru parancssori feldolgozo
  def getargs(argd):
    ok=True
    for v in sys.argv[1:]:
      if '=' in v: # csak egyenlosegest fogad el
        r=v.split("=")
        # rossz esetek:
        # tobb egyenloseg van
        # az lhs nem key
        # az rhs nulla hosszu
        if (len(r)!=2) or (r[0] not in argd.keys()) or (len(r[1])==0):
          ok=False
          break
        argd[r[0]]=r[1]
      else:
        ok=False
        break
    return ok


  def init():
    #print(TESTDIR)
    shutil.rmtree(TEST_DIR,ignore_errors=True)
    os.makedirs(TEST_DIR)
    os.makedirs(TEST_DIR+"/act")

  def cmdline():
    nonlocal prep

    prep["msg"]="OK"
    while True:
      for (k,v) in pool["defaultargs"]:
        prep[k]=v
      if getargs(prep)==False:
        prep["msg"]="hiba a parancssorban"
        break
      
      # a programfájl megléte:
      try:
        open(prep["prog"]).close()
      except:
        prep["msg"]="nem található a "+prep["prog"]
        break

      # van-e ilyen nyelv a listán?
      if prep["lang"] not in pool["langs"]:
        prep["msg"]="ismeretlen nyelv"
        break
      
      if prep["mode"] not in pool["modes"]:
        prep["msg"]="ismeretlen mód"
        break


      if prep["problem"] not in problemlist:
        prep["msg"]="ismeretlen/nem elérhető feladat"
        break
      

      # feladatspecifikus
      if prep["mode"]=="prog" and prep["lang"]=="matlab":
        prep["msg"]="matlabhoz nem elérhető a prog mód"
        break
        
      if prep["mode"]=="func":
        try:
          f=PROBLEM_DIR+"/"+prep["problem"]+"/func"
          import f
        except:
          prep["msg"]="hiányzó func fájl"
          break
        if prep["lang"] not in pool["langs"]:
          prep["msg"]="a feladathoz nem elérhető a func mód"
          break
      break
    
  # prog/func
  def copystuff():
    nonlocal prep
    prog=prep["prog"]
    lang=prep["lang"]
    problem=prep["problem"]
    mode=prep["mode"]
    ext=pool["lang2ext"][lang]
    floc=PROBLEM_DIR+"/"+problem
    shutil.copy(prog, TEST_DIR+"/solve"+ext)
    shutil.copy(floc+"/app"+ext, TEST_DIR+"/app"+ext)
    shutil.copytree(floc+"/io", TEST_DIR+"/io")

  cmdline()
  if prep["msg"]=="OK":
    init()
    copystuff()
  return prep

####

def process(prep):
  if prep["msg"] != "OK":
    return dict()
  def tokensof(allomany):
    f=open(allomany)
    d=f.read().split()
    f.close()
    return [v.strip() for v in d if len(v.strip())>0 ] #paranoia

  def comparethem(actual,official):
    if len(actual)!=len(official): # ez általában túl szigorú
      return('az output sok/kevés tokent tartalmaz')
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
  proc=dict()
  os.chdir(TESTDIR)
  os.system(prep["cmd"])
  cnt=0
  while True:
    scnt=str(cnt)
    if not os.path.exists("act/"+scnt+".info"):
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

####

def report(tab,proc):
  from tabulate import tabulate
  pk=list(proc.keys())
  pk.sort(key=lambda x:int(x))
  for k in pk:
    rk=proc[k]
    tab.append([k, rk[0], rk[1]])
  print()
  print(tabulate(tab, headers=["akció", "eredmény","idő"]))
  print()
  sys.stdout.flush()

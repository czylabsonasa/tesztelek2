def execute(res):
  if res["prep"]["msg"] != "OK":
    res["exec"]=dict()
    return res

  #from auxiliaries import tokensof
  #from config_gen import FLOAT_TOL, INT_TOL
  from os import chdir, system, path
  from pathlib import Path
  from time import time

  # itt az app intez szinte mindent
  def runfunc():
    pth=Path().absolute()
    chdir(res["prep"]["TEST_DIR"])
    #print("a parancs: "+res["prep"]["cmd"])
    system(res["prep"]["cmd"])
    chdir(pth)

  # itt kezzel kell
  def runprog():
    pth=Path().absolute()
    chdir(res["prep"]["TEST_DIR"])
    cmd=res["prep"]["cmd"]
    print("cmd="+cmd)
    cnt=0
    while True:
      scnt=str(cnt)
      if not path.exists("io/"+scnt+".in"):
        break

      t0=time()
      r=1
      try:
        system(cmd.format(scnt,scnt))
      except:
        r=0
      t0=time()-t0

      fd=open("act/"+scnt+".info","w")
      fd.write("{:d} {:.4f}".format(r,t0))
      fd.close()      
      cnt+=1
    
    chdir(pth)


  while True:
    mode=res["prep"]["mode"]
    if mode=="func":
      runfunc()
      break
    if mode=="prog":
      runprog()
      break
    # itt ismeretlen hiba van
    break


  res["exec"]=dict()
  return res

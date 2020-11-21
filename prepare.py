def prepare(res):
  def defaultargs():
    from config_gen import config_gen
    for k,v in config_gen["defaultargs"].items():
      res[k]=v


  def inittestdir():
    from shutil import rmtree
    from os import makedirs
    TEST_DIR=res["TEST_DIR"]

    rmtree(TEST_DIR,ignore_errors=True)
    makedirs(TEST_DIR)
    makedirs(TEST_DIR+"/act")

  def guessargs():
    sol=res["sol"]
    # nincs honnan találgatni
    if sol=="":
      return
    from platform import system
    dirsep="/"
    if system()=="Windows":
      dirsep="\\"
    prob,kit=sol.split(':')[-1].split(dirsep)[-1].split('.')
    if res["problem"]=="":
      res["problem"]=prob
    from config_gen import config_gen
    if res["lang"]=="" and kit in config_gen["ext2lang"]:
      res["lang"]=config_gen["ext2lang"][kit]

  def validargs():
    from config_problems import reg_problems
    from config_gen import config_gen

    PROBLEM_DIR=res["PROBLEM_DIR"]

    while True:
      sol=res["sol"]
      lang=res["lang"]
      problem=res["problem"]
      mode=res["mode"]

      # print(res)
      # nincs sol a cl-ben
      if sol=="":
        res["msg"]="legalább a forrást meg kell adni"
        break
      if lang=="":
        res["msg"]="nem tudom megállapítani a nyelv-et"
        break
      if lang=="":
        res["msg"]="nem tudom megállapítani a feladat-ot"
        break
        
      # a programfájl megléte:
      try:
        open(sol).close()
      except:
        res["msg"]="nem található a megoldásfájl"
        break

      # van-e ilyen nyelv a listán?
      if lang not in config_gen["langs"]:
        res["msg"]="ismeretlen nyelv"
        break
      
      if mode not in config_gen["modes"]:
        res["msg"]="ismeretlen mód"
        break


      if problem not in reg_problems or reg_problems[problem]!=1:
        res["msg"]="ismeretlen/nem elérhető feladat"
        break
      

      # egyesek (matlab) kizarasa prog módban
      if mode=="prog":
        if lang in ["matlab"]:
          res["msg"]="nem elérhető a prog mód"
          break
        
      if mode=="func":
        if lang=="binary":
          res["msg"]="nem elérhető a func mód"
          break

        from os import path
        pth=PROBLEM_DIR+"/"+problem+"/app."+config_gen["lang2ext"][lang]
        #print(pth)
        if False==path.islink(pth) and False==path.isfile(pth):
          res["msg"]="nem elérhető a func mód"
          break

      res["cmd"]=config_gen["lang2cmd"][mode][lang]
        
      break
    
  # prog/func
  def populatetestdir():
    from shutil import copy, copytree
    from config_gen import config_gen

    TEST_DIR=res["TEST_DIR"]
    PROBLEM_DIR=res["PROBLEM_DIR"]

    sol=res["sol"]
    lang=res["lang"]
    problem=res["problem"]
    mode=res["mode"]
    ext=config_gen["lang2ext"][lang]
    
    copy(sol, TEST_DIR+"/solve."+ext)
    if mode=="func":
      copy(PROBLEM_DIR+"/_apps/app."+ext, TEST_DIR+"/app."+ext)
    copytree(PROBLEM_DIR+"/"+problem+"/io", TEST_DIR+"/io")


  # tevékenység:
  from auxiliaries import getargs, copydict
  res["msg"]="OK"
  defaultargs() # ez bemásolja a config-ból a def értékeket
  while True:
    argdict,ok=getargs()
    if ok==False:
      # hiba:
      res["msg"]="hiba a parancssori argumentumokban."
      break
    # insert az ujak
    copydict(argdict,res)
    # megpróbáljuk a hiányzó cl argokat összeszedni
    guessargs()
    # megfelelőek-e az arg-ok
    validargs() 
    if res["msg"]=="OK":
      inittestdir()
      populatetestdir()
    break
  
  return dict({"prep":res})

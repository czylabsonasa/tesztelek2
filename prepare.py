def prepare(res):
  def geninit():
    from config_gen import config_gen
    for k,v in config_gen["defaultargs"].items():
      res[k]=v


  def testdirinit():
    from shutil import rmtree
    from os import makedirs
    TEST_DIR=res["TEST_DIR"]

    rmtree(TEST_DIR,ignore_errors=True)
    makedirs(TEST_DIR)
    makedirs(TEST_DIR+"/act")

  def cmdline():
    from aux import getargs
    from config_problems import reg_problems
    from config_gen import config_gen

    PROBLEM_DIR=res["PROBLEM_DIR"]

    res["msg"]="OK"
    while True:
      # hiba a parancssori argok feldolgozasanal:
      if getargs(res)==False:
        res["msg"]="hiba a parancssorban"
        break

      # print(res)
      sol=res["sol"]
      lang=res["lang"]
      problem=res["problem"]
      mode=res["mode"]
      
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
        from os import path
        pth=PROBLEM_DIR+"/"+problem+"/app"+config_gen["lang2ext"][lang];
        #print(pth)
        if False==path.islink(pth) and False==path.isfile(pth):
          res["msg"]="nem elérhető a func mód"
          break

      res["cmd"]=config_gen["lang2cmd"][mode][lang]
        
      break
    
  # prog/func
  def copystuff():
    from shutil import copy, copytree
    from config_gen import config_gen

    TEST_DIR=res["TEST_DIR"]
    PROBLEM_DIR=res["PROBLEM_DIR"]

    sol=res["sol"]
    lang=res["lang"]
    problem=res["problem"]
    mode=res["mode"]
    ext=config_gen["lang2ext"][lang]
    
    copy(sol, TEST_DIR+"/solve"+ext)
    if mode=="func":
      copy(PROBLEM_DIR+"/_apps/app"+ext, TEST_DIR+"/app"+ext)
    copytree(PROBLEM_DIR+"/"+problem+"/io", TEST_DIR+"/io")

  geninit()
  cmdline()
  if res["msg"]=="OK":
    testdirinit()
    copystuff()

  return dict({"prep":res})

# nehany altalaban is hasznalhato kulso fuggveny

###

# egyszeru parancssori feldolgozo
def getargs(argd): # argd-ben vannak a default ertekek
  from sys import argv
  ok=True
  for v in argv[1:]:
    if '=' in v: # csak egyenlosegest fogad el
      r=v.split("=")
      # hibak kezelese:
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
  if ok==True:
    for k,v in argd.items():
      if len(v)==0:
        ok=False
        break
  return ok

###

# tokenizal
def tokensof(name):
  f=open(name) # trust
  toks=f.read().split()
  f.close()
  return [v.strip() for v in toks if len(v.strip())>0 ] # strip paranoia

###


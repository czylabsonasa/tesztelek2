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
# tabulate - kevesebb függőség


def tabulate(tab,starter=[],prepper=[],ender=[],space=3):
  if starter==[] or ender==[] or len(starter) != len(ender):
    return ""
  ncol=len(starter)
  ntab=len(tab)
  mx=[0]*ncol

  def upd1(akt):
    nonlocal mx, ncol
    acol=len(akt)
    if acol != ncol:
      return False
    for k in range(acol):
      mx[k]=max(mx[k],len(akt[k]))
  def upd():
    nonlocal tab
    ret=True    
    for row in tab:
      if upd1(row)==False:
        ret=False
        break
    return ret
  upd1(starter)
  upd1(prepper)
  upd1(ender)
  if upd()==False:
    return ""

  mx=[v+space for v in mx]
  totmx=sum(mx)

  def mkrow(akt):
    nonlocal mx, ncol
    return "".join([ *[akt[j].ljust(mx[j]) for j in range(ncol-1)], akt[-1].rjust(mx[-1]),])
 
  for k in range(ntab):
    tab[k]=mkrow(tab[k])

  if len(tab)>0:
    tab=["-"*totmx,*tab,"="*totmx,mkrow(ender)]
  else:
    tab=["="*totmx]

  return "\n".join([\
    mkrow(starter), "="*totmx,
    mkrow(prepper),*tab]
  )

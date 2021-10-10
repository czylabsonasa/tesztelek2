### solve.py
def solve(fin,fout):
  import numpy as np
  M=int(fin.read()) 
  P=-1.0
  while True:
    if M<2:
      P=0.0
      break
    if M>365:
      P=1.0
      break
    P=1.0-np.prod(1.0 - np.array(range(0,M))/365.0)
    break
  fout.write("{:.12f}".format(P))

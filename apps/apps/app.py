import time
# import solve
fin=open("solve.py")
exec(fin.read())

cnt=0
while True:
  inname="io/"+str(cnt)+".in"
  try:
    fin=open(inname,"r")
  except:
    break

  fout=open("act/"+str(cnt)+".out","w")

  t0=time.time()
  ok=1
  try:
    #solve.solve(fin,fout)
    solve(fin,fout)
  except:
    ok=0
  mt=time.time()-t0


  fin.close()
  fout.close()

  with open("act/"+str(cnt)+".info","w") as f:
    f.write("{:d} {:.4f}\n".format(ok, mt))

  cnt=cnt+1

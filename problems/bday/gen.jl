function solve(M)
  M>365 && return 1.0
  M<2 && return 0.0
  1.0 - prod(1 .- (0:(M-1)) / 365)
end

for fn=0:10
  fin=open("io/$(fn).in","w")
  M=5*fn
  println(fin,M)

  fout=open("io/$(fn).out","w")
  P=solve(M)
  println(fout,P)

  close(fin)
  close(fout)
end

for fn=11:30
  fin=open("io/$(fn).in","w")
  M=rand(40:150)
  println(fin,M)

  fout=open("io/$(fn).out","w")
  P=solve(M)
  println(fout,P)

  close(fin)
  close(fout)
end

for fn=31:33
  fin=open("io/$(fn).in","w")
  M=rand(366:399)
  println(fin,M)

  fout=open("io/$(fn).out","w")
  P=solve(M)
  println(fout,P)

  close(fin)
  close(fout)
end


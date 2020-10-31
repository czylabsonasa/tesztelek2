# 3 kocka feldobasa, valsegeloszlas
pre=fill(0.0, 6*3)
p=(1.0/6.0)^3
for i=1:6,j=1:6,k=1:6 
  pre[i+j+k]+=p
end

for fn=1:20
  fin=open("io/$(fn).in","w")
  println(fin,fn)
  fout=open("io/$(fn).out","w")
  P=2<fn<19 ? pre[fn] : 0.0
  println(fout,P)

  close(fin)
  close(fout)
end

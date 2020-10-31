function solve(P)
  qM,m,M=1.0,365,1 # qM: "M emberbol nincs ket egyforma napon szuletett" valsege
  while true 
    if 1.0-qM>P
      break
    end
    M+=1
    m-=1
    qM=qM*(m/365)
  end
  M
end


for fn=3:50
  fin=open("input/input$(fn).txt","w")
  P=rand(1:999)/1000
  println(fin,P)

  fout=open("output/output$(fn).txt","w")
  M=solve(P)
  println(fout,M)

  close(fin)
  close(fout)
end

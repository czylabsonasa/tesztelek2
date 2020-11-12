# random, pozitív összeadókra bontás
# n: ezt bontjuk fel, r:részre
# sorrend számít
# pl: (6,2) -> (1,5), (4,2)
# n-1 = n-r + (r-1) --> egyesek és elválasztók
# sample
using StatsBase

function ranpart(n,r)
  if (n==0) || (r>n)
    []
  else
    p=sample(1:(n-1),r-1,replace=false,ordered=true); # ezek a pálcikák
    diff(vcat(0,p,n))
  end
end

# spec esetek nélkül
# ranpart(n,r)=diff(vcat(0,sample(1:(n-1),r-1,replace=false,ordered=true),n))


# pontosan 1 összegű lebegőpontos számok előállítására:
# 0.112, 0.688, 0.200 -> az 1000-et háromfele osztjuk
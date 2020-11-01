### julia
## app
```julia
include("solve.jl")
function app()
  cnt=0
  while true
    
    fin=try open("io/$(cnt).in","r") catch; nothing end
    (fin==nothing) && break
    fout=open("act/$(cnt).out","w")

    t0=time()
    ok=1
    try 
      solve(fin,fout)
    catch ;
      ok=0
    end
    t0=time()-t0

    close(fin)
    close(fout)

    finfo=open("act/$(cnt).info","w")
    s=join([string(ok),string(round(t0,digits=4))]," ")
    #println(stderr,s)
    println(finfo,s)
    close(finfo)

    cnt=cnt+1
  end
end
app()
```

## solve
```julia
function solve(fin, fout)
  n,k=parse.(Int, split(read(fin,String)))  
  println(fout,1.0-(n-k)*(n-k-1)/(n*(n-1)))
end
```

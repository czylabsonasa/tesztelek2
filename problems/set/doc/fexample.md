## gen
### app
* mindig ugyanazt az app fájlt használjuk
* hívás python esetén: ```python app.py``` módon mehet
* a munkakönytárban kell lenni a feladat io könyvtárának és a solve függvényt definiáló 
  megfelelő ```solve.*``` forrásnak - ezt kell megírnod.

---

## python
### app
* [app.py](../../_apps/app.py)

### solve
```python
# N elemű halmazbó véletlen választás
def solve(fin,fout):
  from scipy.stats import binom
  N,K=[int(v) for v in fin.read().split()]
  P=binom.pmf(K,N,0.5) # pmf=probability mass function
  fout.write("{:.12f}".format(P))
```

## octave+matlab
### app
* [app.m](../../_apps/app.m)

### solve
```matlab
function solve(fin,fout)
  v=fscanf(fin,"%d ");
  N=v(1);K=v(2);
  fprintf(fout,"%.12f\n",binopdf(K,N,0.5));
end
```


## julia
### app
* [app.jl](../../_apps/app.jl)

### solve
```julia
# N elemű halmazbó véletlen választás
using Distributions
function solve(fin,fout)
  N,K=parse.(Int, split(read(fin,String)))
  P=pdf(Binomial(N,0.5),K)
  println(fout,P)
end
```






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
def solve(fin,fout):
  fout.write(str(sum(int(v) for v in fin.read().split())))
```

## octave+matlab
### app
* [app.m](../../_apps/app.m)

### solve
```matlab
function solve(fin,fout)
  fprintf(fout, "%d\n", sum(fscanf(fin,"%d ")));
end
```


## julia
### app
* [app.jl](../../_apps/app.jl)

### solve
```julia
solve(fin,fout)=println(fout, parse.(Int, read(fin,String) |> split) |> sum )
```




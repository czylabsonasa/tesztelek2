## gen
### solve
* a megírt programnak az ```stdin/stdout```-ot kell használni.
* ```matlab```-bal nem használható (```octave``` az OK.)
* sokkal lassabb mint a ```func``` mód.
---

## python
### solve
```python
from sys import stdin, stdout
# 3 változat:
# stdout.write(str(sum(int(v) for v in stdin.read().split()))+"\n")
# print(sum(int(v) for v in stdin.read().split()))
print(sum(int(v) for v in input().split()))
```


## octave
### solve
```matlab
fprintf(stdout, "%d\n", sum(fscanf(stdin,"%d ")));
```


## julia
### solve
```julia
println(stdout, parse.(Int, read(stdin, String) |> split) |> sum )
```







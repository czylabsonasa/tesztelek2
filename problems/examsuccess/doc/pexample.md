### octave
```matlab
solve=@(N,K) 1.0-(N-K)*(N-K-1)/(N*(N-1));
inp=sscanf(fgetl(stdin),"%d ");
fprintf(stdout,"%9f\n",solve(inp(1),inp(2)));
```

### julia
```julia
solve(N,K)=1.0-(N-K)*(N-K-1)/(N*(N-1));
n,k=parse.(Int,split(readline()))
println(solve(n,k))
```

### python
```python
solve=lambda N,K : 1.0-(N-K)*(N-K-1)/(N*(N-1))
n,k=[int(v) for v in input().split()]
print(solve(n,k))
```

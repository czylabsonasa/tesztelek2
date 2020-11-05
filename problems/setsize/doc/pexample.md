### octave
```matlab
pkg load statistics
v=sscanf(fgetl(stdin),"%d ");
N=v(1);
K=v(2);
fprintf(stdout,"%.9f\n",binopdf(K,N,0.5)); # pdf=prob. density function
```

### julia
```julia
# N elemű halmazbó véletlen választás
using Distributions
N,K=parse.(Int, split(readline()))
P=pdf(Binomial(N,0.5),K) # pdf=prob. density function
println(P)
```


### python
```python
# N elemű halmazbó véletlen választás
from scipy.stats import binom
N,K=[int(v) for v in input().split()]
P=binom.pmf(K,N,0.5) # pmf=probability mass function
print(P)
```

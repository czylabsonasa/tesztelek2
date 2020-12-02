### octave
```matlab
1;
function P=solve(M)
  if M<2 
    P=0.0;
    return;
  end
  if M>365 
    P=1.0;
    return;
  end
  P=1.0-prod(1.0-(0:(M-1))/365);
end

M=sscanf(fgetl(stdin),"%d");
fprintf(stdout,"%.9f\n",solve(M));
```

### python
```python
import numpy as np
def solve(M):
  if M<2:
    return 0
  if M>365:
    return 1
  return 1.0-np.prod(1.0 - np.array(range(0,M))/365.0)

M=int(input())
print(solve(M))
```

### c/c++ - (bináris lesz ha lefordítod :-))
```C
#include <cstdio>

double solve(int M){
  if(M>365){ return 1.0; }
  if(M<2){ return 0.0; }
  double ret=1.0;
  for(int m=0; m<M; m++){
   ret*=(1.0-m/365.0);
  }
  return 1.0-ret;
}

int main(){
  int M; scanf("%d",&M);
  printf("%.12lf\n",solve(M));

  return 0;
}
```


### golang

```go
package main
  
import "fmt"
  
func main() {
  var m int64
  fmt.Scanf("%d", &m)
  
  solve := func(m int64) float64 {
    var p float64

    if m<2 {
      return 0.0
    }
    if m>365 {
      return 1.0
    }
    p=1
    m=m-1
    for ; m>0; m--{
      p=p*(1.0-float64(m)/365.0)
    }
    return 1.0-p
  }
  fmt.Println(solve(m))
}
```
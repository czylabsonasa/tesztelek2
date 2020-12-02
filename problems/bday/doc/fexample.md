## python

### app.py
* mindig ugyanazt az app fájlt használjuk - ezért nem is inkludálom többet
* hívás: python app.py
* a munkakönytárban kell lenni a feladat io könyvtárának és a solve.py megoldásnak
  de ezzel nem kell foglalkozni ha a checker-t használjuk

```python
import time
import solve

cnt=0
while True:
  inname="io/"+str(cnt)+".in"
  try:
    fin=open(inname,"r")
  except:
    break

  fout=open("act/"+str(cnt)+".out","w")

  t0=time.time()
  ok=1
  try:
    solve.solve(fin,fout)
  except:
    ok=0

  fin.close()
  fout.close()

  mt=time.time()-t0
  with open("act/"+str(cnt)+".info","w") as f:
    f.write("{:d} {:.4f}\n".format(ok, mt))

  cnt=cnt+1
```

### solve.py
```python
def solve(fin,fout):
  import numpy as np
  M=int(fin.read()) 
  P=-1.0
  while True:
    if M<2:
      P=0.0
      break
    if M>365:
      P=1.0
      break
    P=1.0-np.prod(1.0 - np.array(range(0,M))/365.0)
    break
  fout.write("{:.12f}".format(P))
```

## octave+matlab

### app.m
```matlab
cnt=0;
while true

  inname=sprintf("io/%d.in",cnt);
  inid=fopen(inname,'r');
  if inid<0
    break
  end

  outname=sprintf("act/%d.out",cnt);
  outid=fopen(outname,'w');


  tic();
  ok=1;
  try
    solve(inid,outid);
  catch
    ok=0;
  end
  mt=toc();

  fclose(inid);
  fclose(outid);

  infoname=sprintf("act/%d.info",cnt);
  infoid=fopen(infoname,'w');
  fprintf(infoid,"%d %.4f\n", ok, mt);
  fclose(infoid);

  cnt=cnt+1;
end
```


### solve.m
```matlab
function solve(fin,fout)
  M=fscanf(fin,"%d");
  P=-1;
  while true
    if M<2 
      P=0.0;
      break;
    end
    if M>365 
      P=1.0;
      break;
    end
    P=1.0-prod(1.0-(0:(M-1))/365);
    break
  end
  fprintf(fout,"%.12f\n",P);
end
```


## javascript

### app.js
```js
// szerző: Kántor Dániel (thx!)

const fs = require('fs');

const solve = require('./solve.js');

var cnt = 0;

while(true){
    let fin = `./io/${cnt}.in`;
    let fout = `./act/${cnt}.out`;


    if(!fs.existsSync(fin)) break;

    let ok = 1;
    let t0 = process.hrtime();
    try{
        solve(fin,fout);
    }
    catch(ex){
        ok = 0;
    }

    t0 = process.hrtime(t0);
    mt=t0[0]+t0[1]/1e9;

    fs.writeFileSync(`./act/${cnt}.info`,`${ok} ${mt.toFixed(4)}`);
    
    cnt++;
}
```


### solve.js
```js
// Kántor Dániel bday2 megoldásából:
const fs = require('fs');

var solve = (fin,fout) => {
  let M = parseInt(fs.readFileSync(fin,'utf-8'));
  let result=calculate(M);
  fs.writeFileSync(fout,result.toFixed(12).toString(),{flags:'wx'});
};

var calculate = (M) => {
  if(M > 365) return 1.0;
  if(M < 2) return 0.0;

  let result = 1.0;
  for(let i = 0;i<M;i++){
    result *= (1 - i / 365);
  }
  return 1 - result;
};

module.exports = solve;
```
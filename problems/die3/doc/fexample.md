### octave + matlab
```matlab
function solve(fin, fout)
  pre=zeros(1,6);
  p=1/6^2;
  for i=1:6
    for j=1:6
      m=max(i,j);
      pre(m)=pre(m)+p;
    end
  end

  S=fscanf(fin,"%d");
  P=0.0;
  if S>0 && S<7
    P=pre(S);
  end
  fprintf(fout,"%.12f\n",P);
```

### python
```python
def solve(fin,fout):
  pre=[0]*7
  p=1.0/6.0**2
  for i in range(1,7):
    for j in range(1,7):
      pre[max(i,j)]+=p

  S=int(fin.read())
  P=0.0
  if S>0 and S<7:
    P=pre[S]
  fout.write("{:.12f}".format(P))
```


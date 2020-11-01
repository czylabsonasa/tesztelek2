## python
* az ```app``` mindig ugyanaz

```python
def solve(fin,fout):
  pre=[0]*19
  p=1.0/6.0**3
  for i in range(1,7):
    for j in range(1,7):
      for k in range(1,7):
        pre[i+j+k]+=p

  S=int(fin.read())
  P=0.0
  if S>2 and S<19:
    P=pre[S]
  fout.write("{:.12f}".format(P))
```

### octave + matlab
```matlab
function solve(fin,fout)
  pre=zeros(1,6*3);
  p=1/6^3;
  for i=1:6
    for j=1:6
      for k=1:6
        pre(i+j+k)=pre(i+j+k)+p; % matlab-ban nincsen +=
      end
    end
  end
  S=fscanf(fin,"%d");
  P=0.0;
  if S>2 && S<19
    P=pre(S);
  end
  fprintf(fout,"%.12f\n",P);
end
```



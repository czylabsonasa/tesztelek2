### octave
```matlab
pre=zeros(1,6*3);
p=1/6^3;
for i=1:6
  for j=1:6
    for k=1:6
      pre(i+j+k)+=p;
    end
  end
end

S=sscanf(fgetl(stdin),"%d");
P=0.0;
if S>2 && S<19
  P=pre(S);
end
fprintf(stdout,"%.12f\n",P);
```

### python
```python
pre=[0]*19
p=1.0/6.0**3
for i in range(1,7):
  for j in range(1,7):
    for k in range(1,7):
      pre[i+j+k]+=p

S=int(input())
P=0.0
if S>2 and S<19:
  P=pre[S]
print(P)
```

### julia
```julia
pre=fill(0.0, 6*3)
p=(1.0/6.0)^3
for i=1:6,j=1:6,k=1:6 
  pre[i+j+k]+=p
end

S=parse(Int,readline())
println(2<S<19 ? pre[S] : 0.0)
```

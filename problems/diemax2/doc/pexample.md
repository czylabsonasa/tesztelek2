### octave
```matlab
pre=zeros(1,6);
p=1/6^2;
for i=1:6
  for j=1:6
      pre(max(i,j))+=p;
  end
end

S=sscanf(fgetl(stdin),"%d");
P=0.0;
if S>0 && S<7
  P=pre(S);
end
fprintf(stdout,"%.12f\n",P);
```


### julia
```julia
pre=fill(0.0, 6)
p=(1.0/6.0)^2
for i=1:6,j=1:6
  pre[max(i,j)]+=p
end

S=parse(Int,readline())
println(0<S<7 ? pre[S] : 0.0)
```


### python
```python
pre=[0]*7
p=1.0/6.0**2
for i in range(1,7):
  for j in range(1,7):
    pre[max(i,j)]+=p

S=int(input())
P=0.0
if S>0 and S<7:
  P=pre[S]
print(P)
```

% tudjuk hogy milyen mátrix adat -> 2x4-es
v=fscanf(stdin, "%f "); # oszlopvektor 8x1-es
v=reshape(v,4,2)' # oszlopfolytonosan tölti fel
A=v(:,1:2)
B=v(:,3:4)
C=A*B # =A mert B egységmátrix

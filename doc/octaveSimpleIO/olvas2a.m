v=dlmread(stdin) # téglalap-szerű táblázat esetén egyszerű mód olvasásra
A=v(:,1:2)
B=v(:,3:4)
C=A*B # =A mert B egységmátrix

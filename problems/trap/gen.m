1;

function doit(C,a,b,m,T,name)
  name
  fin=fopen(sprintf("io/%s.in",name),"w");
  fprintf(fin,"%.3f ",C);
  fprintf(fin,"\n");
  fprintf(fin,"%d %d %d\n",a,b,m);
  fclose(fin);
  
  fout=fopen(sprintf("io/%s.out",name),"w");
  fprintf(fout,"%.12f\n",T);
  fclose(fout);
end



C=randi([-10,10],1,8)/10;
F=@(x) C(1)*exp(C(2)*x)+C(3)*sin(C(4)*x)+C(5)*cos(C(6)*x)+C(7)*sin(exp(C(8)*x));  
for cnt=6:30
  cnt
  a=randi([-5,5]); b=a+randi(5);
  m=randi([30,1000]);
  x=linspace(a,b,m+1);
  T=trapz(x,F(x));
  doit(C,a,b,m,T,sprintf("%d",cnt));
end



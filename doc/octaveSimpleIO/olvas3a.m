# változó sorhossz - tudjuk milyen hosszuak a sorok
h=[1,2,3,4,3,2,1]; # a hosszak
for k=1:length(h)
  v=fscanf(stdin,"%f ",[1,h(k)]);
  fprintf(stdout,"%f ",v);
  fprintf(stdout,"\n");
end

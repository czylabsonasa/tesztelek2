# változó sorhossz - nem tudjuk milyen hosszuak a sorok
for k=1:3
  v=sscanf(fgetl(stdin),"%f ");
  fprintf(stdout,"%f ",v);
  fprintf(stdout,"\n");
end

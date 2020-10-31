cnt=0;
while true

  inname=sprintf("io/%d.in",cnt);
  inid=fopen(inname,'r');
  if inid<1
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

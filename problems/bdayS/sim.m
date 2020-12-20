function sim(M, ISM, nev)
  Y = zeros(1,ISM); # 1 ha a megfigyelt sokaságban van bday azonosság
  X=1:ISM;

  tt=tic();
  for k = X
    akt=randi(365,M,1);
    [frek,kp]=hist(akt,1:365);
    Y(k)=any(frek>1);
  end
  Y = cumsum(Y) ./ X; # relatív gyakoriságok
  tt=toc(tt);

  plot(X, Y, '.');
  title(sprintf("bday, M=%d, ISM=%d, t=%.2fs",M, ISM, tt));
  xlabel('number of observations');
  ylabel('relative frequency');
  yticks(0:0.1:1);
  ylim([0,1]);

  
  saveas(gcf, nev);
end
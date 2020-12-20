### egy lehetséges megvalósítás

```matlab
function sim(M, ISM, nev) % a nev a kép neve 
  Y = zeros(1,ISM); % 1 ha a megfigyelt sokaságban van bday azonosság
  X=1:ISM;

  tt=tic();
  for k = X
    akt=randi(365,M,1); % megfigyelünk egy M elemű társaságot
    [frek,kp]=hist(akt,1:365); % gyakoriságok
    Y(k)=any(frek>1); % ha van azonosság 1-re állítjuk
  end
  Y = cumsum(Y) ./ X; % relatív gyakoriságok
  tt=toc(tt);

  plot(X, Y, '.');
  title(sprintf("bday, M=%d, ISM=%d, t=%.2fs",M, ISM, tt));
  xlabel('number of observations');
  ylabel('relative frequency');
  yticks(0:0.1:1);
  ylim([0,1]);

  
  saveas(gcf, nev);
end
```
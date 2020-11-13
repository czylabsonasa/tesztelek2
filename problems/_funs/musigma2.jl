function musigma2(v,p)
  mu=sum(v.*p)
  sigma2=sum(p.*(v .- mu).^2)
  mu, sigma2
end
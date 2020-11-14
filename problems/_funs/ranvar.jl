function musigma2(;prob,val)
  mu=sum(val.*prob)
  sigma2=sum(prob.*(val .- mu).^2)
  mu, sigma2
end

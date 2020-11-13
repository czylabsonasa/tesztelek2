function tstring(A::Array{String,2})
  m,_=size(A)
  join( [ join(A[r,:]," ") for r = 1:m] , "\n")
end
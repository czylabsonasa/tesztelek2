function rstring(A::Array{String,1}; delim= " ")
  join(A , delim)
end

function rstring(A::Array{String,2})
  m,_=size(A)
  rstring([ rstring(A[r,:]) for r = 1:m ] , delim="\n")
end

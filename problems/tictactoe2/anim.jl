using Plots

p = plot([sin, cos], zeros(0), leg = false, xlims = (0, 2π), ylims = (-1, 1))
anim = Animation()
for x = range(0, stop = 2π, length = 50)
    push!(p, x, Float64[sin(x), cos(x)])
    frame(anim)
end
gif(anim, "anim.gif", fps=15)
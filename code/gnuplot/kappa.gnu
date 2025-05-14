unset terminal
reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'


# Define parameters
l = 1.0        # Set l value
gamma = 1.0    # Set gamma value

# Define the range for v
v_max = (1.0 - l**2/2)**(1.0/(2.0*gamma))

# Set plot properties
set xrange [0:v_max]
set yrange [0.8:1.0]
#set xlabel "$v$"
#set ylabel "$\\kappa$"
unset xlabel
unset ylabel
set key top left
unset grid
set bmargin 3.5

# Define the function
f(v) = (1/pi) * (l / sqrt(1 - v**2 * gamma)) * sqrt(2 - (l**2 / (1 - v**2 * gamma))) \
       + (2/pi) * atan( (l / sqrt(1 - v**2 * gamma)) / sqrt(2 - (l**2 / (1 - v**2 * gamma))) )

set style line 1 lt 2 lw 2 lc rgb "black" dt "-"

intercept = 0.45

set arrow from intercept, 0.8 to intercept, f(intercept) nohead ls 1
set arrow from 0, f(intercept) to intercept, f(intercept) nohead ls 1

set xtics (0, "$v_\\star$" intercept, "$\\left(1 - \\frac{\\ell^2}{2}\\right)^{1/(2\\gamma)}$" v_max)

set ytics ("$\\kappa_\\mathrm{min}$" f(0.0), "$\\kappa$" f(intercept), 1)

# Plot the function
plot f(x) with lines linewidth 2 title ""

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/kappa.eps && mv output.pdf ./figures/kappa.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')

unset terminal
set out
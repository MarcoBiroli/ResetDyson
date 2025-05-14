reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

set multiplot

# Main plot settings
set origin 0,0
set size 1,1
unset grid
set yrange [0:11]
set xrange [-0.01:1.5]
set key top left height 1
set xlabel "$\\ell = L \\sqrt{\\frac{\\mu}{N D}}$"
set ylabel "$\\frac{\\beta \\pi^2}{2} \\mathrm{Var}[N_L]$"
set bmargin 3.5
set xtics (0, 0.2, 0.4, 0.6, 0.8, 1, 1.2)

set xtics add ("$\\sqrt{2}$" 1.414)

plot "histograms/fcs_var/th_r0.out" with line title "$r = 0$"

# Inset plot settings
set origin 0.2,0.15  # Position of the inset (bottom-left corner)
set size 0.7, 0.5   # Size of the inset
set xrange [0.001:sqrt(2)]     # Inset x-range
set samples 10000
unset yrange
set xlabel "$\\log(\\ell)$"
set ylabel "$\\mathrm{Var}[N_L]$"
unset key
set logscale x 10
unset xtics
#set xtics ("$\\sqrt{2}$" 1.414)
unset ytics
plot log(10000*x*(2 - x**2)**(3/2)) title ""

unset multiplot

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/fcs_var_r0.eps && mv output.pdf ./figures/fcs_var_r0.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
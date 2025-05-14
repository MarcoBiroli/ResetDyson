reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0.0001:0.05]
set xrange [0:sqrt(2)]
set key top right height 1
set xlabel "$\\ell = L \\sqrt{\\frac{\\mu}{N D}}$"
set ylabel "$\\mathrm{Var}[N_L] / N^2$"
set bmargin 3.5
#set logscale y 10

set xtics (0, 0.2, 0.4, 0.6, 0.8, 1, 1.2)

set xtics add ("$\\sqrt{2}$" 1.414)

plot "histograms/fcs_var/S1000.N1000.G1.L.b2.out" title "" lc 1 pt 1, \
        "histograms/fcs_var/S1000.N1000.G0.5.L.b2.out" title "" lc 2 pt 1, \
        "histograms/fcs_var/S1000.N1000.G0.25.L.b2.out" title "" lc 3 pt 1, \
        "histograms/fcs_var/th.G1.out" lc 1 with line title "$\\gamma = 1.0$", \
        "histograms/fcs_var/th.G0.5.out" lc 2 with line title "$\\gamma = 0.5$", \
        "histograms/fcs_var/th.G0.25.out" lc 3 with line title "$\\gamma = 0.25$"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/fcs_var.eps && mv output.pdf ./figures/fcs_var.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
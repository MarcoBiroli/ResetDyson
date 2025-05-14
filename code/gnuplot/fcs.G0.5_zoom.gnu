reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0.001:20]
set xrange [0.9:1]
set key top left title "$\\gamma = 0.5$\\vspace{-20pt}" columns 2 height 3
set xlabel "$N_L / N$"
set ylabel "$N \\cdot {Prob.}[N_L]$"
set bmargin 3.5

set logscale x 10
set logscale y 10

plot "histograms/fcs/S10000.N1000.G0.5.L0.1.b4.out" title "" lc 1 pt 1, \
        "histograms/fcs/S10000.N1000.G0.5.L0.1.b2.out" title "" lc 1 pt 2, \
        "histograms/fcs/S10000.N1000.G0.5.L0.1.b1.out" title "" lc 1 pt 4, \
        "histograms/fcs/th.G0.5.L0.1.out" title "$\\ell = 0.1$" lc 1 with line, \
        "histograms/fcs/S10000.N1000.G0.5.L0.5.b4.out" title "" lc 2 pt 1, \
        "histograms/fcs/S10000.N1000.G0.5.L0.5.b2.out" title "" lc 2 pt 2, \
        "histograms/fcs/S10000.N1000.G0.5.L0.5.b1.out" title "" lc 2 pt 4, \
        "histograms/fcs/th.G0.5.L0.5.out" title "$\\ell = 0.5$" lc 2 with line, \
        "histograms/fcs/S10000.N1000.G0.5.L1.b4.out" title "" lc 3 pt 1, \
        "histograms/fcs/S10000.N1000.G0.5.L1.b2.out" title "" lc 3 pt 2, \
        "histograms/fcs/S10000.N1000.G0.5.L1.b1.out" title "" lc 3 pt 4, \
        "histograms/fcs/th.G0.5.L1.out" title "$\\ell = 1$" lc 3 with line, \
        NaN with points lc 0 pt 1 title "$\\beta = 4$", \
        NaN with points lc 0 pt 2 title "$\\beta = 2$", \
        NaN with points lc 0 pt 4 title "$\\beta = 1$"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/fcs.G0.5_zoom.eps && mv output.pdf ./figures/fcs.G0.5_zoom.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
unset terminal
reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:1]
set xrange [-sqrt(2):sqrt(2)]
set key top right columns 2 width 5 height 0.5
set xlabel "$x \\sqrt{\\frac{\\mu}{N D}}$"
set ylabel "$\\rho_N(x|r) / \\sqrt{ \\frac{\\mu}{N D} }$"
set bmargin 3.5


plot "histograms/density/S10000.N1000.G0.5.b2.out" title "" lc 2 pt 1, \
        "histograms/density/S10000.N1000.G0.5.b1.out" title "" lc 2 pt 2, \
        "histograms/density/S10000.N1000.G0.5.b0.5.out" title "" lc 2 pt 4, \
        "histograms/density/th.G0.5.out" with line title "$\\gamma = 0.5$" lc 2, \
        "histograms/density/S10000.N1000.G1.b2.out" title "" lc 1 pt 1, \
        "histograms/density/S10000.N1000.G1.0.b1.out" title "" lc 1 pt 2, \
        "histograms/density/S10000.N1000.G1.b0.5.out" title "" lc 1 pt 4, \
        "histograms/density/th.G1.out" with line title "$\\gamma = 1.0$" lc 1, \
        "histograms/density/S10000.N1000.G2.b2.out" title "" lc 3 pt 1, \
        "histograms/density/S10000.N1000.G2.0.b1.out" title "" lc 3 pt 2, \
        "histograms/density/S10000.N1000.G2.b0.5.out" title "" lc 3 pt 4, \
        "histograms/density/th.G2.out" with line title "$\\gamma = 2.0$" lc 3, \
        NaN with points pt 1 lc rgb "black" title "$\\beta = 2$", \
        NaN with points pt 2 lc rgb "black" title "$\\beta = 1$", \
        NaN with points pt 4 lc rgb "black" title "$\\beta = 0.5$"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/density.eps && mv output.pdf ./figures/density.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')

unset terminal
set out
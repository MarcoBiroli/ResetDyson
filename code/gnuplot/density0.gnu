reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:1.2]
set xrange [-3:3]
set key top right spacing 1.25
set xlabel "$x \\sqrt{\\frac{r}{4 N D}}$"
set ylabel "$\\rho_N(x|r, \\mu = 0) / \\sqrt{ \\frac{r}{4 N D} }$"
set bmargin 3.5


plot "histograms/density/S10000.N1000.G0.b2.out" title "" lc 1 pt 1, \
    "histograms/density/S10000.N1000.G0.b1.out" title "" lc 1 pt 2, \
    "histograms/density/S10000.N1000.G0.b0.5.out" title "" lc 1 pt 4, \
    "histograms/density/th.G0.out" with line title "$\\mu = 0$" lc 1, \
    NaN with points pt 1 lc rgb "black" title "$\\beta = 2.0$", \
    NaN with points pt 2 lc rgb "black" title "$\\beta = 1.0$", \
    NaN with points pt 4 lc rgb "black" title "$\\beta = 0.5$"


unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/density0.eps && mv output.pdf ./figures/density0.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')

unset terminal
set out
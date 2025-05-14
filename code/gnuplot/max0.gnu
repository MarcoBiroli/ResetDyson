reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:0.7]
set xrange [0:4]
set key top right height 2 spacing 1.25
set xlabel "$x_{\\mathrm{max}} \\sqrt{\\frac{r}{4 N D}}$"
set ylabel "${Prob.}[x_{\\mathrm{max}}] / \\sqrt{ \\frac{r}{4 N D} }$"
set bmargin 3.5


plot "histograms/max/S100000.N1000000000.G0.b2.out" title "" lc 1 pt 1, \
"histograms/max/S100000.N1000000000.G0.b1.out" title "" lc 1 pt 2, \
"histograms/max/S100000.N1000000000.G0.b0.5.out" title "" lc 1 pt 4, \
    "histograms/max/th.G0.out" title "$\\mu = 0$" with line lc 1, \
    NaN with points pt 1 lc rgb "black" title "$\\beta = 2.0$", \
    NaN with points pt 2 lc rgb "black" title "$\\beta = 1.0$", \
    NaN with points pt 4 lc rgb "black" title "$\\beta = 0.5$"

unset logscale
unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/max0.eps && mv output.pdf ./figures/max0.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
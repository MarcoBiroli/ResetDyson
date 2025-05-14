reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0.01:10]
set xrange [0:sqrt(2)]
set key bottom center columns 2 height 0.5
set xlabel "$x_{\\mathrm{max}} \\sqrt{\\frac{\\mu}{N D}}$"
set ylabel "${Prob.}[x_{\\mathrm{max}}] / \\sqrt{ \\frac{\\mu}{N D} }$"
set logscale y 10
set bmargin 3.5

set xtics (0, 0.2, 0.4, 0.6, 0.8, 1, 1.2)
set xtics add ('$ \sqrt{2} $' 1.414)



plot "histograms/max/S100000.N1000000000.G0.25.b2.out" title "" lc 1 pt 1, \
        "histograms/max/S100000.N1000000000.G0.25.b1.out" title "" lc 1 pt 2, \
        "histograms/max/S100000.N1000000000.G0.25.b0.5.out" title "" lc 1 pt 4, \
        "histograms/max/th.G0.25.out" title "$\\gamma = 0.25$" with line lc 1, \
        "histograms/max/S100000.N1000000000.G0.5.b2.out" title "" lc 2 pt 1, \
        "histograms/max/S100000.N1000000000.G0.5.b1.out" title "" lc 2 pt 2, \
        "histograms/max/S100000.N1000000000.G0.5.b0.5.out" title "" lc 2 pt 4, \
        "histograms/max/th.G0.5.out" title "$\\gamma = 0.5$" with line lc 2, \
        "histograms/max/S100000.N1000000000.G1.b2.out" title "" lc 3 pt 1, \
        "histograms/max/S100000.N1000000000.G1.b1.out" title "" lc 3 pt 2, \
        "histograms/max/S100000.N1000000000.G1.b0.5.out" title "" lc 3 pt 4, \
        "histograms/max/th.G1.out" title "$\\gamma = 1.0$" with line lc 3, \
        NaN with points pt 1 lc rgb "black" title "$\\beta = 2.0$", \
        NaN with points pt 2 lc rgb "black" title "$\\beta = 1.0$", \
        NaN with points pt 4 lc rgb "black" title "$\\beta = 0.5$"

unset logscale
unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/max.eps && mv output.pdf ./figures/max.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
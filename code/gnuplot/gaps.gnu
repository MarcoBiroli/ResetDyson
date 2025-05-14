reset session
set terminal epslatex color standalone ps 3 lw 3
set output 'output.tex'

set grid
set yrange [0:0.8]
set xrange [0:7]
set key top right
set xlabel "$s \\sqrt{\\frac{\\mu \\beta}{N D}}$"
set ylabel "${Prob.}[s] / \\sqrt{ \\frac{\\mu \\beta}{N D} }$"
set bmargin 3.5

plot "histograms/gaps/S1000.N1000.G0.5.b4.out" title "" lc 1 pt 1, \
    "histograms/gaps/th.G0.5.b4.out" title "$\\gamma = 0.5$" lc 1 with line, \
    "histograms/gaps/th.G0.5.b1.out" title "$\\gamma = 0.5$" lc 1 with line, \
    "histograms/gaps/th.G0.5.b0.5.out" title "$\\gamma = 0.5$" lc 1 with line, \
    "histograms/gaps/S1000.N1000.G1.out" lc 2 pt 1 title "", \
    "histograms/gaps/th.G1.out" title "$\\gamma = 1.0$" with line lc 2, \
    "histograms/gaps/S1000.N1000.G100.out" title "" lc 3 pt 1, \
    "histograms/gaps/th.G100.out" with line lc 3 title "$\\gamma = 100$"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/gaps.eps && mv output.pdf ./figures/gaps.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:0.45]
set xrange [0:8]
set key top right height 1
set xlabel "$\\bar{s} \\cdot C(\\gamma)$"
set ylabel "${Prob.}[\\bar{s}] / C(\\gamma)$"
set bmargin 3.5


plot "histograms/gaps/S1000000.N2.G0.5.b4.out" title "" lc 1 pt 4, \
"histograms/gaps/S1000.N1000.G0.5.b4.out" title "" lc 1 pt 1, \
    "histograms/gaps/th.G0.5.b4.out" title "$\\gamma = 0.5$" lc 1 with line, \
    "histograms/gaps/S1000000.N2.G1.b4.out" lc 2 pt 4 title "", \
    "histograms/gaps/S1000.N1000.G1.b4.out" lc 2 pt 1 title "", \
    "histograms/gaps/th.G1.b4.out" title "$\\gamma = 1.0$" with line lc 2, \
    "histograms/gaps/S1000000.N2.G100.b4.out" title "" lc 3 pt 4, \
    "histograms/gaps/S1000.N1000.G100.b4.out" title "" lc 3 pt 1, \
    "histograms/gaps/th.G100.b4.out" with line lc 3 title "$\\gamma = 100$", \
    NaN with points lc 0 pt 4 title "$N = 2$", \
    NaN with points lc 0 pt 1 title "$N = 1000$"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/gaps4.eps && mv output.pdf ./figures/gaps4.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
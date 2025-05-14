reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0.005:0.6]
set xrange [0.01:1]
set key bottom right
set xlabel "$\\bar{s} \\cdot C(\\gamma)$"
set ylabel "${Prob.}[\\bar{s}] / C(\\gamma)$"
set bmargin 3.5
set logscale x 10
set logscale y 10

# f(x) = x/(2 * 1 * (4 - 1))
f(x) = x / (2 * 1 * (2 - 1))
g(x) = - x * log(x) / 2
h(x) = sqrt(x) * 1.51
# h(x) = x / (2 * 1 * (2 - 1))

plot "histograms/gaps/S1000000.N2.G1.b2.out" lc 1 pt 1 title "", \
    "histograms/gaps/th.G1.b2.out" title "$\\beta = 2.0$" with line lc 1, \
    "histograms/gaps/S1000000.N2.G1.b1.out" lc 2 pt 1 title "", \
    "histograms/gaps/th.G1.b1.out" title "$\\beta = 1.0$" with line lc 2, \
    "histograms/gaps/S1000000.N2.G1.b0.5.out" lc 3 pt 1 title "", \
    "histograms/gaps/th.G1.b0.5.out" title "$\\beta = 0.5$" with line lc 3, \
    f(x) title "" lc 0, g(x) title "" lc 0, h(x) title "" lc 0, \
    NaN with line lc 0 title "Small $z$ asymptotic"

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/gapssmallz.eps && mv output.pdf ./figures/gapssmallz.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
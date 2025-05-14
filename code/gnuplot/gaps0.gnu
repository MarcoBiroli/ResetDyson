reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:0.6]
set xrange [0:7]
set key top right
set xlabel "$s \\sqrt{\\frac{\\mu \\beta}{N D}}$"
set ylabel "${Prob.}[s] / \\sqrt{ \\frac{\\mu \\beta}{N D} }$"
set bmargin 3.5

plot "histograms/gaps/th.G0.out" title "$\\gamma = 0$" lc 1 with line, "histograms/gaps/S1000.N1000.G0.out" title "$N = 1000$" lc 2 pt 1, \
    "histograms/gaps/S1000000.N2.G0.out" title "$N = 2$" lc 3 pt 1,

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/gaps0.eps && mv output.pdf ./figures/gaps0.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
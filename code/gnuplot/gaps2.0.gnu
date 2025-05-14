reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:0.6]
set xrange [0:7]
set key top right
set xlabel "$\\bar{s} \\sqrt{\\frac{\\pi}{2}}$"
set ylabel "${Prob.}[\\bar{s}] / \\sqrt{ \\frac{\\pi}{2} }$"
set bmargin 3.5


plot "histograms/gaps/S1000000.N2.G0.out" title "" lc 1 pt 1, "histograms/gaps/th.G0.out" title "$\\gamma = 0$" lc 1 with line, 

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/gaps20.eps && mv output.pdf ./figures/gaps20.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
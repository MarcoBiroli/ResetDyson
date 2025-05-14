reset session
set terminal epslatex color standalone ps 3 lw 3 ',14pt'
set output 'output.tex'

unset grid
set yrange [0:0.07]
set xrange [0:10]
set key top right height 1
set xlabel "$\\tilde{r} = \\frac{r L^2}{N D}$"
set ylabel "$\\mathrm{Var}[N_L] / N^2$"
set bmargin 3.5
#set logscale y 10

plot "histograms/fcs_var/S1000.N1000.G0.L.b2.out" title "" lc 1 pt 1, \
        "histograms/fcs_var/th.G0.out" lc 1 with line title "$\\mu = 0$", 

unset out
set out

system('latex output.tex && dvips output.dvi && ps2pdf output.ps')
system('mv output.ps ./figures/fcs_var0.eps && mv output.pdf ./figures/fcs_var0.pdf')
system('rm output.aux && rm output.dvi && rm output.log && rm output.tex && rm output-inc.eps')
unset terminal
set out
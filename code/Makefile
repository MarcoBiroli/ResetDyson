density:
	python density.py -S $S -N $N -r 1 -mu $G -D 1 -b $b -f "results/density/S$S.N$N.G$G.b$b.out"
	python binning.py -i "results/density/S$S.N$N.G$G.b$b.out" -o "histograms/density/S$S.N$N.G$G.b$b.out" -b $B
	python density_theoretical.py -g $G -f "histograms/density/th.G$G.out"

rebin_density:
	python binning.py -i "results/density/S$S.N$N.G$G.b$b.out" -o "histograms/density/S$S.N$N.G$G.b$b.out" -b $B

max:
	python max.py -S $S -N $N -r 1 -mu $G -D 1 -beta $b -f "results/max/S$S.N$N.G$G.b$b.out"
	python binning.py -i "results/max/S$S.N$N.G$G.b$b.out" -o "histograms/max/S$S.N$N.G$G.b$b.out" -b $B
	python max_theoretical.py -g $G -f "histograms/max/th.G$G.out"

rebin_max:
	python binning.py -i "results/max/S$S.N$N.G$G.b$b.out" -o "histograms/max/S$S.N$N.G$G.b$b.out" -b $B

gaps:
	python gaps.py -S $S -N $N -r 1 -mu $G -D 1 -beta $b -f "results/gaps/S$S.N$N.G$G.b$b.out"
	python binning.py -i "results/gaps/S$S.N$N.G$G.b$b.out" -o "histograms/gaps/S$S.N$N.G$G.b$b.out" -b $B
	python gap_theoretical.py -g $G -b $b -f "histograms/gaps/th.G$G.b$b.out"

rebin_gaps:
	python binning.py -i "results/gaps/S$S.N$N.G$G.b$b.out" -o "histograms/gaps/S$S.N$N.G$G.b$b.out" -b $B

fcs:
	python fcs.py -S $S -N $N -r 1 -mu $G -D 1 -beta $b -ell $L -f "results/fcs/S$S.N$N.G$G.L$L.b$b.out"
	python binning.py -i "results/fcs/S$S.N$N.G$G.L$L.b$b.out" -o "histograms/fcs/S$S.N$N.G$G.L$L.b$b.out" -b $B
	python fcs_theoretical.py -g $G -l $L -f "histograms/fcs/th.G$G.L$L.out"

rebin_fcs:
	python binning.py -i "results/fcs/S$S.N$N.G$G.L$L.b$b.out" -o "histograms/fcs/S$S.N$N.G$G.L$L.b$b.out" -b $B

fcs_var:
	python fcs_var.py -S $S -N $N -r 1 -mu $G -D 1 -beta $b -f "histograms/fcs_var/S$S.N$N.G$G.L$L.b$b.out"




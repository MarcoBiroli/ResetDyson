# ResetDyson – _code for “Resetting Dyson Brownian Motion”_

[![arXiv](https://img.shields.io/badge/arXiv-2503.14733-B31B1B.svg)](https://arxiv.org/abs/2503.14733)
![Made with Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)

**ResetDyson** collects the analytical calculations, symbolic notebooks and Monte-Carlo/ODE code that accompany the paper  
> **M. Biroli, S. N. Majumdar & G. Schehr, “Resetting Dyson Brownian Motion” (2025)** 

The repository lets you

* reproduce every figure and numerical check in the manuscript;  
* experiment with the large-\(N\) density, edge statistics and gap/FCS distributions of the *β-RDBM*;  
* explore the Mathematica derivations that lead to the exact stationary joint law.

---

## Contents

| Path | What’s inside |
|------|---------------|
| `code/` | stand-alone Python scripts that generate raw data for the paper – see below |
| `paper/` | complete LaTeX source of the article, ready for *arXiv/APS* compilation |
| `tex_figures/` | the PDF/PGF figures included by `paper/main.tex` |
| `.gitignore` | housekeeping (keeps outputs out of version control) |

---

## Quick start

Run the following to clone the repository and create the conda environment with the necessary packages to run the code.
```bash
# clone & enter
git clone https://github.com/MarcoBiroli/ResetDyson.git
cd ResetDyson

# create conda environment
# you may need to replace the conda path in create_env.sh with your own
./source/create_env.sh 
```

All the code to generate the data from our paper is in the `code` folder which contains a Makefile exposing simple commands to run our simulations. For example, to re-create the data for the density in the NESS you can run

```bash
cd code

make density S=10000 N=1000 G=0.5 b=0.5 B=auto
```

The different parameters are:
 - `S` the number of samples
 - `N` the number of particles
 - `G` the dimensionless gamma value as explained in the paper
 - `b` beta, Dyson's index
 - `B` the number of bins to use when binning the data, either an integer number of auto.

After having created the necessary data, you can re-obtain the plots from our paper by using the corresponding `.gnu` files in the `code/gnuplot` folder. 


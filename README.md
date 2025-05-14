# ResetDyson – _code & data for “Resetting Dyson Brownian Motion”_

[![arXiv](https://img.shields.io/badge/arXiv-2503.14733-B31B1B.svg)](https://arxiv.org/abs/2503.14733)
![Made with Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)
![Mathematica 13+](https://img.shields.io/badge/Mathematica-13%2B-orange)

**ResetDyson** collects the analytical calculations, symbolic notebooks and Monte-Carlo/ODE code that accompany the paper  
> **M. Biroli, S. N. Majumdar & G. Schehr, “Resetting Dyson Brownian Motion” (2025)** 

The repository lets you

* reproduce every figure and numerical check in the manuscript;  
* experiment with the large-\(N\) density, edge statistics and gap/FCN distributions of the *β-RDBM*;  
* explore the Mathematica derivations that lead to the exact stationary joint law.

---

## Contents

| Path | What’s inside |
|------|---------------|
| `code/` | stand-alone Python scripts (no notebook overhead) that generate raw data & plots for the paper – see below |
| `paper/` | complete LaTeX source of the article, ready for *arXiv/APS* compilation |
| `tex_figures/` | the PDF/PGF figures included by `paper/main.tex` |
| `density.py` | minimal reference implementation of the large-\(N\) density in the NESS |
| `density.nb` | Mathematica notebook showing the symbolic steps of the Coulomb-gas saddle |
| `.gitignore` | housekeeping (keeps outputs out of version control) |

<details>
<summary>Language mix (LOC-weighted)</summary>

- Mathematica ≈40 %  
- TeX ≈32 %  
- Jupyter ≈13 %  
- Python ≈ 8 %  
- Gnuplot ≈ 6 %   :contentReference[oaicite:1]{index=1}
</details>

---

## Quick start

```bash
# clone & enter
git clone https://github.com/MarcoBiroli/ResetDyson.git
cd ResetDyson

# (optional) create an isolated environment
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt     # see list below

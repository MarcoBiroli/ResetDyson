import numpy as np
import argparse 
from tqdm import tqdm
from sample_RMT import sample_eigvals_large_Gaussian

def sample_dynamic_Gaussian(N  : int,
                            mu : float,
                            D  : float,
                            t  : float,
                            beta : int,
                            L : float, 
                            repeats : int):
    
    if mu != 0:
        var = np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu))
    else:
        var = np.sqrt(2 * D * t)

    var = var.reshape(-1, 1)
    eigvals = sample_eigvals_large_Gaussian(N, beta, 1, repeats)
    eigvals = eigvals * var
    fcs = np.sum((eigvals < L) * (eigvals > -L), axis = 1)
    return fcs

def sample_reset_Gaussian(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int,
                     L : float,
                     repeats : int):
    tau = np.random.exponential(scale = 1/r, size=(repeats,))
    return sample_dynamic_Gaussian(N, mu, D, tau, beta, L, repeats)

def sampling_loop(S, r, N, mu, D, beta, ell, **kwargs):

    if mu != 0:
        L = ell * np.sqrt(N * D / (mu))
    else:
        L = np.sqrt(ell * N * D / (r))
    out = sample_reset_Gaussian(r, N, mu, D, beta, L, S)

    gamma = mu / r
    c = 1/N

    out = out * c
    
    return out

def main():
    parser = argparse.ArgumentParser(prog="Eigenvalue sampling for resetting GOE")
    parser.add_argument("-S", type = int, help="Number of independent samples to draw")
    parser.add_argument("-N", type = int, help="Size of the random matrix")
    parser.add_argument("-r", type = float, help = "Resetting rate")
    parser.add_argument("-mu", type = float, help = "Trapping stiffness")
    parser.add_argument("-D", type = float, help = "Diffusion constant")
    parser.add_argument("-beta", type = float, help = "Dyson index")
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    if args.mu != 0:
        ell_tab = np.linspace(0, np.sqrt(2), 25)
    else:
        ell_tab = np.linspace(0, 10, 50)
    var_tab = []

    for ell in tqdm(ell_tab):
        out = sampling_loop(**vars(args), ell=ell)
        var_tab.append(np.var(out))
        
    with open(args.f, "w") as f:
        for e, v in zip(ell_tab, var_tab):
            f.write(f'{e}, {v}\n')
    return

if __name__=="__main__":
    main()


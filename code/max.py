import numpy as np
import argparse 
from sample_RMT import sample_maxeigval_large_Gaussian

def sample_dynamic_Gaussian(N  : int,
                            mu : float,
                            D  : float,
                            t  : float,
                            beta : int, 
                            repeats : int):
    if mu != 0:
        var = np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu)) 
    else:
        var = np.sqrt(2 * D * t)

    maxeigval = sample_maxeigval_large_Gaussian(N, beta, 1, repeats)
    maxeigval = maxeigval * var
    return maxeigval

def sample_reset_Gaussian(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int,
                     repeats : int):
    tau = np.random.exponential(scale = 1/r, size=(repeats,))
    return sample_dynamic_Gaussian(N, mu, D, tau, beta, repeats)

def sampling_loop(S, r, N, mu, D, beta, **kwargs):

    out = sample_reset_Gaussian(r, N, mu, D, beta, S)

    if mu != 0:
        c = np.sqrt(N * D / (mu)) 
        out = out / c
    else:
        c = np.sqrt(2 * N * D / (r))
        out = out / c

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

    out = sampling_loop(**vars(args))
        
    with open(args.f, "w") as f:
        for v in out:
            f.write(f'{v}\n')
    return

if __name__=="__main__":
    main()


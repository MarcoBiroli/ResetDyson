import numpy as np
import argparse 
from tqdm import tqdm
from sample_RMT import sample_eigvals_large_Gaussian

def sample_dynamic_GOE(N  : int,
                       mu : float,
                       D  : float,
                       t  : float,
                       beta : int):
    if mu != 0:
        var = np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu))
    else:
        var = np.sqrt(2 * D * t)
    #X = GaussianEnsemble(beta=1, n=N, tridiagonal_form=True)
    eigvals = sample_eigvals_large_Gaussian(N, beta, 1, 1)
    #X = var/2 * np.random.normal(size=(N, N))
    #X = X + np.transpose(X)
    return var, eigvals

def sample_reset_GOE(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int) -> np.array:
    tau = np.random.exponential(scale = 1/r)
    return sample_dynamic_GOE(N, mu, D, tau, beta)

def sampling_loop(N, S, r, mu, D, b, **kwargs):
    beta = b
    out = np.empty(shape = (N*S))

    for i in tqdm(range(S)):
        var, eigvals = sample_reset_GOE(r, N, mu, D, beta)
        eigvals = var * eigvals
        out[i*N : (i+1)*N] = eigvals

    if mu != 0:
        out = out * np.sqrt(mu / (N * D))
    else:
        out = out * np.sqrt( r / (4 * N * D) )
    return out

def main():
    parser = argparse.ArgumentParser(prog="Eigenvalue sampling for resetting GOE")
    parser.add_argument("-S", type = int, help="Number of independent samples to draw")
    parser.add_argument("-N", type = int, help="Size of the random matrix")
    parser.add_argument("-r", type = float, help = "Resetting rate")
    parser.add_argument("-mu", type = float, help = "Trapping stiffness")
    parser.add_argument("-D", type = float, help = "Diffusion constant")
    parser.add_argument("-b", type = float, help = "Dyson index")
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    out = sampling_loop(**vars(args)) 

    with open(args.f, "w") as f:
        for v in out:
            f.write(f'{v}\n')
    return

if __name__=="__main__":
    main()


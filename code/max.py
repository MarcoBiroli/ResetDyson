import numpy as np
import argparse 
from tqdm import tqdm
from skrmt.ensemble.gaussian_ensemble import GaussianEnsemble
from sample_RMT import sample_maxeigval_large_Gaussian

def sample_dynamic_Gaussian(N  : int,
                            mu : float,
                            D  : float,
                            t  : float,
                            beta : int, 
                            repeats : int):
    if mu != 0:
        var = np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu)) #/ np.sqrt(2)
    else:
        var = np.sqrt(2 * D * t)

    maxeigval = sample_maxeigval_large_Gaussian(N, beta, 1, repeats)
    maxeigval = maxeigval * var
    return maxeigval
    #beta = 1
    #var = np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu * beta)) / np.sqrt(2)
    #X = GaussianEnsemble(beta=1, n=N, tridiagonal_form=True)
    #return var, X
    #X = var / 2 * np.random.normal(size=(N, N))
    #X = X + np.transpose(X)
    #return X

def sample_reset_Gaussian(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int,
                     repeats : int):
    tau = np.random.exponential(scale = 1/r, size=(repeats,))
    return sample_dynamic_Gaussian(N, mu, D, tau, beta, repeats)

def sampling_loop(S, r, N, mu, D, beta, **kwargs):
    #out = np.empty(shape = (S))

    #for i in tqdm(range(S)):
    #    (var, X) = sample_reset_GOE(r, N, mu, D)
    #    eigvals = var * X.eigvals()
    #    out[i] = max(eigvals)

    out = sample_reset_Gaussian(r, N, mu, D, beta, S)

    #n23 = N**(2/3)
    #xstar = -1.3926626448799095
    if mu != 0:
        c = np.sqrt(N * D / (mu)) #* (2 * np.sqrt(2) * n23 + xstar) / (2 * n23)
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


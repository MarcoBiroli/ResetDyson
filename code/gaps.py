import numpy as np
import argparse 
import scipy.special
from sample_RMT import sample_gap_large_Gaussian, sample_gap_small_Gaussian
import scipy

def sample_dynamic_Gaussian_unormalized(N  : int,
                            mu : float,
                            D  : float,
                            t  : float,
                            beta : int, 
                            repeats : int):
    
    if N > 100:
        ndiff = N-1
        if mu != 0:
            var = np.repeat(np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu)) , ndiff)
        else:
            var = np.repeat(np.sqrt(2 * D * t) , ndiff)
        gap = sample_gap_large_Gaussian(N, beta, 1, repeats)
        gap = gap * var
        return gap
    else:
        ndiff = N-1
        if mu != 0:
            var = np.repeat(np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu)) , ndiff)
        else:
            var = np.repeat(np.sqrt(2 * D * t) , ndiff)
        gap = sample_gap_small_Gaussian(N, beta, 1, repeats)
        gap = gap * var
        return gap

def sample_reset_Gaussian_unormalized(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int,
                     repeats : int):
    tau = np.random.exponential(scale = 1/r, size=(repeats,))
    return sample_dynamic_Gaussian_unormalized(N, mu, D, tau, beta, repeats)

def sample_dynamic_Gaussian(N  : int,
                            mu : float,
                            D  : float,
                            t  : float,
                            beta : int, 
                            repeats : int):
    
    if N > 100:
        ndiff = N-1
        if mu != 0:
            var = np.repeat(np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu * beta)) , ndiff)
        else:
            var = np.repeat(np.sqrt(2 * D * t) , ndiff)
        gap = sample_gap_large_Gaussian(N, beta, 1, repeats)
        gap = gap * var
        return gap / np.mean(gap)
    else:
        ndiff = N-1
        if mu != 0:
            var = np.repeat(np.sqrt(D * (1 - np.exp(-2 * mu * t))/(mu * beta)) , ndiff)
        else:
            var = np.repeat(np.sqrt(2 * D * t / beta) , ndiff)
        gap = sample_gap_small_Gaussian(N, beta, 1, repeats)
        gap = gap * var
        return gap / np.mean(gap)

def sample_reset_Gaussian(r  : float,
                     N  : int,
                     mu : float,
                     D  : float,
                     beta : int,
                     repeats : int):
    tau = np.random.exponential(scale = 1/r, size=(repeats,))
    return sample_dynamic_Gaussian(N, mu, D, tau, beta, repeats)

def sampling_loop(S, r, N, mu, D, beta, **kwargs):

    if r != 0:
        out = sample_reset_Gaussian(r, N, mu, D, beta, S)
        out = out / np.mean(out)

        if mu != 0:
            gamma = mu / r
            c = np.sqrt(np.pi) * scipy.special.gamma(1 + beta/2) * scipy.special.gamma(1 + 1/(2*gamma)) / ( scipy.special.gamma((1 + beta)/2) * scipy.special.gamma( 3/2 + 1/(2*gamma) ) ) 
        else:
            c = np.pi / 2

        out = out * c
    else:
        raise RuntimeError("Outdated code, now not supported")

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


import numpy as np
import scipy
import matplotlib.pyplot as plt
from tqdm import tqdm
from dppy.beta_ensembles import HermiteEnsemble

def sample_large_Gaussian(n, beta):
    cutoff = int(10 * n**(1/3))
    upper_diag = np.sqrt(np.arange(n-1, n+1-cutoff, -1))/2/np.sqrt(n)
    diag = np.random.normal(size=(cutoff)) / np.sqrt(n*beta)
    return upper_diag, diag

def sample_maxeigval_large_Gaussian(n, beta, sigma, repeats):
    cutoff = int(10 * n**(1/3))
    upper_diag = np.sqrt(np.arange(n-1, n-cutoff, -1))/2/np.sqrt(n)

    res = np.empty((repeats,))

    for i in tqdm(range(repeats), leave = False):
        diag = np.random.normal(size=(cutoff)) / np.sqrt(n*beta)
        maxeigval = scipy.linalg.eigh_tridiagonal(diag, upper_diag, eigvals_only = True, select = 'i', select_range = (cutoff-1, cutoff-1))
        res[i] = maxeigval

    res = sigma * (np.sqrt(2 * n) + (res-1) * (2 * n**(2/3)))

    return res

def sample_gap_large_Gaussian(n, beta, sigma, repeats):
    cutoff = n
    upper_diag = np.sqrt(np.arange(n-1, n-cutoff, -1))/2/np.sqrt(n)

    ndiff = n-1

    res = np.empty((repeats * ndiff,))

    for i in tqdm(range(repeats), leave = False):
        diag = np.random.normal(size=(cutoff)) / np.sqrt(n*beta)
        eigvals = scipy.linalg.eigh_tridiagonal(diag, upper_diag, eigvals_only = True)
        eigvals = np.sqrt(2 * n) * eigvals
        eigvals.sort()
        #gaps = np.triu(np.abs(eigvals - eigvals[:, None]))
        #gaps = gaps[gaps != 0]
        gaps = np.diff(eigvals)
        res[i*ndiff:(i+1)*ndiff] = gaps

    res = sigma * res

    return res

def sample_gap_small_Gaussian(n, beta, sigma, repeats):
    '''
    #upper_diag = np.sqrt(np.arange(n-1, n-cutoff, -1))/2/np.sqrt(n)
    upper_diag = np.sqrt( np.random.chisquare(df = np.arange(n-1, 0, -1) * beta) / (2*n))

    ndiff = n-1

    res = np.empty((repeats * ndiff,))

    for i in tqdm(range(repeats), leave = False):
        diag = np.random.normal(size=(n)) / np.sqrt(n * beta)
        eigvals = scipy.linalg.eigh_tridiagonal(diag, upper_diag, eigvals_only = True)
        eigvals = np.sqrt(2 * n) * eigvals
        eigvals.sort()
        #gaps = np.triu(np.abs(eigvals - eigvals[:, None]))
        #gaps = gaps[gaps != 0]
        gaps = np.diff(eigvals)
        res[i*ndiff:(i+1)*ndiff] = gaps

    res = sigma * res
    '''
    ndiff = n-1
    res = np.empty((repeats * ndiff,))

    for i in tqdm(range(repeats), leave = False): 
        hermite = HermiteEnsemble(beta=beta)
        eigvals = hermite.sample_banded_model(loc=0.0, scale = 1.0, size_N=n)
        eigvals.sort()
        gaps = np.diff(eigvals)
        res[i*ndiff:(i+1)*ndiff] = gaps

    return sigma * res

def sample_eigvals_large_Gaussian(n, beta, sigma, repeats):
    cutoff = n
    upper_diag = np.sqrt(np.arange(n-1, n-cutoff, -1))/2/np.sqrt(n)

    res = np.empty((repeats, n))

    for i in tqdm(range(repeats), leave = False):
        diag = np.random.normal(size=(cutoff)) / np.sqrt(n*beta)
        eigvals = scipy.linalg.eigh_tridiagonal(diag, upper_diag, eigvals_only = True)
        eigvals = np.sqrt(2 * n) * eigvals
        res[i, :] = eigvals

    res = sigma * res

    return res

if __name__ == "__main__":
    res = sample_maxeigval_large_Gaussian(int(1e9), 2, 1, int(1e3))
    print(res[:20])
    plt.hist(res, bins = 'auto')
    plt.show()

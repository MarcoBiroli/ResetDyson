import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.special import erfc

def sample_reset(N, r, D):
    if r != 0:
        t = np.random.exponential(scale = 1/r, size = 1)
        out = np.random.normal(size = (N, N)) / np.sqrt(2)
        out = np.sqrt(2 * D * t) * out
    else:
        out = np.random.normal(size = (N, N)) / np.sqrt(2)
    out = np.triu(out)
    out = out + np.transpose(out)
    return out

N = 100
r = 1.24951
#r = 0
D = 2.4581

repeats = 10000

out = np.empty(repeats * N)

for i in tqdm(range(repeats)):
    H = sample_reset(N, r, D).reshape(N, N)
    eig = np.linalg.eigvals(H)
    out[i*N:(i+1)*N] = eig

if r == 0:
    scale = 1/np.sqrt(N)
else:
    scale = np.sqrt(r/(4 * D * N))

def f(z):
    if r != 0:
        return 2 * np.exp(-z**2)/np.sqrt(np.pi) - 2 * np.abs(z) * erfc(np.abs(z))
    else:
        return 1 / (np.pi) * np.sqrt(2 - z**2)

out = out * scale

ztab = np.linspace(-3, 3, 1000)

plt.hist(out, density = True, bins = 'auto')
plt.plot(ztab, f(ztab))

plt.show()
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from tqdm import tqdm

def E(mu, D, x):
    return (-mu * x + D * (1 / ((x[:, None] - x[None, :]) + np.eye(len(x))) - np.eye(len(x))).sum(axis = 1))

def step(mu, D, beta, x, dt):
    return x + dt * (-mu * x + \
                     D * (1 / ((x[:, None] - x[None, :] + 1e-4) + np.eye(len(x))) - np.eye(len(x))).sum(axis = 1) + \
                         np.sqrt(2 * D / (beta * dt)) * np.random.randn(len(x)))


N = 2
T = 0.1
D = 1
beta = 4
mu = 1
dt = 1e-4
dtfactor = 1e-2
mindt = 1e-6
eps = 1e-5

repeats = 500
samples = []

for _ in tqdm(range(repeats)):
    t = 0
    x = np.random.randn(N) * eps
    final = False
    while t < T:
        dt = max(min(dtfactor * (np.abs(x[:, None] - x[None, :] + np.eye(N))**2).min(), dt), mindt)
        if t + dt > T:
            dt = T - t
            final = True
        x = step(mu, D, beta, x, dt)
        t += dt
        if final:
            break
    samples.append(deepcopy(x))

samples = np.stack(samples)

xedges = np.linspace(-2, 2, 10)
yedges = np.linspace(-2, 2, 10)

H, xedges, yedges = np.histogram2d(samples[:, 0], samples[:, 1], 
                                   bins=(xedges, yedges),
                                   density = True)
H = H.T

fig, ax = plt.subplots()
X, Y = np.meshgrid(xedges, yedges)
ax.pcolormesh(X, Y, H)

'''
from matplotlib.image import NonUniformImage

im = NonUniformImage(ax, interpolation='bilinear')
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
im.set_data(xcenters, ycenters, H)
ax.add_image(im)'
'''

plt.show()

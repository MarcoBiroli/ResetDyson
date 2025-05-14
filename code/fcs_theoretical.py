import numpy as np
from TracyWidom import TracyWidom
import scipy
import argparse
from mpmath import *

def free_mean(l, u):
    adim = l/u
    if np.any(adim < 0) or np.any(adim > np.sqrt(2)):
        raise RuntimeError('Out of range.')
    return 1/np.pi * adim * np.sqrt(2 - adim**2) + 2 /np.pi * np.arctan(adim/np.sqrt(2 - adim**2))
    return 1/np.pi * l / u * np.sqrt(2 - l**2/u**2) + 2 /np.pi * np.arctan((l/u)/(2 - l**2/u**2)**(1/2))
    adim = l/np.sqrt(u)
    return 1/np.pi * adim * np.sqrt(2 - adim**2) + 2 /np.pi * np.arctan(adim/np.sqrt(2 - adim**2))

def free_mean_v(l, v, gamma):
    return free_mean(l, np.sqrt(1 - v**(2*gamma)))

def rec_v(low, high, target, l, gamma, eps = 1e-6):
    mid = (low+high)/2
    val = free_mean_v(l, mid, gamma)
    if np.abs(val - target) < eps:
        return mid
    elif val > target:
        return rec_v(low, mid, target, l, gamma, eps)
    elif val < target:
        return rec_v(mid, high, target, l, gamma, eps)
    else:
        raise RuntimeError('Recursion Error.')

def vstar(z, l, gamma):
    # v \in [0, (1 - l**2/2)**(1/(2 * gamma))]
    low = 0
    high = (1 - l**2/2)**(1/(2 * gamma))
    return rec_v(low, high, z, l, gamma)

def delta_th_f(ztab, l, gamma):
    out = []
    for z in ztab:
        cur = 0
        if z > free_mean(l, 1) and z < free_mean(l, l/np.sqrt(2) + 1e-9):
            v = vstar(z, l, gamma)
            #breakpoint()
            u = 1 - v**(2 * gamma)
            cur += np.pi/(2 * gamma * l) * v**(1-2*gamma) * u**2 / np.sqrt(2 * u - l**2 )
        if z == 1:
            cur += (1 - (1 - l**2/2)**(1/(2 * gamma)))
        if cur == 0:
            cur = np.nan
        out.append(cur)
    return out

def right_asymp(z, l, gamma):
    if gamma != 0:
        return np.pi**(2/3)/(4 * 6**(1/3) * gamma) * l**2 * (1 - l**2/2)**(1/(2*gamma) - 1) * (1/(1 - z))**(1/3)
    else:
        y = l
        return np.pi**(2/3) * y / (4 * 6**(1/3)) * np.exp(-y/4) * (1 - z)**(-1/3)

def left_asymp(z, l, gamma):
    if gamma != 0:
        zmin = 1/np.pi * l*np.sqrt(2 - l**2) + 2/np.pi * np.arctan(l/np.sqrt(2 - l**2))
        return 1/(2*gamma) * (np.pi / (l * np.sqrt(2 - l**2)))**(1/(2*gamma)) * (z - zmin)**(1/(2*gamma) - 1)
    else:
        y = l
        return 8 * y / (np.pi**2 * z**3) * np.exp(- 4 * y / (np.pi**2 * z**2))


def free_mean_logv_free(logv, y):
    return (1/(2 * np.pi * logv) * np.sqrt(y * (4 * logv - y)) + \
            2/np.pi * np.arctan(1/np.sqrt(4 * logv/y - 1)))

def rec_logv_free(low, high, target, y, eps = 1e-6):
    mid = (low+high)/2
    val = free_mean_logv_free(mid, y)
    if np.abs(val - target) < eps:
        return mid
    elif val < target:
        return rec_logv_free(low, mid, target, y, eps)
    elif val > target:
        return rec_logv_free(mid, high, target, y, eps)
    else:
        raise RuntimeError('Recursion Error.')

def vstar_free(z, y):
    # v \in [0, (1 - l**2/2)**(1/(2 * gamma))]
    low = 0
    high = np.exp(-y/4)
    loglow = y/4
    loghigh = 1e20
    return np.exp(-rec_logv_free(loglow, loghigh, z, y))

def q(ztab, y):
    out = []
    for z in ztab:
        cur = 0
        v = vstar_free(z, y)
        cur += 2 * np.pi * v * np.log(v)**2 / np.sqrt( y * (4 * np.log(1/v) - y) )
        if z == 1:
            cur += (1 - np.exp(-y/4))
        out.append(cur)
    return out

def main():
    parser = argparse.ArgumentParser(prog="FCS for resetting GOE")
    parser.add_argument("-g", type = float, help = 'Dimensionless parameter')
    parser.add_argument("-l", type = float, help = "Dimensionless FCS bound.")
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    ztab = np.linspace(0, 1, 10000)

    if args.g != 0:
        res = np.array(delta_th_f(ztab, args.l, args.g))
    else:
        res = np.array(q(ztab, args.l))

    left = left_asymp(ztab, args.l, args.g)
    right = right_asymp(ztab, args.l, args.g)

    dz = ztab[1] - ztab[0]
    print(np.sum(res[~np.isnan(res)]) * dz)
    
    with open(args.f, 'w') as f:
        for z, v in zip(ztab, res):
            f.write(f'{z} {v}\n')

    left_filename = '.'.join(args.f.split('.')[:-1] + ['left', 'out'])
    right_filename = '.'.join(args.f.split('.')[:-1] + ['right', 'out'])

    with open(left_filename, 'w') as f:
        for z, v in zip(ztab, left):
            f.write(f'{z} {v}\n')

    with open(right_filename, 'w') as f:
        for z, v in zip(ztab, right):
            f.write(f'{z} {v}\n')

if __name__ == "__main__":
    main()


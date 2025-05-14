import numpy as np
import scipy.special
from TracyWidom import TracyWidom
import scipy
import argparse
from mpmath import *

def delta_th_f(ztab, gamma):
    return [z * scipy.special.gamma(1 + 1/(2*gamma))/2 * meijerg([[], [1/(2*gamma)]], [[0, 0], []], z**2/4) for z in ztab]
    #return ztab/4 * np.exp(-ztab**2/8) * scipy.special.kn(0, ztab**2/8)

def th_f0(y):
    return y * scipy.special.k0(y)

def reghyp1f1(a, b, z):
    return scipy.special.hyp1f1(a, b, z) / scipy.special.gamma(b)

def th_h(z, gamma, beta):
    return np.pi / (np.cos( np.pi * beta / 2 ) * 4 * gamma * scipy.special.gamma((1 + beta)/2)) * (\
        2**(1-beta) * z**beta * scipy.special.gamma(1/(2*gamma)) / scipy.special.gamma( ( 1 - (beta - 1)*gamma )/(2 * gamma) ) * \
        reghyp1f1( ( (1 + beta) * gamma - 1 ) / (2 * gamma), (1 + beta)/2, - z**2/4 ) - \
        z * reghyp1f1( 1 - 1/(2*gamma), (3 - beta)/2, - z**2/4)
        )

def th_h0(y, beta):
    return y**((1 + beta)/2) / ( 2**((beta - 1)/2) * scipy.special.gamma( (1 + beta)/2 ) ) * scipy.special.kn( (beta - 1)/2, y )

def main():
    parser = argparse.ArgumentParser(prog="Max for resetting GOE")
    parser.add_argument("-g", type = float, help = 'Dimensionless parameter')
    parser.add_argument("-b", type = float, help = "Dyson's index")
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    ztab = np.linspace(0, 10, 1000)

    if args.b == 1:
        if args.g != 0:
            res = delta_th_f(ztab, args.g)
        else:
            res = th_f0(ztab)
    else:
        if args.g != 0:
            res = th_h(ztab, args.g, args.b)
        else:
            res = th_h0(ztab, args.b)
    
    with open(args.f, 'w') as f:
        for z, v in zip(ztab, res):
            f.write(f'{z} {v}\n')

if __name__ == "__main__":
    main()


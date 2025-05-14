import numpy as np
import scipy.special
from TracyWidom import TracyWidom
import scipy
import argparse
import matplotlib.pyplot as plt

def th_f(z, gamma):
    return (1/np.pi * np.sqrt(2 - z**2) * np.pi**(1/2) / (2 ** (2 + 1/(2 * gamma)) * gamma )  \
            * scipy.special.gamma(1/(2*gamma)) / scipy.special.gamma( 1/2 * (3 + 1/gamma) )  \
            * (2 - z**2)**(1/(2*gamma)) * scipy.special.hyp2f1(1, 1/(2 * gamma), 1/2 * (3 + 1/gamma), 1 - z**2/2) )
    
def th_f0(y):
    return 2 * np.exp(-y**2) / np.sqrt(np.pi) - 2 * np.abs(y) * scipy.special.erfc(np.abs(y))

def main():
    parser = argparse.ArgumentParser(prog="Max for resetting GOE")
    parser.add_argument("-g", type = float, help = 'Dimensionless parameter')
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()


    if args.g != 0:
        ztab = np.linspace(-np.sqrt(2), np.sqrt(2), 101)
        res = th_f(ztab, args.g)
    else:
        ztab = np.linspace(-5, 5, 101)
        res = th_f0(ztab)

    with open(args.f, 'w') as f:
        for z, v in zip(ztab, res):
            f.write(f'{z} {v}\n')

if __name__ == "__main__":
    main()


import numpy as np
from TracyWidom import TracyWidom
import scipy
import argparse
import matplotlib.pyplot as plt

def th_f(ztab, gamma):
    return ztab * (1 - ztab**2 / 2)**(1/(2 * gamma) - 1) / (2 * gamma)

def th_f0(y):
    return y * np.exp(-y**2 / 2)

def main():
    parser = argparse.ArgumentParser(prog="Max for resetting GOE")
    parser.add_argument("-g", type = float, help = 'Dimensionless parameter')
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    if args.g != 0:
        ztab = np.linspace(0, np.sqrt(2), 1000)
        res = th_f(ztab, args.g)
    else:
        ztab = np.linspace(0, 10, 1000)
        res = th_f0(ztab)
    
    with open(args.f, 'w') as f:
        for z, v in zip(ztab, res):
            f.write(f'{z} {v}\n')

if __name__ == "__main__":
    main()


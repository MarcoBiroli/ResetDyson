import numpy as np
import scipy.integrate
import scipy
import argparse
from mpmath import *
from tqdm import tqdm

def f(ell, gamma, v):
    a = ell / np.sqrt(1 - v**(2*gamma))
    out = 1/np.pi * a * np.sqrt(2 - a**2) + 2/np.pi * np.arctan( a / np.sqrt(2 - a**2) )
    if np.isnan(out):
        return 0.0
    else:
        return out

def th_var(ell, gamma):
    top = (1 - ell**2/2)**(1/(2*gamma)) - 1e-4
    return (
        scipy.integrate.quad(
            lambda v : f(ell, gamma, v)**2,
            0,
            top
        )[0] + (1 - (1 - ell**2/2)**(1/(2*gamma))) - \
        (
            scipy.integrate.quad(
                lambda v : f(ell, gamma, v),
                0,
                top
            )[0] + (1 - (1 - ell**2/2)**(1/(2*gamma)))
        )**2
    )

def f0(y, v):
    invlogv = np.log(1/v)
    return ( 
        1/(2 * np.pi * invlogv) * np.sqrt( y * ( 4 * invlogv - y ) ) + \
        2 / np.pi * np.arctan(1 / np.sqrt( 4 * invlogv / y - 1 ))
     )

def th_var0(y):
    top = np.exp(-y/4) - 1e-6
    return (
        scipy.integrate.quad(
            lambda v : f0(y, v)**2,
            0,
            top
        )[0] + (1 - top) - \
        (
            scipy.integrate.quad(
                lambda v : f0(y, v),
                0,
                top
            )[0] + (1 - top)
        )**2
    )

def main():
    parser = argparse.ArgumentParser(prog="FCS for resetting GOE")
    parser.add_argument("-g", type = float, help = 'Dimensionless parameter')
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    if args.g != 0:
        elltab = np.linspace(0, np.sqrt(2), 100)
        vartab = [th_var(ell, args.g) for ell in tqdm(elltab)]
        x = elltab
        y = vartab
    else:
        ytab = np.linspace(0, 10, 100)
        vartab = [th_var0(y) for y in tqdm(ytab)]
        x = ytab
        y = vartab

    with open(args.f, 'w') as f:
        for z, v in zip(x, y):
            f.write(f'{z} {v}\n')
    

if __name__ == "__main__":
    main()


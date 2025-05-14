import numpy as np
import argparse
from mpmath import *
from tqdm import tqdm

def th_var(ell):
    return np.log(1e4*ell * (2 - ell**2)**(2/3))

def main():
    parser = argparse.ArgumentParser(prog="FCS for resetting GOE")
    parser.add_argument("-f", type = str, help = 'Output filename')
    args = parser.parse_args()

    elltab = np.linspace(0, np.sqrt(2)-1e-6, 100000)

    vartab = [th_var(ell) for ell in tqdm(elltab)]

    with open(args.f, 'w') as f:
        for z, v in zip(elltab, vartab):
            f.write(f'{z} {v}\n')

        f.write(f'{np.sqrt(2)} {-10}')
    

if __name__ == "__main__":
    main()


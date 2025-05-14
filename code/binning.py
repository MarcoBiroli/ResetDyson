import numpy as np
import argparse

def parse(line):
    return float(line.strip())

def binning(i, o, b, **kwargs):
    vals = []
    with open(i, 'r') as f:
        for line in f:
            vals.append(parse(line))
    
    vals = np.array(vals)

    bins, bin_edges = np.histogram(vals, density=True, bins = b)
    bin_centers = (bin_edges[1:] + bin_edges[:-1])/2

    with open(o, 'w') as f:
        for c, v in zip(bin_centers, bins):
            f.write(f'{c} {v}\n')

    return

def main():
    parser = argparse.ArgumentParser(prog="Binner")
    parser.add_argument("-i", type = str, help = 'Input filename')
    parser.add_argument("-o", type = str, help = 'Output filename')
    parser.add_argument("-b", type = str, help = 'Binning')
    args = parser.parse_args()

    if args.b != 'auto':
        args.b = int(args.b)

    binning(**vars(args))
    return

if __name__=="__main__":
    main()
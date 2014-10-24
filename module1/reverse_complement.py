import sys


if __name__ == '__main__':
    comp = {
        'A' : 'T',
        'C' : 'G',
        'G' : 'C',
        'T' : 'A',
    }
    symbols = sys.argv[1]
    complement = ''
    for s in symbols:
        complement += comp[s]
    # reverse it
    complement = complement[::-1]
    print complement

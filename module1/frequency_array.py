import timeit

letter_to_idx = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}

idx_to_letter = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T',
}

N=4

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def pattern_to_number2(pattern):
    if len(pattern) < 1: return 0
    return (N * pattern_to_number2(pattern[0:-1])) + letter_to_idx[pattern[-1]]

def pattern_to_number(pattern):
    idx_cum = 0
    for i, l in enumerate(pattern):
        weight = letter_to_idx[l]
        # Model it as an n-dimensional array, where the 'width' of each dimension
        # is the number of possible values for a character: 4
        idx = (weight * (N**(len(pattern) - (i+1))))
        idx_cum += idx
    return idx_cum

def number_to_pattern2(num, k):
    if k == 1: return idx_to_letter[num]
    prefix_index = num / N
    r = num % N
    prefix_pattern = number_to_pattern2(prefix_index, k - 1)
    symbol = idx_to_letter[r]
    return prefix_pattern + symbol

def number_to_pattern(num, k):
    if num >= N**k: return None
    kmer = ''
    for i in range(0, k):
        div = (N**(k-(i+1)))
        letter_idx = num / div
        kmer += idx_to_letter[letter_idx]
        num -= (letter_idx * div)
    return kmer

#wrapped = wrapper(pattern_to_number, 'ACGCCCTGAGCACCCA')

#for i in range(0, 256):
#    print number_to_pattern(i, 4)
#    print number_to_pattern2(i, 4)
#    print

print number_to_pattern2(7727, 10)


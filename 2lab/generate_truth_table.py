from itertools import product

def generate_combinations(length):
    combs = product([0, 1], repeat=length)
    return [list(comb) for comb in combs]
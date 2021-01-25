from itertools import combinations


def sum_pairs(ints, s):
    for i, j in sorted(combinations(list(range(len(ints))), 2), key=lambda x: x[1]):
        if ints[i] + ints[j] == s:
            return [ints[i], ints[j]]
    return None

from fractions import gcd
import math
import functools


def convertFracts(lst):
    def lcm(a, b): return abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x: x[1], list(lst)))
    lcm_num = functools.reduce(lcm, tmp_list)
    return list(map(lambda x: [x[0] * lcm_num // x[1], lcm_num], list(lst)))


def convertFracts(lst):
    D = 1
    for _, d in lst:
        D *= d//gcd(d, D)
    return [[D*n//d, D] for n, d in lst]

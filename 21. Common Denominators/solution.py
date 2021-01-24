from math import gcd


def convertFracts(lst):
    def lcd(a, b): return abs(a*b)//gcd(a, b)
    if len(lst) <= 1:
        return lst
    d = lcd(lst[0][1], lst[1][1])
    for i in range(2, len(lst)):
        d = lcd(lst[i][1], d)
    return [[a*d//b, d] for a, b in lst]

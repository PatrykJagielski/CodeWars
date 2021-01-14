def find_nb(m):
    n = 0
    x = 1
    while m > 0:
        m -= x**3
        n += 1
        x += 1
    return n if m == 0 else -1

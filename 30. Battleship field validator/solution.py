import numpy as np

def validate_battlefield(field):
    arr = np.array(field)

    def neighbors(x, y, arr, size = 1):
        arr_copy = arr.copy()
        for x in range(x, x+size):
            if x > 9:
                return False
            if arr[x][y] == 1:
                arr_copy[x][y] = 10 * size
        slx, suy = size - 1, 1
        if x == 0: slx = 0
        if y == 0: suy = 0
        x0 = x - slx - 1
        y0 = y - suy
        if x0 < 0: x0 = 0
        if y0 < 0: y0 = 9
        return arr_copy[x0:x+2,y0:y+2]

    def n_ships(arr, size=1):
        c = 0
        for x in range(arr.shape[0]):
            for y in range(arr.shape[1]):
                sum_n = neighbors(x, y, arr, size=size)
                if not isinstance(sum_n, bool) and sum_n.sum() == 10 * size * size:
                    c += 1
        return c

    if n_ships(arr) == 4 and n_ships(arr, size=2) + n_ships(np.rot90(arr), size=2) == 3 and \
        n_ships(arr, size=3) + n_ships(np.rot90(arr), size=3) == 2 and \
        n_ships(arr, size=4) + n_ships(np.rot90(arr), size=4) == 1:
        return True
    return False
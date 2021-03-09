import numpy as np


def valid_solution(board):
    for vertical in board:
        if len(set(vertical)) != 9:
            return False

    for horizontal in np.rot90(board, k=1, axes=(1, 0)):
        if len(set(horizontal)) != 9:
            return False

    arr = np.array(board)

    for i_start, i_stop in [(0, 3), (3, 6), (6, 9)]:
        for j_start, j_stop in [(0, 3), (3, 6), (6, 9)]:
            if len(np.unique(arr[i_start:i_stop, j_start:j_stop])) != 9:
                return False

    return True

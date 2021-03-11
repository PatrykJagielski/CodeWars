def spiralize(size):
    # Make a snake
    spiral = [[1 - min(i, j, size-max(i, j)-1) %
               2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size/2-(size % 4 == 0)):
        spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral

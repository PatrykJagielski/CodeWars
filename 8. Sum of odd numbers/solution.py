def row_sum_odd_numbers(n):
    odd = 1
    triangle = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            temp.append(odd)
            odd += 2
        triangle.append(temp)
    return sum(triangle[-1])

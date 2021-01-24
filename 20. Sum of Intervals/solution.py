def sum_of_intervals(intervals):
    l = [list(range(x[0], x[1])) for x in intervals]
    results = []
    for i in l:
        results += i
    return len(set(results))

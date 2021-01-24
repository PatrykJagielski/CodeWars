def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)

    return len(result)


def sum_of_intervals(intervals):
    return len(set([i for a, b in intervals for i in range(a, b)]))


def sum_of_intervals(intervals):
    return len(set.union(*(set(range(*i))for i in intervals)))

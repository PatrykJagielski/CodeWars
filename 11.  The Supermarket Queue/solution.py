def queue_time(customers, n):
    customers.reverse()
    q = [0]*n
    while customers:
        q[q.index(min(q))] += customers.pop()
    return max(q)

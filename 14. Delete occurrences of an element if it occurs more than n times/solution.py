from collections import Counter


def delete_nth(order, max_e):
    order.reverse()
    c = Counter(order)

    for k, v in c.items():
        if v > max_e:
            for _ in range(v - max_e):
                order.remove(k)

    return list(reversed(order))

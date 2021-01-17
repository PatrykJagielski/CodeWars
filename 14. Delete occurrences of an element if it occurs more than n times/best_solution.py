def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans


def delete_nth(order, max_e):
    return [o for i, o in enumerate(order) if order[:i].count(o) < max_e]

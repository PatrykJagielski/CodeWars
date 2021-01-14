def find_outlier(integers):
    odd = 0
    even = 0
    for sample in integers[:3]:
        if sample % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd > even:
        for i in integers:
            if i % 2 == 0:
                return i
    else:
        for i in integers:
            if i % 2 == 1:
                return i

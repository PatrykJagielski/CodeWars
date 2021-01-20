from collections import Counter


def find_uniq(arr):
    m = None
    for i in range(3):
        if arr[:3].count(arr[i]) > 1:
            m = arr[i]
    for i in range(len(arr)):
        if arr[i] != m:
            return arr[i]


def find_uniq(a):
    return Counter(a).most_common()[-1][0]

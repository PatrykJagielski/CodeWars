def find_even_index(arr):
    left = 0
    for i in range(len(arr)):
        left += arr[i]
        right = 0
        for j in range(i, len(arr)):
            right += arr[j]
        if right == left:
            return i
    return -1

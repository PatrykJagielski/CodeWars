def snail(array):
    result = []
    while array:
        result.extend(array.pop(0))
        if array:
            for i in array:
                result.append(i.pop(-1))
        if array:
            result.extend(reversed(array.pop(-1)))
        result.extend(reversed([i.pop(0) for i in array]))
    return result
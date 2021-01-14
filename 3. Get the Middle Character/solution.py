def get_middle(s):
    l = len(s)
    if len(s) % 2 == 0:
        return s[int(l/2)-1] + s[int(l/2)]
    return s[int(l/2)]

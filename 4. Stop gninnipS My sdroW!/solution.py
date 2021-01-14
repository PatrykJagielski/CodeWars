def spin_words(s):
    return ' '.join(list(map(lambda x: x[::-1] if len(x) >=5 else x, s.split())))

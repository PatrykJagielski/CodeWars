def longest(s1, s2):
    s3 = s1 + s2
    chars = [char for char in s3]
    uniq_chars = set(chars)
    uniq_chars = list(uniq_chars)
    uniq_chars.sort()
    return ''.join(uniq_chars)

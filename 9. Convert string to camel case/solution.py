def to_camel_case(text):
    if len(text) == 0:
        return ''
    t = [x.capitalize() for x in text.replace(
        '-', ' ').replace('_', ' ').split()[1:]]
    return text.replace('-', ' ').replace('_', ' ').split()[0] + ''.join(t)

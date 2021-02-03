from re import sub


def simplify(poly):
    if not poly.startswith('-'):
        poly = '+' + poly
    t = sub(r'(.)([+-])', r'\1,\2', poly).split(',')

    s = {}
    for i in t:
        var = ''.join(sorted(sub('[0-9+-]', '', i)))
        val = sub('[a-z]', '', i)
        if s.get(var):
            s[var].append(val)
        else:
            s[var] = [val]

    r = {}
    for k, v in s.items():
        r[k] = 0
        for i in v:
            if i == '+':
                r[k] += 1
            elif i == '-':
                r[k] -= 1
            else:
                r[k] += int(i)
    r = dict(sorted(r.items(), key=lambda x: (len(x[0]), x[0])))
    r = {key: val for key, val in r.items() if val != 0}

    result = ''.join([str(v)+k if v < 0 else '+'+str(v) +
                      k for k, v in r.items()]).replace('1', '')

    return result[1:] if result.startswith('+') else result

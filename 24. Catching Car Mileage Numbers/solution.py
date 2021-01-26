import re


def is_interesting(number, awesome_phrases, c=True):
    if number in awesome_phrases:
        return 2

    if number in [98, 99]:
        return 1

    if number < 100:
        return 0

    if re.fullmatch(r'[123456789]00+', str(number)):
        return 2

    if re.fullmatch(r'1+|2+|3+|4+|5+|6+|7+|8+|9+', str(number)):
        return 2

    inc = True
    for i in range(len(str(number)) - 1):
        if int(str(number)[i]) != (int(str(number)[i+1]) - 1) % 10:
            inc = False
            break
    if inc:
        return 2

    dec = True
    for i in range(len(str(number)) - 1):
        if int(str(number)[i]) - 1 != (int(str(number)[i+1])) % 10:
            dec = False
            break
    if dec:
        return 2

    if str(number) == str(number)[::-1]:
        return 2

    if c and (is_interesting(number + 1, awesome_phrases, c=False) == 2 or is_interesting(number + 2, awesome_phrases, c=False) == 2):
        return 1

    return 0

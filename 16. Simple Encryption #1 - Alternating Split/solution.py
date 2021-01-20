def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    text = ''.join([a + b for a, b in list(zip(encrypted_text[int(
        len(encrypted_text)/2):], encrypted_text[:int(len(encrypted_text)/2)]))])
    if len(encrypted_text) % 2 == 1:
        text += encrypted_text[-1]
    return decrypt(text, n - 1)


def encrypt(text, n):
    while n > 0:
        text = ''.join([x[1] for x in sorted(
            [i for i in enumerate(text)], key=lambda x: 1 - x[0] % 2)])
        n -= 1
    return text

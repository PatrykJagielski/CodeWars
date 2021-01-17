def tribonacci(signature, n):
    for i in range(n - 3):
        signature.append(sum(res[-3:]))
    return signature[:n]

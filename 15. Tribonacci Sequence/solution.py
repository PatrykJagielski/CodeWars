def tribonacci(signature, n):
    while n > len(signature):
        signature.append(sum(signature[-3:]))
    return signature[:n]

def odd(n: int):
    odd = []
    for i in range(n):
        if i % 2 == 1:
            odd.append(i)
    return odd

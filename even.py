def even(n: int):
    even = []
    for i in range(n):
        if i % 2 == 0:
            even.append(i)
    return even

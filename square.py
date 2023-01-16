def square(n: int):
    square = []
    for i in range(n):
        if i*i < n:
            square.append(i*i)
    return square

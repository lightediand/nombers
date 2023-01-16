def fib(n: int):
    fib=[]
    fib.append(0)
    fib.append(1)
    i = 0
    j = 1
    while i+j < n:
        z = i+j
        fib.append(z)
        i = j
        j = z
    return fib

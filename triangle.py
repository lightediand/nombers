def tri(n: int):
    tri = []
    for i in range(n):
        triangle = (i*(i+1))//2
        if triangle < n:
            tri.append(triangle)
    return tri

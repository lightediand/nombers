from odd import odd 

def ppt(n: int):
    o = odd(n)
    pairs = []
    ppt = []
    for j in o:
        for k in o:
            if k != j and k > j:
                pairs.append((k, j))
    for x in pairs:
        a = x[0]*x[1]
        b = (x[0]**2 - x[1]**2)//2
        c = (x[0]**2 + x[1]**2)//2
        ppt.append((a, b, c))
    return ppt

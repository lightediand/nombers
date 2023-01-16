def happy(n: int):
    happy_nums = []
    for x in range(n):
        if x==1:
            happy_nums.append(x)
        else:
            init_val = x
            if x > 9:
                while x > 9:
                    beep = []
                    for i in range(len(str(x))):
                        y=str(x)
                        a=int(y[i])
                        beep.append(a**2)
                    b=sum(beep)
                    x=b
                if x!=1:
                    pass
                else:
                    happy_nums.append(init_val)
            else:
                init_val = x
                b=x**2
                while b > 9:
                    boop = []
                    for i in range(len(str(b))):
                        y=str(b)
                        a=int(y[i])
                        boop.append(a**2)
                    c=sum(boop)
                    b=c
                if b!=1:
                    pass
                else:
                    happy_nums.append(init_val)
                
    return happy_nums

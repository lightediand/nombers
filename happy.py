def happy(n: int):
    happy_nums = []
    for x in range(n):
        if x==1:
            happy_nums.append(x)
        elif x > 9:
            init_val = x
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
            pass
    return happy_nums

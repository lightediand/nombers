def happy(n: int):
    happy_nums = [1]

    for i in range(2, n):
        x = i**2 if i < 10 else i

        while x > 9:
            x = sum([int(digit)**2 for digit in str(x)])

        if x == 1:
            happy_nums.append(i)

    return happy_nums

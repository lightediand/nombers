from nat import nat
from odd import odd
from primpytrip import ppt
from fib import fib
from even import even
from square import square
from triangle import tri
from happy import happy
from primes import primes
from dodec import dodec

menu=("\nThese are the numbers we currently have to offer.\n0: Natural numbers\n1: Odd numbers\n2: Primitive Pythagorean triples\n3: Fibonacci numbers\n4: Even numbers\n5: Square numbers\n6: Triangle numbers\n7: Happy numbers\n8: Prime numbers\n9: Dodecahedral numbers")

funcs = [nat, odd, ppt, fib, even, square, tri, happy, primes, dodec]

print("Hello and welcome to Nombers!\nYou want numbers?\nWe got numbers.\n")

while True:
    number_type = input("Please place your order. Type menu to show which numbers are available, or type exit to quit: ")
    if number_type == str("exit"):
        print("Have a nice day!")
        break
    elif number_type == str("menu"):
        print(menu)
        number_type = input("Number type: ")
    number = input("Specify an upper bound for your numbers: ")
    print("\nComing right up!")
    t = int(number_type)
    n = int(number)
    print(*funcs[t](n), "\n")

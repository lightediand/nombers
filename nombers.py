from nat import nat
from odd import odd
from primpytrip import ppt
from fib import fib
from even import even
from square import square
from triangle import tri
from happy import happy
from primes import primes

print("Hello and welcome to Nombers!\nYou want numbers?\nWe got numbers.\nHere are the types of numbers we currently have to offer.\nPlease place your order!\n")


print("0: Natural numbers")
print("1: Odd numbers")
print("2: Primitive Pythagorean triples")
print("3: Fibonacci numbers")
print("4: Even numbers")
print("5: Square numbers")
print("6: Triangle numbers")
print("7: Happy numbers")
print("8: Prime numbers")

number_type = input("\nChoose the type of numbers you wish to generate: ")

number = input("Specify an upper bound for your numbers: ")

t = int(number_type)
n = int(number)

funcs = [nat, odd, ppt, fib, even, square, tri, happy, primes]

print(funcs[t](n))

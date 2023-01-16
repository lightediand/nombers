from odd import odd
from primpytrip import ppt
from fib import fib

print("Hello and welcome to Nombers!\nWould you like some numbers?\nWe've got numbers.\nHere are the type of numbers we currently have.\nPlease place your order!\n")

print("1: Odd numbers")
print("2: Primitive Pythagorean triples")
print("3: Fibonacci numbers")

number = input("\nPlease specify an upper bound for your numbers: ")

number_type = input("Choose the type of numbers you wish to generate: ")

n = int(number)
t = int(number_type)

if t==1:
    print(odd(n))

if t==2:
    print(ppt(n))

if t==3:
    print(fib(n))

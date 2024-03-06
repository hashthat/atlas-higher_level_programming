#!/usr/bin/python3
def fizzbuzz():
    for x in range(101):
        if x % 3 == 0 and x % 5 == 0:
            print(f"{x}: FizzBuzz", end="\n")
        elif x % 3 == 0:
            print(f"{x}: Fizz", end="\n")
        elif x % 5 == 0:
            print(f"{x}: Buzz", end="\n")
        else:
            print(f"{x}: ", end="\n")

# Test the function
fizzbuzz()


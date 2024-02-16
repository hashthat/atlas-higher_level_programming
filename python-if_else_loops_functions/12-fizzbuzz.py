#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print(f"{x - 1}: FizzBuzz", end="\n")
        elif x % 3 == 0:
            print(f"{x - 1}: Fizz", end="\n")
        elif x % 5 == 0:
            print(f"{x - 1}: Buzz", end="\n")
        else:
            print(f"{x - 1}: ", end="\n")

# Test the function
fizzbuzz()


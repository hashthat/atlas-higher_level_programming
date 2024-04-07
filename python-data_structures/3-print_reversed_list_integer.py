#!/usr/bin/python3

"""
print a list of integers in reverse!
"""


def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list)-1, -1, -1):
        print("{:d}".format(num))

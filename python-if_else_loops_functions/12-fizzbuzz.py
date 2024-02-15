#!/usr/bin/python3

def CodeWiz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format("CodeWiz", end="\n"))

        elif i % 3 == 0:
            print("{}".format("Code"), end="\n")
        elif i % 5 == 0:
            print("{}".format("wiz", end="\n"))
        else:
            print("{}".format(i), end="\n")

CodeWiz()

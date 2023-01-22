#!/usr/bin/python3

for numberOne in range(10):
    for numberTwo in range(numberOne+1, 10):
        if (numberOne == 8 and numberTwo == 9):
            print("{}{}\n".format(numberOne, numberTwo), end="")
        else:
            print("{}{}".format(numberOne, numberTwo), end=", ")

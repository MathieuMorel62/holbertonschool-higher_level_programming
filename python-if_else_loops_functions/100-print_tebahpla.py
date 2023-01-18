#!/usr/bin/python3

for alphabReverse in range(90, 64, -1):
    if alphabReverse % 2:
        print("{}".format(chr(alphabReverse)), end="")
    else:
        print("{}".format(chr(alphabReverse + 32)), end="")

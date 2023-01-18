#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    numArgs = len(argv)

    if numArgs - 1 == 0:
        print("{} arguments.\n".format(numArgs - 1), end="")
    elif numArgs - 1 == 1:
        print("{} argument:\n".format(numArgs - 1), end="")
    else:
        print("{} arguments:\n".format(numArgs - 1), end="")

    if numArgs != 0:
        for index in range(1, numArgs):
            print("{}: {}".format(index, argv[index]))

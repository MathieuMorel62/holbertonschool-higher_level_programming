#!/usr/bin/python3

for print_number in range(00, 100):
    if print_number < 99:
        print("{:02d}".format(print_number), end=", ")
    else:
        print("{:02d}".format(print_number))

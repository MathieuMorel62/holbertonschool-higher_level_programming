#!/usr/bin/python3

from calculator_1 import add, sub, div, mul
import sys

if __name__ == '__main__':
    numberArg = sys.argv
    if len(numberArg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = int(numberArg[1])
    operator = numberArg[2]
    b = int(numberArg[3])
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

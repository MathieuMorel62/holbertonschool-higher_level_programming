#!/usr/bin/python3


def fizzbuzz():
    for fizz in range(1, 101):
        if fizz % 3 == 0 and fizz % 5 == 0:
            print("FizzBuzz", end=" ")
            continue
        elif fizz % 3 == 0:
            print("Fizz", end=" ")
            continue
        elif fizz % 5 == 0:
            print("Buzz", end=" ")
            continue
        print(fizz, end=" ")
        
#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


dictstatus = {}
totalsize = 0
totalcount = 0
try:
    for line in sys.stdin:
        split = line.split()
        status = split[-2]
        totalsize += int(split[-1])
        if status in dictstatus.keys():
            dictstatus[status] += 1
        else:
            dictstatus[status] = 1
        totalcount += 1
        if totalcount == 10:
            sortme = sorted(dictstatus.keys())
            print("File size:", totalsize)
            for keys in sortme:
                print("{}: {}".format(keys, dictstatus[keys]))
            totalcount = 0
            continue
except KeyboardInterrupt:
    sortme = sorted(dictstatus.keys())
    print("File size:", totalsize)
    for keys in sortme:
        print("{}: {}".format(keys, dictstatus[keys]))

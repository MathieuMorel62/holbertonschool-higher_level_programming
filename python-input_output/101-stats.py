#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


total_size = 0
status_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        elements = line.split()
        total_size += int(elements[-1])
        status_count[int(elements[-2])] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for status_code in sorted(status_count.keys()):
                if status_count[status_code] > 0:
                    print("{}: {}".format(status_code, status_count[status_code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status_code in sorted(status_count.keys()):
        if status_count[status_code] > 0:
            print("{}: {}".format(status_code, status_count[status_code]))

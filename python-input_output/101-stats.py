#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


status_counts = {}
total_size = 0
line_count = 0

for log_line in sys.stdin:
    split_line = log_line.split()
    status = split_line[-2]
    total_size += int(split_line[-1])

    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

    line_count += 1
    if line_count == 10:
        sorted_keys = sorted(status_counts.keys())
        print("Total size:", total_size)

        for key in sorted_keys:
            print("{}: {}".format(key, status_counts[key]))
        line_count = 0
        continue

#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


# Initialize variables
total_file_size = 0
status_codes = {
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
    # Read each line from stdin
    for line in sys.stdin:
        # Split the line by space to get the fields
        fields = line.split()

        if len(fields) < 5:
            continue

        # Get the status code and file size
        status_code = int(fields[-2])
        file_size = int(fields[-1])

        # Update the status code count and total file size
        status_codes[status_code] += 1
        total_file_size += file_size

        line_count += 1

        # If 10 lines have been processed, print the statistics
        if line_count % 10 == 0:
            print("File size:", total_file_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    # Print the final statistics when a keyboard interrupt (CTRL + C)
    print("File size:", total_file_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

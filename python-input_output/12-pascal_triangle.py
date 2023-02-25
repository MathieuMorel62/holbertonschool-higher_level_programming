#!/usr/bin/python3
""" Pascal's triangle"""


def pascal_triangle(n):
    """
    This function generates the Pascal triangle to line n.
    If n is smaller or equal to 0, returns an empty list.

    :Param n: The number of lines in Pascal's triangle.
    :Return: Pascal's triangle complete to line n.
    """
    if n <= 0:
        return []
    result = [[1]]
    for num_line in range(n-1):
        line = [1]
        for num_column in range(num_line):
            new_column = (result[-1][num_column] + result[-1][num_column+1])
            line.append(new_column)
        line.append(1)
        result.append(line)
    return result

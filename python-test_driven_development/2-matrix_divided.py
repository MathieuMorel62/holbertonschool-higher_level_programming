#!/usr/bin/python3
""" Function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    summary:
        Divides all elements of a matrix and returns the result as a new matrix

    Parameters:
        matrix (list of lists): a matrix of integers/floats
        div (int or float): the value to divide

    Returns:
        list of lists: a new matrix with all elements divided by div,
            rounded to 2 decimal places

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
            or if div is not a number
        TypeError: if each row of the matrix is not of the same size
        ZeroDivisionError: if div is equal to 0
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]

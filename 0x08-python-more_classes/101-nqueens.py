#!/usr/bin/python3
""" Program that solves the N queens problem. """


import sys


def solveNQueens(n):
    """ Function that solves the N queens problem for a given board size N. """
    def could_place(row, col):
        """
        Function that checks if a queen can be
        placed at a given row and column.
        """
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def place_queen(row, n):
        """
        Function that places queens on the board
        by calling itself recursively.
        """
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queen(row + 1, n)

    board = [-1] * n
    result = []
    place_queen(0, n)
    return result


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

result = solveNQueens(n)
for res in result:
    print([[i, j] for i, j in enumerate(res)])

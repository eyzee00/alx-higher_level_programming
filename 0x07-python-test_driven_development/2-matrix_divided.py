#!/usr/bin/pyhton3
"""Module defining matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    c = bool(type(matrix) is not list)
    if c or not all(isinstance(row, list) for row in matrix):
        s = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(s)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        s = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(s)
    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

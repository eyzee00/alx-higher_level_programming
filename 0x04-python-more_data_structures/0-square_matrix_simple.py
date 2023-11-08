#!/usr/bin/python3
def square(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    square_matrix = []
    for sublist in matrix:
        square_matrix.append(list(map(square, sublist)))
    return square_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

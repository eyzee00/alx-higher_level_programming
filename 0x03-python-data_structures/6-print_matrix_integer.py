#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for column in row:
            print("{:d}".format(column))


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print_matrix_integer(matrix)

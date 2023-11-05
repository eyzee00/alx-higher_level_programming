#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    j = 0
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end="")
            if j != len(row) - 1:
                print(" ", end="")
            j += 1
        j = 0
        print("")


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print_matrix_integer(matrix)

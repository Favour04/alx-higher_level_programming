#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in matrix:
        for j in i:
            d = len(i) - 1
            if j == i[d]:
                print("{:d}" .format(j))
            else:
                print("{:d}".format(j), end=' ')

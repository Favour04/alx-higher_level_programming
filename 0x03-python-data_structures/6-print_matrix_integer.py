#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 1:
        print("")
    for i in matrix:
        for j in i:
            d = len(i) - 1
            if j == i[d]:
                print("{}" .format(j))
            else:
                print("{}".format(j), end=' ')

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for i in matrix:
        k = 0
        n = -1
        for j in i:
            j = j ** 2
            if k % 3 == 0:
                temp.append([j])
            else:
                temp[n].append(j)
            k += 1
        n += 1
    return temp

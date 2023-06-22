#!/usr/bin/python3
"""
    Module containg matrix
    function
"""


def matrix_divided(matrix, div):
    """
        This function divide all
        the numbers in the list
        by div
    """

    # Verify in matrix is a list of list to prevent error
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix\
 (list of lists) of integers/floats')
    elif isinstance(matrix, list):
        # Ensuring that the list also contain set of list
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError('matrix must be a matrix\
 (list of lists) of integers/floats')

    # check if any value in the list is not int, float
    # also check if the sub list are of same size
    rowSize = len(matrix[0])
    for row in matrix:
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError('matrix must be a matrix\
 (list of lists) of integers/floats')
        if rowSize != len(row):
            raise TypeError('Each row of the matrix\
 must have the same size')

    # Lets Scrutinize div
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if div == float('inf'):
        raise ValueError('infinity wont be used')
    # divide each number in matrix by div
    new = []
    i = 0
    for row in matrix:
        idx = 0
        for column in row:
            result = column / div
            if idx == 0:
                new.append([round(result, 2)])
            else:
                new[i].append(round(result, 2))
            idx += 1
        i += 1
    return new

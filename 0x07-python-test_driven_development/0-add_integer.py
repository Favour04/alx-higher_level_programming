#!/usr/bin/python3
"""
    Module containing add_integer
    function to return sum of two
    integers
"""


def add_integer(a, b=98):

    """
    validate the input to a & b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    # Cast a & b to int incase they are float
    a = int(a)
    b = int(b)

    return a + b

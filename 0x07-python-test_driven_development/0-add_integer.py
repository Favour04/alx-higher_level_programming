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
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")

    # Cast a & b to int incase they are float
    try:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)

        return int(a) + int(b)
    except Exception as e:
        print(e)

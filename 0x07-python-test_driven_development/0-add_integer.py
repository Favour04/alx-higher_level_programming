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
    if not isinstance(a, (int, float)) and a is None:
        raise TypeError("a must be an integer")
        
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a & b to int incase they are float
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return int(a) + int(b)

#!/usr/bin/python3

"""
This module contain
A class.
"""


class BaseGeometry:
    """
    Methods:

    Area
    ----
    raises an eception message

    Integer_validator
    -----------------
    validates integer
    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        # valdidate integer
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

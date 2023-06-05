#!/usr/bin/python3
"""
    MODULE CONTAINS THE CLASS Square
"""


class Square:
    """
        CLASS CONTAIN THE ATTRIBUTE
        size, WHICH IS THE SIZE OF
        THE LEGNTH OF THE SQUARE
     """

    def __init__(self, size=0):
        """
            THIS FUNCTION INITIALIZES THE SIZE
            OF Square AND MAKE SURE IT IS A
            CORRECT VALUE
        """

        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

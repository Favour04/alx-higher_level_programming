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
            OF Square
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
         area FINDS AND RETURN THE AREA OF THE
         SQUARE. IT USES THE size ATTRIBUTE TO
         GET THE AREA
        """

        sqrArea = self.__size * self.__size
        return sqrArea

    def my_print(self):
        """
            FUNCTION TO PRINT THE SQUARE
        """

        if self.size == 0:
            print(None)
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end='')
            print("")

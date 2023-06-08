#!/usr/bin/python3

"""
MODLE CONTAINING CLASS RECTANGLE
"""


class Rectangle:
"""
   Class containing the attributes of a
   Square

"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

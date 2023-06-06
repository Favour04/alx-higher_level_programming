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

    def __init__(self, size=0, position=(0, 0)):
        """
            THIS FUNCTION INITIALIZES THE SIZE
            OF Square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            try:
                x, y = value
                self.__position = value
                if not isinstance(y, int) or not isinstance(x, int):
                    raise TypeError('position must be a tuple of 2 positive integers')
                if y < 0 or x < 0:
                    raise TypeError('position must be a tuple of 2 positive integers')
            except Exception:
                raise TypeError('position must be a tuple of 2 positive integers')

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
            print()

        x, y = self.position

        #if not isinstance(y, int) or not isinstance(x, int):
         #   raise TypeError('position must be a tuple of 2 positive integers')
        #if y < 0 or x < 0:
            #raise TypeError('position must be a tuple of 2 positive integers')

        for i in range(0, self.size):
           
            if self.position is not None and x != 0:
                print(" " * x, end='')
            
            for j in range(0, self.size):
                print("#", end='')

            print("")

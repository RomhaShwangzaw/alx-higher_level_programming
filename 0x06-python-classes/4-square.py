#!/usr/bin/python3
''' A module containing a Square class '''


class Square:
    ''' A Square class'''

    def __init__(self, size=0):
        ''' Initialization function '''

        self.size = size

    def area(self):
        ''' Returns the area of the square '''

        return self.__size * self.__size

    @property
    def size(self):
        ''' Retrieves the value of size '''

        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the value of size '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

#!/usr/bin/python3
''' A module containing a Square class '''


class Square:
    ''' A Square class'''

    def __init__(self, size=0):
        ''' Initialization function '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        ''' Returns the area of the square '''

        return self.__size * self.__size

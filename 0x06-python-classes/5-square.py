#!/usr/bin/python3
''' A module containing a Square class '''


class Square:
    ''' A Square class'''

    def __init__(self, size=0):
        ''' Initialization function '''

        self.__size = size

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

        self.__size = value

    def my_print(self):
        '''
            prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
        '''

        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

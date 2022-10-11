#!/usr/bin/python3
''' A module containing a Square class '''


class Square:
    ''' A Square class'''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initialization function '''

        self.__size = size
        self.__position = position

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
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for p in range(self.__position[0]):
                    print(" ", end="")

                for j in range(self.__size):
                    print("#", end="")

                print()

    @property
    def position(self):
        ''' Retrieves the value of position '''

        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets the value of position '''

        if (not isinstance(value, tuple) or len(value) != 2
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

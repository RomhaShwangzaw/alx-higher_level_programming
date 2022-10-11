#!/usr/bin/python3
''' A module containing a Square class '''


class Square:
    ''' A Square class'''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initialization function '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        ''' Retrieves the value of position '''

        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets the value of position '''

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        ''' Returns the area of the square '''

        return self.__size * self.__size

    def my_print(self):
        ''' Print the square with the # character '''

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

    def __str__(self):
        ''' Define the print() representation of a Square '''

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

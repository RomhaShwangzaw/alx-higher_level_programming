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

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()

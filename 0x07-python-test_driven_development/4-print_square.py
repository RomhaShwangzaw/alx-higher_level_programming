#!/usr/bin/python3
''' THIS IS A MODULE THAT PRINTS A SQUARE USING'#' '''


def print_square(size):
    ''' Prints a square of size 'size' with '#' notation '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()

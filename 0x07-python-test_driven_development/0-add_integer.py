#!/usr/bin/python3
''' THIS IS AN ADDITION MODULE'''


def add_integer(a, b=98):
    ''' This function adds two integers and returns the result '''

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))

#!/usr/bin/python3
'''A subclass checking module'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    '''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False

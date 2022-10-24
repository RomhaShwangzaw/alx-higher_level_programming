#!/usr/bin/python3
'''An instance checking module'''


def is_kind_of_class(obj, a_class):
    '''returns True if the object is an instance of the specified class or any
    of its base classes, otherwise False.
    '''
    return isinstance(obj, a_class)

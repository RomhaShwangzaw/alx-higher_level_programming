#!/usr/bin/python3
'''A module for knowing if we can add new attributes to an object'''


def add_attribute(obj, attr, value):
    '''adds a new attribute to an object if it’s possible:
    Raise a TypeError exception, with the message can't add new attribute
    if the object can’t have new attribute.

    You are not allowed to use try/except.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

#!/usr/bin/python3
''' A Locked Class Module '''


class LockedClass:
    ''' A class that prevents the user from dynamically creating 
        new instance attributes, except if the new instance 
        attribute is called first_name.
    '''
    __slots__ = ['first_name']

#!/usr/bin/python3
# Contains a functions to find peak of a list of integers

def find_peak(list_of_integers):
    """Finds the peak of a list of integers"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[len(list_of_integers) - 1]

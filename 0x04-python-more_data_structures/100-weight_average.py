#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num = 0
    den = 0
    for s, w in my_list:
        num += s * w
        den += w

    return num / den

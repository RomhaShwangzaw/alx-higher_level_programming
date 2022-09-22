#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 0
    res = 0
    for arg in sys.argv:
        if i != 0:
            res += int(arg)
        i = 1

    print(res)

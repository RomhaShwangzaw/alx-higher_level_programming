#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = -number
    else:
        num = number

    last = num % 10
    print(last, end="")
    return last

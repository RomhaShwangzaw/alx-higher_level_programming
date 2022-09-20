#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {} {}"
last = number % 10
if last > 5:
    print(str.format(number, last, "and is greater than 5"))
elif last = 0:
    print(str.format(number, last, "and is 0"))
else:
    print(str.format(number, last, "and is less than 6 and not 0"))

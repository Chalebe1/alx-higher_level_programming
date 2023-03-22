#!/usr/bin/python3
def print_last_digit(number):
    if (number >= 0):
        last_digit = number % 10
    else:
        pos = abs(number) % 10
        last_digit = (pos)
    print("{:d}".format(last_digit), end="")
    return last_digit

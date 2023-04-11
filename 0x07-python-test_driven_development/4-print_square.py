#!/usr/bin/python3
"""

This module contain a function that is gonna print only a square

"""


def print_square(size):
    """This function prints a square with the character (#)

    Args:
        size (int):  the length of the square

    Raises:
        TypeError: If size not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size should be n integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be  integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")

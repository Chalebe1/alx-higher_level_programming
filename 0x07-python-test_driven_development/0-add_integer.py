#!/usr/bin/python3
"""

This module has one function that is going to adds up 2 integers

"""


def add_integer(a, b=98):
    """Return the sum of two integers/floats as integers

    Args:
        a: first arg
        b: second arg

    Returns:
        Sum of the two arg

    Raises:
        TypeError: If either of the arguments is not an integer or a floating value
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a should be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b should be an integer")
    return (int(a) + int(b))

#!/usr/bin/python3
""""

This module is containing a function that prints just a name

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name> <last name>)

    Args:
        first_name (str):  fisrt name to be printed
        last_name (str):  last name to be printed

    Raises:
        TypeError: If  the first_name and last_name are not strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

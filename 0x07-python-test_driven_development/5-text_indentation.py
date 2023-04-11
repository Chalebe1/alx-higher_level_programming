#!/usr/bin/python3
"""

This module contains a function that will  indents only texts

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str):  string to be printed

    Raises:
        TypeError: when text is not a string

    '''

    if not isinstance(text, str):
        raise TypeError("textshould be  string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1

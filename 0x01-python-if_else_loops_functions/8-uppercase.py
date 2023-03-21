#!/usr/bin/python3
def uppercase(str):
    str_len = len(str)
    i = 0
    while (str_len):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str[i] = ord(str[i]) - 32
    print(str)

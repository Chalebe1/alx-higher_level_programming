#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) || idx < 0:
        return my_list
    Del(my_list[idx])
    return my_list

#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list):
        biggest = 0
        for i in len(my_list):
            if (my_list[i] > biggest):
                biggest = my_list[i]
        return biggest
    else:
        return None
                

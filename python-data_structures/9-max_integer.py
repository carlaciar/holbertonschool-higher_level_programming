#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()

    if len(my_list) > 0:
        maxint = my_list[-1]

    if len(my_list) == 0:
        maxint = "None"

    return maxint

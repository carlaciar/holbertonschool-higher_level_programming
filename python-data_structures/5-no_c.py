#!/usr/bin/python3
def no_c(my_string):
    newstring = ""

    for ch in my_string:
        if ch != 'c' and ch != 'C':
            newstring += ch

    return newstring

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()

    for index, item in enumerate(copy):
        if item == search:
            copy[index] = replace
    
    return copy

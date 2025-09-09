#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 2:
          list_a = list(tuple_a[:2])

    if len(tuple_b) >= 2:
        list_b = list(tuple_b[:2])

    if len(tuple_a) < 2:
        list_a = list(tuple_a)
        list_a.append(0)
        list_a.append(0)
    
    if len(tuple_b) < 2:
        list_b = list(tuple_b)
        list_b.append(0)
        list_b.append(0)
    
    x = list_a[0] + list_b[0]
    y = list_a[1] + list_b[1]
    addtuple = tuple([x, y])
    return addtuple

    

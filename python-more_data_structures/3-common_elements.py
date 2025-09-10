#!/usr/bin/python3
def common_elements(set_1, set_2):
    commonset = {}

    commonset = set(set_1.intersection(set_2))

    return commonset

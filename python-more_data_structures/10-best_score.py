#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:   # handles None or empty dict
        return None

    return max(a_dictionary, key=a_dictionary.get)

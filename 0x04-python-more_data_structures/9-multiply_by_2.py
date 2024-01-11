#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    new_d = {}
    for i in a_dictionary.items():
        a, b = i
        new_d[a] = b * 2
    return new_d

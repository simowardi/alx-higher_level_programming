#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    n_list = []
    for element in my_list:
        if element == search:
            n_list.append(replace)
        else:
            n_list.append(element)
    return n_list

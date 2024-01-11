#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    n_list = set(my_list)
    res = 0
    new = list(n_list)
    for i in range(len(new)):
        res += new[i]
    return res

#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    """
    if not list_of_integers or list_of_integers == []:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the middle element is smaller than the next element
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # If true, the peak (if it exists) is to the right of mid
            # Update left to mid + 1
            left = mid + 1
        else:
            # Otherwise, the peak (if it exists) is to the left of or at mid
            # Update right to mid
            right = mid
    # After the loop terminates, left will point to a peak element
    return list_of_integers[left]

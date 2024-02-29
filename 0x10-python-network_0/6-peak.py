#!/usr/bin/python3
"""
contains find_peak function
"""


def find_peak(list_of_integers):
    """
    func finds the peak in a list
    """
    if not list_of_integers:
        return None
    for i in range(1, len(list_of_integers)):
        if (list_of_integers[i] > list_of_integers[i - 1]) and \
        (list_of_integers[i] > list_of_integers[i+1]):
            return list_of_integers[i]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

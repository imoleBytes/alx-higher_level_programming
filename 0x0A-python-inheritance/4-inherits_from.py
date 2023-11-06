#!/usr/bin/python3

"""a function that returns True if the object is a subclass; otherwise False.
"""


def inherits_from(obj, a_class):
    """this funtion return true if obj is a subclass of a_class
        Args:
            obj;
            a_class;
    """

    if issubclass(obj.__class__, a_class):
        return True
    return False


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

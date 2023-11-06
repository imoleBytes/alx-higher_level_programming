#!/usr/bin/python3

"""a function that returns True if the object is exactly an instance of
the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """this funtion return true if obj is a_class
        Args:
            obj;
            a_class;
    """
    if not obj or not a_class:
        raise NameError("obj or a_class must be supplied")
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False

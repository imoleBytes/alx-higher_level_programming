#!/usr/bin/python3

"""function converts to string"""
import json


def to_json_string(my_obj):
    """returns the string representation of an object
    Args:
        my_obj: can be any
    """
    return json.dumps(my_obj)

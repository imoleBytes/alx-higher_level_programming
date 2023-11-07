#!/usr/bin/python3

"""function converts a string to object"""
import json


def from_json_string(my_str):
    """returns the object representation of a json string
    Args:
        my_str: can be any
    """
    return json.loads(my_str)

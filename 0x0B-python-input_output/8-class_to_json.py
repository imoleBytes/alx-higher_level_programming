#!/usr/bin/python3

"""function returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """returns the dict discription of a class object"""
    str = json.dumps(obj.__dict__)
    return (str)

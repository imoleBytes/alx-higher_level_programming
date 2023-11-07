#!/usr/bin/python3

"""function that loads a json file, and convert to an object"""
import json


def load_from_json_file(filename):
    """returns an object representatio of a json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

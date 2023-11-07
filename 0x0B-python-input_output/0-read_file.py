#!/usr/bin/python3


"""functions on reading from a file"""


def read_file(filename=""):
    """function reads from a file
    Args:
        filename (str): file name
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

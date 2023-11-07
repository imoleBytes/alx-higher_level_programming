#!/usr/bin/python3


"""function appends to a file"""


def append_write(filename="", text=""):
    """function appends to a file
    Args:
        filename (str): file name
        text (str): text to write
    """
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
        return (n)

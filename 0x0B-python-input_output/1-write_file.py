#!/usr/bin/python3


"""functions on reading from a file"""


def write_file(filename="", text=""):
    """function writes to a file
    Args:
        filename (str): file name
        text (str): text to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
        return (n)

#!/usr/bin/python3


"""Base class"""


class Base:
    """base class defination"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id:
            self.id = id
        else:
            # self.__class__.__nb_objects
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

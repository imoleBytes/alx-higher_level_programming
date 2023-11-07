#!/usr/bin/python3

"""a class Student that defines a student """


class Student:
    """student class defination"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dict discription of a class object"""
        dict_rep = self.__dict__
        return (dict_rep)

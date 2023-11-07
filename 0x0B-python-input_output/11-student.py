#!/usr/bin/python3

"""a class Student that defines a student """


class Student:
    """student class defination"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dict discription of a class object"""
        dict_rep = self.__dict__
        if type(attrs) is list:
            are_all_strings = all(isinstance(item, str) for item in attrs)
            if are_all_strings:
                new_dict = {i: dict_rep.get(i) for i in attrs if i in dict_rep}
                return (new_dict)
        return (dict_rep)

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)

#!/usr/bin/python3


"""Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionary must be a list of dict")
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        serializable_list = [r.to_dictionary() for r in list_objs]
        s = cls.to_json_string(serializable_list)
        obj = json.loads(s)
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            json.dump(obj, f)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string == "":
            return []
        return json.loads(json_string)

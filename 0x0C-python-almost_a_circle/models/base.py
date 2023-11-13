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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances, data gotten from a json file"""
        try:
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
                # list_of_dict = json.load(f)
                list_of_dict_str = f.read()
        except FileNotFoundError:
            return []
        else:
            list_of_dict = cls.from_json_string(list_of_dict_str)
            return [cls.create(**dic) for dic in list_of_dict]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes an obj and save to a csv file"""
        serializable_list = [r.to_dictionary() for r in list_objs]
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            for dic in serializable_list:
                if cls.__name__ == "Rectangle":
                    f.write(f"{dic['id']},{dic['width']},{dic['height']},{dic['x']},{dic['y']}\n")
                elif cls.__name__ == "Square":
                    f.write(f"{dic['id']},{dic['size']},{dic['x']},{dic['y']}\n")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes string representation of the objects from a csv file
        and return a list of objects
        """
        list_of_obj = []
        try:
            with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as f:
                s = f.readlines() #[:-1]     
            for line in s:
                line = line[:-1] #to remove the '\n' character
                ls = line.split(",")
                if cls.__name__ == "Rectangle":
                    dummy = cls(int(ls[1]), int(ls[2]), x=int(ls[3]), y=int(ls[4]), id=int(ls[0]))
                elif cls.__name__ == "Square":
                    dummy = cls(int(ls[1]), x=int(ls[2]), y=int(ls[3]), id=int(ls[0]))
                list_of_obj.append(dummy)
        except FileNotFoundError:
            print("File not found!")
            exit()
        return list_of_obj

    def draw(list_rectangles, list_squares):
        """draw the shapes!"""
        pass
    
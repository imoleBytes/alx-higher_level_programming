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


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

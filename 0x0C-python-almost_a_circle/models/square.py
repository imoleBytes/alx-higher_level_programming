#!/usr/bin/python3


"""Square class inherits from Rectangle class"""
from models.rectangle import Rectangle
# Base = __import__("base").Base


class Square(Rectangle):
    """Square class defination
    its inherit from  Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize by calling its parent init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """string representation of the object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """size is set and validated here"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """this updates the attributes of the instance"""
        if args:
            num = len(args)
            if num > 0:
                self.id = args[0]
            if num > 1:
                self.size = args[1]
            if num > 2:
                self.x = args[2]
            if num > 3:
                self.y = args[3]
        if kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

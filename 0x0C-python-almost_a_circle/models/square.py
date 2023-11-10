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

#!/usr/bin/python3


"""Rectangle class inherits from Base class"""
from models.base import Base
# Base = __import__("base").Base


class Rectangle(Base):
    """Rectangle class defination
    its inherit from  Base class
    Args:
        width: int
        height: int
        x: int
        y: int
        id: int
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """width property"""
            return self.__width

        @width.setter
        def width(self, value):
            """width is set and validated here"""
            self.__width = value
            return self.__width

        @property
        def height(self):
            """height property"""
            return self.__height

        @height.setter
        def height(self, value):
            """height is set and validated here"""
            self.__height = value
            return self.__height

        @property
        def x(self):
            """x property"""
            return self.__x

        @x.setter
        def x(self, value):
            """x is set and validated here"""
            self.__x = value
            return self.__x

        @property
        def y(self):
            """y property"""
            return self.__y

        @y.setter
        def y(self, value):
            """y is set and validated here"""
            self.__y = value
            return self.__y

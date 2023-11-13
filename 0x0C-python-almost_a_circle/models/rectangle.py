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
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height is set and validated here"""
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """x is set and validated here"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """y is set and validated here"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the are value of the object"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for line in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """string representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """this updates the attributes of the instance"""
        num = len(args)
        if num > 0:
            self.id = args[0]
        if num > 1:
            self.width = args[1]
        if num > 2:
            self.height = args[2]
        if num > 3:
            self.x = args[3]
        if num > 4:
            self.y = args[4]

        for k, v in kwargs.items():
            if k == "id":
                if v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of the Rectangle"""
        dic = \
            {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        return dic

#!/usr/bin/python3
"""Module for creating rectangle class"""


class Rectangle:
    """Creating rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
try:
    my_rectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    my_rectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
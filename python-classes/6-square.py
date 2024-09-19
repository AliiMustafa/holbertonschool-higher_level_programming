#!/usr/bin/python3
"""Module for class"""


class Square():
    """Define class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        for x in position:
            if not isinstance(x, int):
                raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        for x in value:
            if not isinstance(x, int):
                raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("_" * self.__position[0], end="")
            for j in range(self.__size):
                if j == self.__size - 1:
                    print("#")
                else:
                    print("#", end="")

#!/usr/bin/python3
"""Module for class"""


class Square:
    """Define class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        for x in range(len(position)):
            if not (isinstance(position[x], int) and len(position) == 2 and
                    position[x] >= 0 and isinstance(position, tuple)):
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

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    @position.setter
    def position(self, value):
        for x in range(len(value)):
            if not (isinstance(value[x], int) and len(value) == 2 and
                    value[x] > 0 and isinstance(value, tuple)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(self.__position[0] * " " + self.size * "#")

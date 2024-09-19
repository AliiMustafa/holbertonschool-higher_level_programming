#!/usr/bin/python3
"""Module for class"""


class Square:
    """Define class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if not isinstance(all(position), int) or len(position) != 2 or position < (0, 0):
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(all(value), int) or len(value) != 2 or value < (0, 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print("_" * self.__position[0], end="")
                for j in range(self.__size):
                    if j == self.__size - 1:
                        print("#")
                    else:
                        print("#", end="")

#!/usr/bin/env python3
"""Module for creating abc class"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """create abc class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """create subclass of shape class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Area: {self.area()}\nPerimeter: {self.perimeter()}"


class Rectangle(Shape):
    """create subclass of shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Area: {self.area()}\nPerimeter: {self.perimeter()}"


def shape_info(obj):
    print(obj)

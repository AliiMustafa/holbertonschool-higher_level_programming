#!/usr/bin/python3
"""Module for class to json"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new = {}
        for at in attrs:
            if at in self.__dict__:
                new[at] = self.__dict__[at]
        return new

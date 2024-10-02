#!/usr/bin/python3
"""Module for write data"""


def append_write(filename="", text=""):
    """Function for append write data"""
    with open(filename, "a+", encoding="UTF-8") as f:
        data = f.write(text)
        return data

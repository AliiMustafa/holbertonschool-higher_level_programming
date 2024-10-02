#!/usr/bin/python3
"""Module for write data in file"""


def write_file(filename="", text=""):
    """function for write data in text"""
    with open(filename, "x", encoding="utf-8") as f:
        data = f.write(text)
        return data

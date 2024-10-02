#!/usr/bin/python3
"""Module for read data"""
def read_file(filename=""):
    """function for read data"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
#!/usr/bin/python3
"""Module for save json"""
import json


def save_to_json_file(my_obj, filename):
    """Function for save json"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))

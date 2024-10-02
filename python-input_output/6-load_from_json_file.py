#!/usr/bin/python3
"""Module for save json"""
import json


def load_from_json_file(filename):
    """Function for save json"""
    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())

#!/usr/bin/python3
"""Module for JSON"""
import json


def serialize_and_save_to_file(data, filename):
    """Function for save to json file"""
    json_data = json.dumps(data)

    with open(filename, "w") as f:
        f.write(data)

def load_and_deserialize(filename):
    """Function for load python"""
    with open(filename, "r") as f:
        from_json = f.read()

    return json.loads(from_json)

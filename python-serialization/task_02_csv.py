#!/usr/bin/python3
"""Module for CSV serialization"""
import csv
import json


def convert_csv_to_json(filename):
    """Function for convert csv to json"""
    try:
        with open(filename, "r") as f:
            my_data = csv.DictReader(f)
            data = list(my_data)

        with open("data.json", "w") as j:
            j.write(json.dumps(data, indent=4))
            return True

    except Exception:
        return False

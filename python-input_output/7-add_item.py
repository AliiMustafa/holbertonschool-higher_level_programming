#!/usr/bin/python3
"""Module for add all arguments"""
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file = "add_item.json"

try:
    my_list = load_from_json_file(file)
except FileNotFoundError:
    my_list = []
my_list.extend(argv[1:])
save_to_json_file(my_list, file)

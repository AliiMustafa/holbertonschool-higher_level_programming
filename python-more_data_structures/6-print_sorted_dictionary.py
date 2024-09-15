#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_a = sorted(a_dictionary.items())
    for i, j in new_a:
        print(f"{i}: {j}")

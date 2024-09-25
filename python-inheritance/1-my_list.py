#!/usr/bin/python3
"""Module for print asc order"""


class MyList(list):
    """Class inherited from list class"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))

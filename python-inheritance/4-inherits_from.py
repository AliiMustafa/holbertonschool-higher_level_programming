#!/usr/bin/python3
"""Module for instance"""


def inherits_from(obj, a_class):
    """Function ofr instance"""
    return isinstance(obj, a_class) and type(obj) is not a_class

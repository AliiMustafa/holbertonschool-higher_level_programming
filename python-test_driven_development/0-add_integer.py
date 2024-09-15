#!/usr/bin/python3
"""Module for function of adding integer"""


def add_integer(a, b=98):
    """Add function for integers"""

    # Check if a and b is int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    #  Change the type of a and b if both are float
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Return sum of a and b
    return a + b

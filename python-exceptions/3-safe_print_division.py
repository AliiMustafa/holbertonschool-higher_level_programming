#!/usr/bin/python3
from typing import final


def safe_print_division(a, b):
    result  = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result

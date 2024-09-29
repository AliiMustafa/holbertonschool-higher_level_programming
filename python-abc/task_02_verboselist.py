#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Module for creating list class"""


class VerboseList(list):
    """List class"""

    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items.")

    def remove(self, value):
        if value in self:
            print(f"Removed [{value}] from the list.")
            super().remove(value)

    def pop(self, value=None):
        if value is None:
            r = super().pop()
            print(f"Popped [{r}] from the list.")
            return r
        else:
            r = super().pop(value)
            print(f"Popped [{r}] from the list.")
            return r

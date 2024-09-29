#!/usr/bin/python3
"""Module for iteration class"""


class CountedIterator:
    """Class for iteration"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter

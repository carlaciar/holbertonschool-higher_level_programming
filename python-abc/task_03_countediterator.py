#!/usr/bin/env python3
"""
An iterator class that counts how many items have been iterated.
"""


class CountedIterator:
    """Iterator wrapper that counts how many items have been yielded."""
    def __init__(self, iterable):
        self._it = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._it)
        self._count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated so far."""
        return self._count

    def next(self):
        return self.__next__()

"""Difference between two collections"""


def diff(a, b):
    return sorted(set(a).symmetric_difference(b))

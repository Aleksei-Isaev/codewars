"""
White or Black?
"""


def square_color(file, rank):
    return {
        0: 'black',
        1: 'white'
    }.get(({
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }.get(file) + rank) % 2)

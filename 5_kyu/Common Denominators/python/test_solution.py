import pytest

from solution import convert_fracts


tests = [
    (
        [],
        []
    ),
    (
        [[1, 2], [1, 3], [1, 4]],
        [[6, 12], [4, 12], [3, 12]]
    ),
    (
        [[2, 7], [1, 3], [1, 12]],
        [[24, 84], [28, 84], [7, 84]]
    ),
    (
        [[69, 130], [87, 1310], [3, 4]],
        [[18078, 34060], [2262, 34060], [25545, 34060]]
    ),
    (
        [[77, 130], [84, 131], [3, 4]],
        [[20174, 34060], [21840, 34060], [25545, 34060]]
    ),
    (
        [[6, 13], [187, 1310], [31, 41]],
        [[322260, 698230], [99671, 698230], [527930, 698230]]
    ),
    (
        [[8, 15], [7, 111], [4, 25]],
        [[1480, 2775], [175, 2775], [444, 2775]]
    ),
    (
        [[1, 1], [3, 1], [4, 1], [5, 1]],
        [[1, 1], [3, 1], [4, 1], [5, 1]]
    ),
    (
        [[1, 100], [3, 1000], [1, 2500], [1, 20000]],
        [[200, 20000], [60, 20000], [8, 20000], [1, 20000]]
    ),
    (
        [[27115, 5262], [87546, 11111111], [43216, 255689]],
        [
            [77033412951888085, 14949283383840498],
            [117787497858828, 14949283383840498],
            [2526695441399712, 14949283383840498]
        ]
    ),
]


@pytest.mark.parametrize(
    "lst, expected", tests
)
def test_convert_fracts(lst, expected):
    assert convert_fracts(lst) == expected

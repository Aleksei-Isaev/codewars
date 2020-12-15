import pytest

from solution import sum_even_numbers


@pytest.mark.parametrize(
    "seq, result",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),
        ([], 0),
        ([1337, 374, 849, 22.5, 19, 16, 0, 0, 16, 32], 438),
        ([-16, -32, 20, 21, 41, 42], 14),
        (
            [
                15397,
                12422,
                10495,
                22729,
                23921,
                18326,
                27955,
                24073,
                23690,
                15002,
                11615,
                15682,
                24346,
                16725,
                17252,
                20467,
                20493,
                17807,
                13041,
                25861,
                22471,
                22747,
                24082,
                18979,
                28543,
                26488,
                10002,
                24740,
                17950,
                26573,
                25851,
                19446,
                22584,
                14857,
                17387,
                29310,
                28265,
                19497,
                11394,
                28111,
                20957,
                17201,
                26647,
                26885,
                27297,
                17252,
                25961,
                12409,
                22858,
                27869,
                19832,
                13906,
                11256,
                11304,
                24186,
                28783,
                16647,
                23073,
                11105,
                13327,
                17102,
                10172,
                21104,
                23001,
                24108,
                16166,
                21690,
                14218,
                11903,
                10286,
                19116,
                18585,
                25511,
                18273,
                11862,
                17166,
                13456,
                28562,
                16262,
                11100,
                22806,
                14748,
                17362,
                11633,
                17165,
                16390,
                24580,
                22498,
                26121,
                16170,
                18917,
                26963,
                17605,
                20839,
                22487,
                12187,
                23752,
                12444,
                14392,
                28313,
            ],
            870822,
        ),
    ],
)
def test_sum_even_numbers(seq, result):
    assert sum_even_numbers(seq) == result

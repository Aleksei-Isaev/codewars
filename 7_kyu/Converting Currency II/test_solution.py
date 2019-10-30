from solution import solution


def test_convert_to_usd():
    res = ['$1.15', '$94.65', '$5.68', '$26.40', '$822.98']
    assert solution('USD', [1.01, 83.29, 5.0, 23.23, 724.22]) == res

    res = ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']
    assert solution('USD', [1394.0, 250.85, 721.3, 911.25, 1170.67]) == res


def test_convert_to_eur():
    res = ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']
    assert solution('EUR', [109.45, 640.31, 1310.99, 669.51, 415.54]) == res

    res = ['518.58€', '582.83€', '1,187.74€', '103.78€', '7.26€']
    assert solution('EUR', [589.29, 662.31, 1349.71, 117.93, 8.25]) == res


def test_currency_not_implemented():
    assert solution('XYZ', [1.01, 83.29, 5.0, 23.23, 724.22]) is None

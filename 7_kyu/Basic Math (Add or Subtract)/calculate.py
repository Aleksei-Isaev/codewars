"""
Basic Math (Add or Subtract)
"""


def calculate(s):
    return str(eval(s.replace('plus', '+').replace('minus', '-')))

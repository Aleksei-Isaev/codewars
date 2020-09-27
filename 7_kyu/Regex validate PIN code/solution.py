"""Regex validate PIN code
"""

import re


def validate_pin(pin):
    return bool(re.match(r'(?:\d{4}$|\d{6})\Z', pin))

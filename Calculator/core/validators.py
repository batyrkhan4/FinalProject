import re


def is_valid_number(value):
    """
    Checks if the value is a valid integer or decimal number.
    """
    pattern = r"^-?\d+(\.\d+)?$"
    return bool(re.match(pattern, value))
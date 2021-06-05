__all__ = [
    'centering_indentation_len',
    'indented',
    'newlined',
    'newline_succeeded'
]

from typing import Any
import functools


def centering_indentation_len(string_length: int, reference_length: int) -> int:
    """ Returns:
            length of whitespace indentation necessary for centering string
            wrt reference_length

    >>> centering_indentation_len(4, 50)
    23
    >>> centering_indentation_len(7, 23)
    8 """

    return reference_length // 2 - string_length // 2


def indented(serializable_obj: Any, columns: int) -> str:
    return f'{" ".rjust(columns)}{serializable_obj}'


def newlined(serializable_obj: Any) -> str:
    return f'{serializable_obj}\n'


def newline_succeeded(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return newlined(func(*args, **kwargs))
    return wrapper

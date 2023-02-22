from typing import Any


def centering_indentation_len(string_length: int, reference_length: int) -> int:
    """ Returns:
            length of whitespace indentation necessary for centering string
            wrt reference_length

    >>> centering_indentation_len(4, 50)
    23
    >>> centering_indentation_len(7, 23)
    8 """

    return reference_length // 2 - string_length // 2


def indented(obj: Any, by: int) -> str:
    """
    >>> indented('AYYYYYYAYAYAYAYAY', 7)
    '       AYYYYYYAYAYAYAYAY' """

    return f'{indentation(by)}{obj}'


def indentation(length: int) -> str:
    return " " * length


def newline_trailed(obj: Any) -> str:
    return f'{obj}\n'

from asciiplot._utils.type_aliases import Serializable


def centering_indentation_len(string_length: int, reference_length: int) -> int:
    """ Returns:
            length of whitespace indentation necessary for centering string
            wrt reference_length

    >>> centering_indentation_len(4, 50)
    23
    >>> centering_indentation_len(7, 23)
    8 """

    return reference_length // 2 - string_length // 2


def indented(serializable: Serializable, columns: int) -> str:
    """
    >>> indented('AYYYYYYAYAYAYAYAY', 7)
    '       AYYYYYYAYAYAYAYAY' """

    return f'{" ".rjust(columns)}{serializable}'


def newline_succeeded(serializable: Serializable) -> str:
    return f'{serializable}\n'
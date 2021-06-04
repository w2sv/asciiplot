from typing import Any
import shutil

import colored as _colored


RESET_COLOR_ANSI: str = _colored.style.RESET


def colored(serializable_obj: Any, color: str) -> str:
    """
    >>> print(colored('yessir', _colored.colors.names[0]))
    \x1b[38;5;0myessir\x1b[0m
    >>> print(colored('wasssup', _colored.colors.names[-1]))
    \x1b[38;5;255mwasssup\x1b[0m """

    try:
        return f'{_colored.fg(_colored.colors.names.index(color))}{serializable_obj}{RESET_COLOR_ANSI}'
    except ValueError:
        raise ValueError(f"'{color}' not amongst eligible colors")


def centering_indentation_len(string_length: int, reference_length: int) -> int:
    """ Returns:
            length of whitespace indentation necessary for centering string
            wrt reference_length

    >>> centering_indentation_len(4, 50)
    23
    >>> centering_indentation_len(7, 23)
    8 """

    return reference_length // 2 - string_length // 2


def terminal_columns() -> int:
    return shutil.get_terminal_size().columns


def indented(serializable_obj: Any, columns: int) -> str:
    return f'{" ".rjust(columns)}{serializable_obj}'


def newlined(serializable_obj: Any) -> str:
    return f'{serializable_obj}\n'

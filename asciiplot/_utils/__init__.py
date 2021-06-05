from typing import Any
import shutil

import colored as _colored

from .formatting import *


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


def terminal_columns() -> int:
    return shutil.get_terminal_size().columns


if __name__ == '__main__':
    print(_colored.colors.names)
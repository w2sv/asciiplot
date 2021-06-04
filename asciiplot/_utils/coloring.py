from typing import Any

import colored as _colored


RESET: str = _colored.style.RESET


def colored(obj: Any, color: str) -> str:
    """
    >>> print(colored('yessir', _colored.colors.names[0]))
    \x1b[38;5;0myessir\x1b[0m
    >>> print(colored('wasssup', _colored.colors.names[-1]))
    \x1b[38;5;255mwasssup\x1b[0m """

    try:
        return f'{_colored.fg(_colored.colors.names.index(color))}{obj}{RESET}'
    except ValueError:
        raise ValueError(f"'{color}' not amongst eligible colors")

import colored as _colored


RESET_COLOR: str = _colored.style.RESET


def colored(string: str, color: str) -> str:
    """
    >>> print(colored('yessir', _colored.colors.names[0]))
    \x1b[38;5;0myessir\x1b[0m
    >>> print(colored('wasssup', _colored.colors.names[-1]))
    \x1b[38;5;255mwasssup\x1b[0m """

    try:
        return _colored.fg(_colored.colors.names.index(color)) + string + RESET_COLOR
    except ValueError:
        raise ValueError(f"'{color}' not amongst eligible colors")

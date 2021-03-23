import colored as _colored


RESET_COLOR: str = _colored.style.RESET


def colored(string: str, color: str) -> str:
    return _colored.fg(_colored.colors.names.index(color)) + string + RESET_COLOR

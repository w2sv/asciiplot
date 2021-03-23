import functools

import colored as _colored


def centering_indentation_len(*lengths: int) -> int:
    return functools.reduce(lambda a, b: a - b, map(lambda length: length // 2, lengths))


# ---------------
# Coloring
# ---------------
RESET_COLOR: str = _colored.style.RESET


def colored(string: str, color: str) -> str:
    return _colored.fg(_colored.colors.names.index(color)) + string + RESET_COLOR

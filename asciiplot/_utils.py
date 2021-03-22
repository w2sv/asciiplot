import functools

import colored as _colored


def centering_indentation_len(*lengths: int) -> int:
    return functools.reduce(lambda a, b: a - b, map(lambda length: length // 2, lengths))


RESET_COLOR: str = _colored.style.RESET


def colored(string: str, color: str) -> str:
    return getattr(_colored.fore, color) + string + RESET_COLOR

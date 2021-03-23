import functools


def centering_indentation_len(*lengths: int) -> int:
    return functools.reduce(lambda a, b: a - b, map(lambda length: length // 2, lengths))

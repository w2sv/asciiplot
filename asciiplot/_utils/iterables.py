from typing import Iterable, Sequence


def max_element_length(sequences: Iterable[Sequence]) -> int:
    return max(map(len, sequences))
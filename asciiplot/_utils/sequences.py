from typing import Iterable

from asciiplot._utils.type_aliases import PlotSequence


def max_sequence_length(sequences: Iterable[PlotSequence]) -> int:
    return max(map(len, sequences))
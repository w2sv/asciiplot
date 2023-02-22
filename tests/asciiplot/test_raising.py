import pytest

from asciiplot import asciiize
from asciiplot._coloring import Color


def test_raising_on_too_many_colors(sequences):
    SEQUENCE_COLORS = [Color.AQUAMARINE_1A, Color.DARK_VIOLET_1A, Color.RED]

    with pytest.raises(ValueError):
        asciiize(*sequences[:-1], sequence_colors=SEQUENCE_COLORS)

    asciiize(*sequences, sequence_colors=SEQUENCE_COLORS)


def test_raising_on_passing_XOR_arguments():
    with pytest.raises(ValueError):
        asciiize([1, 77], center_horizontally=True, indentation=6)
    asciiize([1, 77], center_horizontally=True)
    asciiize([1, 77], indentation=6)

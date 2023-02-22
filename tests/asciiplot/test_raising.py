import pytest

from asciiplot import asciiize
from asciiplot._coloring import Color
from asciiplot._utils.console import console_width


def test_raising_on_too_many_colors(sequences):
    SEQUENCE_COLORS = [Color.AQUAMARINE_1A, Color.DARK_VIOLET_1A, Color.RED]

    with pytest.raises(ValueError):
        asciiize(*sequences[:-1], sequence_colors=SEQUENCE_COLORS)

    asciiize(*sequences, sequence_colors=SEQUENCE_COLORS)

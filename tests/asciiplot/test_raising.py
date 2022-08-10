import pytest

from asciiplot import asciiize
from asciiplot._coloring import Color
from asciiplot._utils.console import console_width


def test_raising_on_too_many_colors(sequences):
    SEQUENCE_COLORS = [Color.AQUAMARINE_1A, Color.DARK_VIOLET_1A, Color.RED]

    with pytest.raises(ValueError):
        asciiize(*sequences[:-1], sequence_colors=SEQUENCE_COLORS)

    asciiize(*sequences, sequence_colors=SEQUENCE_COLORS)


def test_raising_on_terminal_columns_exceeded(sequences):
    n_terminal_columns = console_width()

    with pytest.raises(ValueError):
        asciiize(*sequences, horizontal_indentation=int(n_terminal_columns * 1.5))

    asciiize(*sequences, horizontal_indentation=int(n_terminal_columns * 0.8))


def test_raising_on_indentation_and_chart_centering_set(sequences):
    with pytest.raises(ValueError):
        asciiize(*sequences, horizontal_indentation=5, center_horizontally=True)

    asciiize(*sequences, center_horizontally=True)
    asciiize(*sequences, horizontal_indentation=5)
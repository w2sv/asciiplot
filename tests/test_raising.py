import pytest

from asciiplot import asciiize
from asciiplot._utils import terminal_columns
from asciiplot._coloring import Color

SEQUENCES = [
    [4, 6, 3],
    [5, 5, 5],
    [8, 3]
]


def test_too_many_colors_exception_raising():
    SEQUENCE_COLORS = [Color.AQUAMARINE_1A, Color.DARK_VIOLET_1A, Color.RED]

    with pytest.raises(ValueError):
        asciiize(*SEQUENCES[:-1], sequence_colors=SEQUENCE_COLORS)

    asciiize(*SEQUENCES, sequence_colors=SEQUENCE_COLORS)


def test_terminal_columns_exceeded_exception():
    n_terminal_columns = terminal_columns()

    with pytest.raises(ValueError):
        asciiize(*SEQUENCES, indentation=int(n_terminal_columns * 1.5))

    asciiize(*SEQUENCES, indentation=int(n_terminal_columns * 0.8))


def test_xlabels_exceeding_domain_of_definition_length_raising():
    with pytest.raises(ValueError):
        asciiize(*SEQUENCES, x_ticks=list(range(4)), inter_points_margin=5)

    asciiize(*SEQUENCES, x_ticks=list(range(3)), inter_points_margin=5)


def test_indentation_and_chart_centering_set_raising():
    with pytest.raises(ValueError):
        asciiize(*SEQUENCES, indentation=5, center=True)

    asciiize(*SEQUENCES, center=True)
    asciiize(*SEQUENCES, indentation=5)

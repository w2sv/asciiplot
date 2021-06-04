import pytest

from asciiplot import asciiize
from asciiplot._utils import terminal_columns, coloring


SEQUENCES = [
    [4, 6, 3],
    [5, 5, 5],
    [8, 3]
]


def test_too_many_colors_exception_raising():
    SEQUENCE_COLORS = ['WHITE', 'RED', 'BLUE']

    with pytest.raises(ValueError):
        asciiize(*SEQUENCES[:-1], sequence_colors=SEQUENCE_COLORS)

    asciiize(*SEQUENCES, sequence_colors=SEQUENCE_COLORS)


def test_terminal_columns_exceeded_exception():
    n_terminal_columns = terminal_columns()

    with pytest.raises(ValueError):
        asciiize(*SEQUENCES, chart_indentation=int(n_terminal_columns * 1.5))

    asciiize(*SEQUENCES, chart_indentation=int(n_terminal_columns * 0.8))


def test_color_unavailability_raising():
    with pytest.raises(ValueError):
        coloring.colored('haycaramba', 'PINKISH_BLUE_MUSTARD')

    coloring.colored('haycaramba', 'BLUE')


def test_xlabels_exceeding_domain_of_definition_length_raising():
    with pytest.raises(ValueError):
        asciiize(*SEQUENCES, x_labels=list(range(4)), in_between_points_margin=5)

    asciiize(*SEQUENCES, x_labels=list(range(3)), in_between_points_margin=5)

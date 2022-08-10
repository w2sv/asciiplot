import itertools as itt
from typing import List, Optional

import more_itertools

from asciiplot._coloring import Color, colored
from asciiplot._type_aliases import TickLabelValue, TickLabelValues
from asciiplot._utils.formatting import indented


def x_axis_tick_label_row(x_axis_tick_labels: TickLabelValues,
                          tick_color: Color,
                          bg: Color,
                          horizontal_y_axis_offset: int,
                          inter_points_margin: int) -> str:

    """ Returns:
            x-label-row indented according to chart_indentation """

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create labels objects
    ticks: List[_XAxisTickLabel] = list(
        map(
            lambda label: _XAxisTickLabel(label, color=tick_color),
            x_axis_tick_labels
        )
    )

    return indented(
        _tick_row(ticks, inter_points_margin=inter_points_margin, bg=bg),
        columns=(horizontal_y_axis_offset - ticks[0].left_margin_length)
    )


class _XAxisTickLabel(str):
    """ Serving the creation of helper objects facilitating the computation
    of whitespace sequences in between labels """

    def __new__(cls, content: Optional[TickLabelValue], color: Optional[Color] = None):
        if content is None:
            content = ' '
        elif color:
            content = colored(content, color)
        return super().__new__(cls, content)

    def __init__(self, content: Optional[TickLabelValue], color: Optional[Color] = None):
        """ Initialize such that center of serialized label right beneath tick
        in case of odd string length, otherwise shift by one column towards the right

        >>> margin_lengths = lambda label: [label.left_margin_length, label.right_margin_length]
        >>> margin_lengths(_XAxisTickLabel(234))
        [1, 1]
        >>> margin_lengths(_XAxisTickLabel(23))
        [0, 1]
        >>> margin_lengths(_XAxisTickLabel(2))
        [0, 0]
        >>> margin_lengths(_XAxisTickLabel('second'))
        [2, 3] """

        if content is not None:
            content_str = str(content)
            floored_halved_length = len(content_str) // 2
            self.left_margin_length = floored_halved_length - int(not len(content_str) % 2)
            self.right_margin_length = floored_halved_length
        else:
            self.left_margin_length = self.right_margin_length = 0

    def whitespace_succeeded(self, succeeding_tick, inter_points_margin: int, bg: Color) -> str:
        n_whitespaces = inter_points_margin - self.right_margin_length - succeeding_tick.left_margin_length
        if n_whitespaces < 0 and str(self) != ' ':
            raise ValueError(f'Adjacent x-axis tick labels {self} and {succeeding_tick} are overlapping')

        return colored(self, bg=bg) + colored(" ".rjust(n_whitespaces) if n_whitespaces else '', bg=bg)


def _tick_row(ticks: List[_XAxisTickLabel], inter_points_margin: int, bg: Color) -> str:
    """
    >>> _tick_row(list(map(_XAxisTickLabel, ['great', 'cool', 'splendid', 'sick'])), inter_points_margin=6, bg=Color.NONE)
    'great   cool splendid sick'
    >>> _tick_row(list(map(_XAxisTickLabel, ['first', 'second', 'third', 'fourth'])), inter_points_margin=8, bg=Color.NONE)
    'first    second   third    fourth'
    >>> _tick_row(list(map(_XAxisTickLabel, range(9, 14))), inter_points_margin=3, bg=Color.NONE)
    '9   10  11  12  13'
    >>> _tick_row(list(map(_XAxisTickLabel, range(4))), inter_points_margin=0, bg=Color.NONE)
    '0123' """

    return ''.join(
        itt.starmap(
            lambda a, b: a.whitespace_succeeded(b, inter_points_margin=inter_points_margin, bg=bg),
            more_itertools.pairwise(ticks)
        )
    ) + colored(ticks[-1], bg=bg)
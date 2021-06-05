import itertools as itt
from typing import List, Optional, Union

import more_itertools

from asciiplot._config import Ticks
from asciiplot._utils import indented
from asciiplot._coloring import colored, Color


def render(
        x_axis_ticks: Ticks,
        tick_color: Color,
        horizontal_y_axis_offset: int,
        inter_points_margin: int) -> str:

    """ Returns:
            x-label-row indented according to chart_indentation """

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create labels objects
    ticks: List[_XAxisTickLabel] = list(
        map(
            lambda label: _XAxisTickLabel(label, color=tick_color),
            x_axis_ticks
        )
    )

    return indented(
        _tick_row(ticks, inter_points_margin=inter_points_margin),
        columns=(horizontal_y_axis_offset - ticks[0].left_margin_length)
    )


class _XAxisTickLabel(str):
    """ Serving the creation of helper objects facilitating the computation
    of whitespace sequences in between labels """

    def __new__(cls, content: Optional[Union[str, float]], color: Optional[Color] = None):
        if not content:
            content = ' '
        elif color:
            content = colored(content, color)

        return super().__new__(cls, content)

    def __init__(self, content: Optional[Union[str, float]], color: Optional[Color] = None):
        """ Initialize such that center of serialized label right beneath tick
        in case of odd string length, otherwise shift by one column towards the right

        >>> _XAxisTickLabel(234).margin_lengths
        [1, 1]
        >>> _XAxisTickLabel(23).margin_lengths
        [0, 1]
        >>> _XAxisTickLabel(2).margin_lengths
        [0, 0]
        >>> _XAxisTickLabel('second').margin_lengths
        [2, 3] """

        if content is not None:
            content_str = str(content)
            is_of_even_length: bool = len(content_str) % 2 == 0
            self.left_margin_length = len(content_str) // 2 - int(is_of_even_length)
            self.right_margin_length = self.left_margin_length + int(is_of_even_length)
        else:
            self.left_margin_length = self.right_margin_length = 0

    @property
    def margin_lengths(self) -> List[int]:
        return [self.left_margin_length, self.right_margin_length]

    def whitespace_succeeded(self, succeeding_tick, inter_points_margin: int) -> str:
        n_whitespaces = inter_points_margin - self.right_margin_length - succeeding_tick.left_margin_length
        if n_whitespaces < 0 and str(self) != ' ':
            raise ValueError(f'Adjacent x-axis ticks {self} and {succeeding_tick} are overlapping')

        return f'{self}{" ".rjust(n_whitespaces)}'


def _tick_row(ticks: List[_XAxisTickLabel], inter_points_margin: int) -> str:
    """
    >>> _tick_row(list(map(_XAxisTickLabel, ['great', 'cool', 'splendid', 'sick'])), inter_points_margin=6)
    'great   cool splendid sick'
    >>> _tick_row(list(map(_XAxisTickLabel, ['first', 'second', 'third', 'fourth'])), inter_points_margin=8)
    'first    second   third    fourth'
    >>> _tick_row(list(map(_XAxisTickLabel, range(9, 14))), inter_points_margin=3)
    '9   10  11  12  13' """

    return ''.join(
        itt.starmap(
            lambda a, b: a.whitespace_succeeded(b, inter_points_margin=inter_points_margin),
            more_itertools.pairwise(ticks)
        )
    ) + ticks[-1]

from typing import List, Union, Optional, Dict, Tuple
import re
import more_itertools
import itertools as itt

from asciiplot._utils import types
from asciiplot._utils.coloring import colored, RESET
from asciiplot._variable_encapsulations._config import Config
from asciiplot._variable_encapsulations._params import Params


# -----------------
# Y-Axis with Labels
# -----------------
def y_axis_comprising_chart(chart: types.ChartGrid, config: Config, params: Params) -> types.ChartGrid:
    """ Returns:
            y-axis comprising chart grid """

    SEGMENT_REPLACEMENTS = {
        '─': '┤',
        '|': '┼'
    }

    for i in range(config.chart_height):
        parcel = chart[i][0]
        if parcel == ' ':
            chart[i][0] = '┤'
        else:
            chart[i][0] = _segment_replaced_parcel(parcel, segment_replacements=SEGMENT_REPLACEMENTS)

    return [[colored(label.rjust(params.n_label_column_columns), config.label_color)] + row for label, row in zip(params.y_labels, chart)]


# -----------------
# X-Axis
# -----------------
def x_axis_comprising_chart(chart: types.ChartGrid, config: Config) -> types.ChartGrid:
    """ Adds x-axis to chart """

    SEGMENTS = ('┼', '┤', '┬', '─')
    SEGMENT_REPLACEMENTS = {
        '┤': '┼',
        '─': '┬',
        '╰': '├',
        '╯': '┤'
    }

    def is_data_point(point_index: int) -> bool:
        """ Returns:
                flag whether or not point corresponding to point_index is actual
                data point denoted in original sequences instead of interpolated
                one """

        return not point_index % (config.in_between_points_margin + 1)

    last_row = chart[-1]

    if not _extract_parcel_elements(last_row[0])[0]:
        last_row[0] = SEGMENTS[0]

    for i, parcel in enumerate(last_row):
        # add straight horizontal axis segment if parcel doesn't contain
        # a sequence segment, otherwise convert present sequence segment
        # to one comprising both the sequence and axis segment in color
        # of respective sequence

        _is_data_point = is_data_point(i)
        if parcel == ' ':
            last_row[i] = SEGMENTS[[3, 2][_is_data_point]]
        elif _is_data_point:
            last_row[i] = _segment_replaced_parcel(parcel, SEGMENT_REPLACEMENTS)

    return chart


def _segment_replaced_parcel(parcel: str, segment_replacements: Dict[str, str]) -> str:
    """ Returns:
            segment replaced parcel containing eventually present, original ansi color

        >>> SEGMENT_REPLACEMENTS = {'┤': '┼'}

        >>> _segment_replaced_parcel('┤', SEGMENT_REPLACEMENTS)
        '┼'
        >>> print(_segment_replaced_parcel(f'\x1b[36m┤\x1b[0m', SEGMENT_REPLACEMENTS))
        \x1b[36m┼\x1b[0m """

    color, element = _extract_parcel_elements(parcel)
    new_element = segment_replacements.get(element, element)

    if color:
        return color + new_element + RESET
    return new_element


_ANSI_ESCAPE_PATTERN = re.compile(r'\x1b[^m]*m')


def _extract_parcel_elements(parcel: str) -> Tuple[Optional[str], str]:
    """ Returns:
            Tuple[
                ansicolor if present else None,
                sequence segment
            ]

    >>> ansi_color, segment = _extract_parcel_elements(parcel='\x1b[36m-\x1b[0m')
    >>> print(ansi_color)
    \x1b[36m
    >>> segment
    '-'

    >>> _extract_parcel_elements(parcel='┤')
    (None, '┤') """

    ansi_sequences = re.findall(_ANSI_ESCAPE_PATTERN, parcel)
    if len(ansi_sequences):
        return ansi_sequences[0], parcel[len(ansi_sequences[0]):-len(RESET)]
    return None, parcel


# -----------------
# X-Axis Labels
# -----------------
def x_axis_ticks_row(config: Config, params: Params) -> str:
    """ Returns:
            x-label-row indented according to chart_indentation """

    assert config.x_labels is not None

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create labels objects
    ticks: List[_XAxisTickLabel] = list(
        map(
            lambda label: _XAxisTickLabel(label, color=config.label_color),
            config.x_labels
        )
    )

    return f'{" " * (params.horizontal_y_axis_offset - ticks[0].left_margin_length)}' \
           f'{_tick_row(ticks, inter_points_margin=config.in_between_points_margin)}'


class _XAxisTickLabel(str):
    """ Serving the creation of helper objects facilitating the computation
    of whitespace sequences in between labels """

    def __new__(cls, content: Optional[Union[str, float]], color: Optional[str] = None):
        if not content:
            content = ' '
        elif color:
            content = colored(content, color)

        return super().__new__(cls, content)

    def __init__(self, content: Optional[Union[str, float]], color: Optional[str] = None):
        """ Initialize such that center of sequentialized label right beneath tick
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

        return f'{self}{" " * n_whitespaces}'


def _tick_row(ticks: List[_XAxisTickLabel], inter_points_margin: int) -> str:
    """
    >>> _tick_row(list(map(_XAxisTickLabel, ['great', 'cool', 'splendid', 'sick'])), inter_points_margin=6)
    'great   cool splendid sick' """

    return ''.join(
        itt.starmap(
            lambda a, b: a.whitespace_succeeded(b, inter_points_margin=inter_points_margin),
            more_itertools.pairwise(ticks)
        )
    ) + ticks[-1]

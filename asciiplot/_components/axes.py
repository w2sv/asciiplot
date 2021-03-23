from typing import List, Union, Optional, Dict, Tuple
import re

from asciiplot._utils import types
from asciiplot._utils.coloring import colored, RESET_COLOR
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

    for i in range(config.n_plot_rows):
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

    SEGMENTS = ['┼', '┤', '┬', '─']
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

        return point_index % (config.columns_between_points + 1) == 0

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
    color, element = _extract_parcel_elements(parcel)
    new_element = segment_replacements.get(element, element)

    if color:
        return color + new_element + RESET_COLOR
    return new_element


_ANSI_ESCAPE_PATTERN = re.compile(r'\x1b[^m]*m')


def _extract_parcel_elements(parcel: str) -> Tuple[Optional[str], str]:
    """ Returns:
            Tuple[
                ansicolor if present else None,
                sequence segment
            ]

    >>> _extract_parcel_elements(parcel=f'\x1b[36m-{RESET_COLOR}')
    ('\x1b[36m', '-')
    >>> _extract_parcel_elements(parcel='┤')
    (None, '┤') """

    ansi_sequences = re.findall(_ANSI_ESCAPE_PATTERN, parcel)
    if len(ansi_sequences):
        return ansi_sequences[0], parcel[len(ansi_sequences[0]):-len(RESET_COLOR)]
    return None, parcel


# -----------------
# X-Axis Labels
# -----------------
class _Label:
    """ Serving the creation of helper objects facilitating the computation
    of whitespace sequences in between labels """

    def __init__(self, description: Optional[Union[str, int]], color: Optional[str] = None):
        """ Initialize such that center of sequentialized label right beneath tick
        in case of odd string length, otherwise shift by one column towards the right

        >>> _Label(234).__dict__
        {'negative_protrusion': 1, 'positive_protrusion': 1, 'label': '234'}
        >>> _Label(23).__dict__
        {'negative_protrusion': 0, 'positive_protrusion': 1, 'label': '23'}
        >>> _Label(2).__dict__
        {'negative_protrusion': 0, 'positive_protrusion': 0, 'label': '2'} """

        self.label: str
        self.negative_protrusion: int  # n columns occupied towards the left starting from tick column
        self.positive_protrusion: int  # n columns occupied towards the right starting from tick column

        if description is not None:
            label = str(description)
            is_of_even_length: bool = len(label) % 2 == 0
            self.negative_protrusion = len(label) // 2 - int(is_of_even_length)
            self.positive_protrusion = self.negative_protrusion + int(is_of_even_length)
            self.label = colored(label, color) if color else label
        else:
            self.label = ' '
            self.negative_protrusion = self.positive_protrusion = 0


def x_label_row(config: Config, params: Params) -> str:
    """ Returns:
            x-label-row indented according to label_column_offset """

    assert config.x_labels is not None

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create labels objects
    labels: List[_Label] = list(map(lambda label: _Label(label, color=config.label_color), config.x_labels))  # type: ignore

    def compute_n_whitespaces(preceding_tick: _Label, tick: _Label, tick_index: int) -> int:
        n = config.columns_between_points - preceding_tick.positive_protrusion - tick.negative_protrusion
        if n < 0 and tick_index != len(labels) - 1 and tick.label != ' ':
            raise ValueError(f'Adjacent x-axis ticks {preceding_tick.label} and {tick.label} are overlapping')
        return n

    # add label_column_offset + first tick to label row
    label_row = labels[0].label

    # add consecutive ticks
    for i in range(1, len(labels)):
        n_whitespaces = compute_n_whitespaces(preceding_tick=labels[i-1], tick=labels[i], tick_index=i)
        label_row += f'{" " * n_whitespaces}{colored(labels[i].label, config.label_color)}'

    return ' ' * (params.horizontal_y_axis_offset - labels[0].negative_protrusion) + label_row


if __name__ == '__main__':
    print(_Label('twa'))
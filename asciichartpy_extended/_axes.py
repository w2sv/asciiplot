from typing import List, Union, Optional
import re
import dataclasses

from asciichartpy_extended._types import _ChartGrid
from asciichartpy_extended._config import Config
from asciichartpy_extended._params import _Params
from asciichartpy_extended import colors


def _y_axis_comprising_chart(chart: _ChartGrid, config: Config, params: _Params) -> _ChartGrid:
    """ Returns:
            y-axis comprising chart grid """

    SEGMENT_REPLACEMENTS = {
        '─': '┤',
        '|': '┼'
    }

    for i in range(config.plot_height + 1):
        if (parcel := chart[i][0]) == ' ':
            chart[i][0] = '┤'
        else:
            chart[i][0] = extract_color(parcel) + SEGMENT_REPLACEMENTS.get(colorless_segment(parcel), parcel) + colors.RESET

    return [[label.rjust(params.label_columns)] + row for label, row in zip(params.labels, chart)]


def _add_x_axis(chart: _ChartGrid, config: Config):
    """ Adds x-axis to chart """

    SEGMENTS = ['┼', '┤', '┬', '─']
    SEGMENT_2_X_AXIS_TOUCHING_SUBSTITUTE = {
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

    if not extract_color(last_row[0]):
        last_row[0] = SEGMENTS[0]

    for i, parcel in enumerate(last_row):
        # add straight horizontal axis segment if parcel doesn't contain
        # a sequence segment, otherwise convert present sequence segment
        # to one comprising both the sequence and axis segment in color
        # of respective sequence

        _is_data_point = is_data_point(i)
        if parcel == ' ':
            if _is_data_point:
                last_row[i] = SEGMENTS[2]
            else:
                last_row[i] = SEGMENTS[3]
        elif _is_data_point:
            if color := extract_color(parcel):
                parcel = colorless_segment(parcel)

            last_row[i] = color + SEGMENT_2_X_AXIS_TOUCHING_SUBSTITUTE.get(parcel, parcel) + colors.RESET


_ANSI_ESCAPE_PATTERN = re.compile(r'\x1b[^m]*m')

def extract_color(parcel: str) -> str:
    """
    >>> extract_color(parcel='\033[30m-\033[0m')
    '\033[30m'
    >>> extract_color(parcel='┤')
      """

    if len((ansi_sequences := re.findall(_ANSI_ESCAPE_PATTERN, parcel))):
        return ansi_sequences[0]
    return ''


def colorless_segment(parcel: str):
    """ Assumes color presence

    >>> colorless_segment(parcel='\033[30m-\033[0m')
    '-' """

    return re.split(_ANSI_ESCAPE_PATTERN, parcel)[1]


@dataclasses.dataclass
class _Tick:
    """ Serving the creation of helper objects facilitating the computation
    of whitespace sequences in between ticks """

    label: str
    negative_protrusion: int  # n columns occupied towards the left starting from tick column
    positive_protrusion: int  # n columns occupied towards the right starting from tick column

    def __init__(self, label: Optional[Union[str, int]]):
        """ Initialize such that center of sequentialized label right beneath tick
        in case of odd string length, otherwise shift by one column towards the right

        >>> tick = _Tick(234)
        tick(label='234', negative_protrusion=1, positive_protrusion=1)
        >>> tick = _Tick(23)
        tick(label='23', negative_protrusion=0, positive_protrusion=1)
        >>> tick = _Tick(2)
        tick(label='234', negative_protrusion=0, positive_protrusion=0) """

        self.label: str
        self.negative_protrusion: int
        self.positive_protrusion: int

        if label:
            self.label = str(label)
            is_of_even_length: bool = len(self.label) % 2 == 0
            self.negative_protrusion: int = len(self.label) // 2 - int(is_of_even_length)
            self.positive_protrusion: int = self.negative_protrusion + int(is_of_even_length)
        else:
            self.label = ' '
            self.negative_protrusion = self.positive_protrusion = 0

def _x_label_row(config: Config, params: _Params) -> str:
    """ Returns:
            x-label-row indented according to label_column_offset """

    assert config.x_labels is not None

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create tick objects
    padded_label_sequence = [config.x_labels.get(i) for i in range(params.definition_area_magnitude)]
    ticks: List[_Tick] = list(map(_Tick, padded_label_sequence))  # type: ignore

    # add label_column_offset + first tick to label row
    label_row = ticks[0].label

    # add consecutive ticks
    for i in range(1, len(ticks)):
        n_whitespaces = config.columns_between_points - ticks[i - 1].positive_protrusion - ticks[i].negative_protrusion
        assert n_whitespaces >= 1
        label_row += f'{" " * n_whitespaces}{ticks[i].label}'

    return ' ' * (params.horizontal_y_axis_offset - ticks[0].negative_protrusion) + label_row


if __name__ == '__main__':
    print(_Tick('twa'))
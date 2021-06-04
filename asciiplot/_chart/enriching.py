from typing import *
import itertools as itt

import more_itertools

from asciiplot._utils import (
    indented,
    colored,
    centering_indentation_len,
    newlined
)
from asciiplot._config import Config
from asciiplot._chart import ChartGrid


def enriched(serialized_chart: str, config: Config, chart_params: ChartGrid.Params) -> str:
    if config.x_axis_description:
        serialized_chart += f' {config.axis_description(x_axis=True)}'
    serialized_chart = newlined(serialized_chart)

    if config.y_axis_description:
        serialized_chart = f'{newlined(indented(config.axis_description(x_axis=False), columns=centering_indentation_len(len(config.y_axis_description), chart_params.columns_to_y_axis_ticks * 2)))}' \
                           f'{serialized_chart}'
    if config.title:
        serialized_chart = _title_header(
            config.title,
            config.title_color,
            chart_params.width,
            chart_params.columns_to_y_axis_ticks
        ) + serialized_chart
    if config.x_labels:
        serialized_chart = serialized_chart + x_axis_ticks_row(
            config.x_labels,
            config.label_color,
            chart_params.columns_to_y_axis_ticks,
            config.inter_points_margin
        )

    return serialized_chart


def _title_header(title: str, title_color: str, chart_width: int, horizontal_y_axis_offset: int) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    return f'{indented(colored(title, title_color), columns=(centering_indentation_len(len(title), reference_length=chart_width) + horizontal_y_axis_offset))}\n'


def x_axis_ticks_row(x_labels, label_color: str, horizontal_y_axis_offset: int, inter_points_margin: int) -> str:
    """ Returns:
            x-label-row indented according to chart_indentation """

    # provide label sequences containing empty strings as labels for ticks,
    # for which none were given and create labels objects
    ticks: List[_XAxisTickLabel] = list(
        map(
            lambda label: _XAxisTickLabel(label, color=label_color),
            x_labels
        )
    )

    return indented(
        _tick_row(ticks, inter_points_margin=inter_points_margin),
        columns=(horizontal_y_axis_offset - ticks[0].left_margin_length)
    )


# -----------------
# X-Axis Labels
# -----------------
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

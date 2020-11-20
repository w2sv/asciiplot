from __future__ import annotations
from typing import *
import math
from functools import partial

from asciichartpy_extended._types import _Sequences, _Chart
from asciichartpy_extended._axes import _add_x_axis, _add_y_axis, _x_label_row
from asciichartpy_extended._config import Config
from asciichartpy_extended._params import _Params
from asciichartpy_extended import colors


def render_chart(*sequences: List[float], config=Config()) -> str:
    sequences = config.process(sequences)
    params = _Params(sequences, config)

    # create serialized chart
    serialized_chart = _serialize_chart(chart=_render_chart(sequences, config, params))

    # add desired chart ornaments
    if config.title:
        serialized_chart = _title_header(config, params) + serialized_chart
    if config.x_labels:
        serialized_chart = serialized_chart + _x_label_row(config)

    return serialized_chart


def _serialize_chart(chart: _Chart) -> str:
    return '\n'.join([''.join(row).rstrip() for row in chart]) + '\n'


def _render_chart(sequences: _Sequences, config: Config, params: _Params) -> _Chart:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.chart_width for _ in range(params.n_rows + 1)]
    _add_y_axis(chart, config, params)
    last_row_indices = _add_sequences(sequences, chart, config, params)

    if config.display_x_axis:
        _add_x_axis(chart, config, last_row_indices)

    return chart


def _add_sequences(sequences: _Sequences, chart: _Chart, config: Config, params: _Params) -> List[int]:
    """ Adds ascii-ized sequences to chart

        Returns:
            last_column_occupying_segment_row_indices: List[int], row indices of sequence ends occupying
                the last chart column """

    SEGMENTS = ['┼', '─', '╰', '╭', '╮', '╯', '│']
    INIT_VALUE = -1

    scaled = partial(_scaled,
                     desired_minimum=config.min,
                     desired_maximum=config.max,
                     actual_minimum=params.min,
                     delta_y=config.delta_y)

    last_column_occupying_segment_row_indices: List[int] = []
    for i, sequence in enumerate(sequences):
        color = config.sequence_colors[i % len(config.sequence_colors)]

        # add '┼' at sequence beginning where sequences overlaps with y-axis
        if math.isfinite(sequence[0]):
            chart[params.n_rows - scaled(sequence[0])][config.offset - 1] = _colored(SEGMENTS[0], color)

        # ascii-ize sequence
        j = INIT_VALUE
        y0, y1 = INIT_VALUE, INIT_VALUE
        while (j := j + 1) < len(sequence) - 1:

            def set_parcel(row_subtrahend: int, segment: str):
                chart[params.n_rows - row_subtrahend][j + config.offset] = _colored(segment, color)

            y0 = scaled(sequence[j])
            y1 = scaled(sequence[j + 1])

            if y0 == y1:
                set_parcel(y0, SEGMENTS[1])

            else:
                if y0 > y1:
                    symbol_y0, symbol_y1 = SEGMENTS[4], SEGMENTS[2]
                else:
                    symbol_y0, symbol_y1 = SEGMENTS[5], SEGMENTS[3]

                set_parcel(y0, symbol_y0)
                set_parcel(y1, symbol_y1)

                # add vertical segmentation in case of consecutive sequence
                # value steepness
                for y in range(min(y0, y1) + 1, max(y0, y1)):
                    chart[params.n_rows - y][j + config.offset] = _colored(SEGMENTS[6], color)

        # add row index of last added segment to last_column_occupying_segment_row_indices
        # if segment end occupies last chart column
        if j + 1 + config.offset == params.chart_width:
            last_column_occupying_segment_row_indices.append([min, max][y1 > y0](y0, y1))

    return last_column_occupying_segment_row_indices


def _scaled(value: float,
            desired_minimum: float,
            desired_maximum: float,
            actual_minimum: float,
            delta_y: float) -> int:
    """ Scales sequence point clamped to desired extrema to
    corresponding point within chart value range """

    clamped_value = min(max(value, desired_minimum), desired_maximum)
    return int(round(clamped_value * delta_y) - actual_minimum)


def _colored(string: str, color: str) -> str:
    return color + string + colors.RESET


def _title_header(config: Config, params: _Params) -> str:
    """ Returns:
            title header indented by offset with successive newline """

    assert config.title is not None
    return ' ' * (config.offset + params.plot_width // 2 + len(config.title) // 2) + config.title + '\n'

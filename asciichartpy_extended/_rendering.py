from __future__ import annotations
from typing import *

from asciichartpy_extended._sequences import _add_sequences, _padded_sequences
from asciichartpy_extended._types import _Sequences, _Chart
from asciichartpy_extended._axes import _add_x_axis, _y_axis_comprising_chart, _x_label_row
from asciichartpy_extended._config import Config
from asciichartpy_extended._params import _Params


def render_chart(*sequences: List[float], config=Config()) -> str:
    if config.columns_between_points:
        sequences = _padded_sequences(sequences, config.columns_between_points)

    params = _Params(sequences, config)

    chart_grid = _render_chart_grid(sequences, config, params)

    if config.x_axis_description:
        chart_grid[-1] += [' ' + config.x_axis_description]

    serialized_chart = _serialize_chart(chart=chart_grid)

    # add desired chart ornaments
    if config.y_axis_description:
        description_row = ' ' * (params.horizontal_y_axis_offset - len(config.y_axis_description) // 2) + config.y_axis_description + '\n'
        serialized_chart = description_row + serialized_chart
    if config.title:
        serialized_chart = _title_header(config, params) + serialized_chart
    if config.x_labels:
        serialized_chart = serialized_chart + _x_label_row(config, params)

    return serialized_chart


def _render_chart_grid(sequences: _Sequences, config: Config, params: _Params) -> _Chart:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.definition_area_magnitude for _ in range(config.height + 1)]

    _add_sequences(sequences, chart, config, params)

    if config.display_x_axis:
        _add_x_axis(chart, config)

    chart = _y_axis_comprising_chart(chart, config, params)

    if config.offset:
        indentation = ' ' * config.offset
        chart = [[indentation] + row for row in chart]

    return chart


def _serialize_chart(chart: _Chart) -> str:
    return '\n'.join([''.join(row).rstrip() for row in chart]) + '\n'


def _title_header(config: Config, params: _Params) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    assert config.title is not None
    return ' ' * ((params.definition_area_magnitude // 2) + params.horizontal_y_axis_offset - len(config.title) // 2) + config.title + '\n'

from __future__ import annotations
from typing import List

from asciichartpy_extended._components._sequences import _add_sequences, _stretched_sequences
from asciichartpy_extended._components._axes import _add_x_axis, _y_axis_comprising_chart, _x_label_row
from asciichartpy_extended._types import _Sequences, _ChartGrid
from asciichartpy_extended._variable_encapsulations import Config, _Params
from asciichartpy_extended._coloring import _colored


def asciiize(*sequences: List[float], config=Config()) -> str:
    definition_area_magnitude = max(map(len, sequences))

    # stretch sequences if desired
    if config.columns_between_points:
        sequences = _stretched_sequences(sequences, config.columns_between_points)  # type: ignore

    # calculate params, render chart grid
    params = _Params(sequences, config, definition_area_magnitude)
    chart_grid = _render_chart_grid(sequences, config, params)

    # add x axis description if desired
    if config.x_axis_description:
        chart_grid[-1] += [' ' + _colored(config.x_axis_description, config.axis_description_color)]

    # serialize chart
    serialized_chart = _serialize_chart(chart=chart_grid)

    # add desired chart ornaments
    if config.y_axis_description:
        description_row = ' ' * (params.horizontal_y_axis_offset - len(config.y_axis_description) // 2) + _colored(config.y_axis_description, config.axis_description_color) + '\n'
        serialized_chart = description_row + serialized_chart
    if config.title:
        serialized_chart = _title_header(config, params) + serialized_chart
    if config.x_labels:
        serialized_chart = serialized_chart + _x_label_row(config, params)

    return serialized_chart


def _render_chart_grid(sequences: _Sequences, config: Config, params: _Params) -> _ChartGrid:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.plot_width for _ in range(config.plot_height + 1)]

    _add_sequences(sequences, chart, config, params)

    if config.display_x_axis:
        _add_x_axis(chart, config)

    chart = _y_axis_comprising_chart(chart, config, params)

    if config.label_column_offset:
        indentation = ' ' * config.label_column_offset
        chart = [[indentation] + row for row in chart]

    return chart


def _serialize_chart(chart: _ChartGrid) -> str:
    return '\n'.join([''.join(row).rstrip() for row in chart]) + '\n'


def _title_header(config: Config, params: _Params) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    assert config.title is not None
    return ' ' * ((params.plot_width // 2) + params.horizontal_y_axis_offset - len(config.title) // 2) + config.title + '\n'

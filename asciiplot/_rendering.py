from typing import List

import shutil

from asciiplot._utils import colored, centering_indentation_len
from asciiplot._types import _Sequences, _ChartGrid
from asciiplot._components._sequences import _add_sequences, _stretched_sequences
from asciiplot._components._axes import _add_x_axis, _y_axis_comprising_chart, _x_label_row
from asciiplot._variable_encapsulations import Config, _Params


_n_terminal_columns = shutil.get_terminal_size().columns


def asciiize(*sequences: List[float], config=Config()) -> str:
    domain_of_definition_length: int = max(map(len, sequences))

    # raise Value Error if received more x-labels than there are x-values
    if len(config.x_labels) > domain_of_definition_length:
        raise ValueError(f"X-labels aren't matching determined domain of definition. Passed sequences comprise "
                         f"{domain_of_definition_length} distinct x-values, passed {len(config.x_labels)} labels")

    # stretch sequences if desired
    if config.columns_between_points:
        sequences = _stretched_sequences(sequences, config.columns_between_points)  # type: ignore

    # calculate params, create chart grid
    params = _Params(sequences, config, domain_of_definition_length)
    raise_if_occupied_columns_exceeding_terminal_columns(params.total_width)

    chart_grid = _create_chart_grid(sequences, config, params)

    # add x axis description if desired
    if config.x_axis_description:
        chart_grid[-1] += [' ' + colored(config.x_axis_description, config.axis_description_color)]

    # center chart if desired
    if config.center_plot:
        n_whitespaces = centering_indentation_len(_n_terminal_columns, params.total_width)
        centering_margin = ' ' * n_whitespaces

        [row.insert(0, centering_margin) for row in chart_grid]
        params.horizontal_y_axis_offset += n_whitespaces

    # serialize chart
    serialized_chart = _serialize_chart(chart=chart_grid)

    # add desired chart ornaments
    if config.y_axis_description:
        description_row = ' ' * (params.horizontal_y_axis_offset - len(config.y_axis_description) // 2) + colored(config.y_axis_description, config.axis_description_color) + '\n'
        serialized_chart = description_row + serialized_chart
    if config.title:
        serialized_chart = _title_header(config, params) + serialized_chart
    if config.x_labels:
        serialized_chart = serialized_chart + _x_label_row(config, params)

    return serialized_chart


def raise_if_occupied_columns_exceeding_terminal_columns(occupied_columns: int):
    if occupied_columns > _n_terminal_columns:
        raise ValueError(
            f'Number of columns occupied by entire plot ({occupied_columns}) '
            f'exceeding number of terminal columns ({_n_terminal_columns})'
        )


def _create_chart_grid(sequences: _Sequences, config: Config, params: _Params) -> _ChartGrid:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.chart_width for _ in range(config.n_plot_rows)]

    _add_sequences(sequences, chart, config, params)

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
    return ' ' * (centering_indentation_len(params.chart_width, len(config.title)) + params.horizontal_y_axis_offset) + config.title + '\n'

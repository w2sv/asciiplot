from typing import List, Sequence, Optional, Union

import shutil

from asciiplot import _types
from asciiplot._utils.coloring import colored
from asciiplot._utils import centering_indentation_len
from asciiplot._components._sequences import add_sequences, stretched_sequences
from asciiplot._components._axes import add_x_axis, y_axis_comprising_chart, x_label_row
from asciiplot._variable_encapsulations import Config, Params


_n_terminal_columns = shutil.get_terminal_size().columns
_DEFAULT_COLOR = 'WHITE'


def asciiize(
        *sequences: List[float],
        n_plot_rows: int = 5,
        label_column_offset: int = 0,
        columns_between_points: int = 0,

        sequence_colors: Sequence[str] = (_DEFAULT_COLOR),
        axis_description_color: str = _DEFAULT_COLOR,
        label_color: str = _DEFAULT_COLOR,

        x_labels: Optional[Sequence[Optional[Union[str, float]]]] = None,
        x_axis_description: str = '',
        y_label_decimal_places: int = 1,
        y_axis_description: str = '',

        title: Optional[str] = None,
        title_color: _DEFAULT_COLOR,
        center_plot: bool = False) -> str:

    # raise Value Error if passed more sequence colors than sequences
    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of passed sequence colors exceeding number of sequences')

    # create config and compute params
    kwargs = locals().copy()
    del kwargs['sequences']

    config = Config(**kwargs)

    # stretch sequences if desired
    if config.columns_between_points:
        sequences = stretched_sequences(sequences, config.columns_between_points)  # type: ignore

    params = Params(sequences, config)

    # raise Value Error if received more x-labels than there are x-values
    if config.x_labels is not None and len(config.x_labels) > params.domain_of_definition_length:
        raise ValueError(f"X-labels aren't matching determined domain of definition. Passed sequences comprise "
                         f"{params.domain_of_definition_length} distinct x-values, passed {len(config.x_labels)} labels")

    # calculate params, create chart grid
    _raise_if_occupied_columns_exceeding_terminal_columns(params.total_width)

    chart_grid = _create_chart_grid(sequences, config, params)

    # add x axis description if desired
    if config.x_axis_description:
        chart_grid[-1] += [' ' + colored(config.x_axis_description, config.axis_description_color)]

    # center chart if desired
    if config.center_plot:
        n_whitespaces = centering_indentation_len(_n_terminal_columns, params.total_width)
        centering_margin = ' ' * n_whitespaces

        for row_i in range(len(chart_grid)):
            chart_grid[row_i].insert(0, centering_margin)

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
        serialized_chart = serialized_chart + x_label_row(config, params)

    return serialized_chart


def _raise_if_occupied_columns_exceeding_terminal_columns(occupied_columns: int):
    if occupied_columns > _n_terminal_columns:
        raise ValueError(
            f'Number of columns occupied by entire plot ({occupied_columns}) '
            f'exceeding number of terminal columns ({_n_terminal_columns})'
        )


def _create_chart_grid(sequences: _types.Sequences, config: Config, params: Params) -> _types.ChartGrid:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.chart_width for _ in range(config.n_plot_rows)]

    add_sequences(sequences, chart, config, params)

    add_x_axis(chart, config)

    chart = y_axis_comprising_chart(chart, config, params)

    if config.label_column_offset:
        indentation = ' ' * config.label_column_offset
        chart = [[indentation] + row for row in chart]

    return chart


def _serialize_chart(chart: _types.ChartGrid) -> str:
    return '\n'.join([''.join(row).rstrip() for row in chart]) + '\n'


def _title_header(config: Config, params: Params) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    assert config.title is not None
    return ' ' * (centering_indentation_len(params.chart_width, len(config.title)) + params.horizontal_y_axis_offset) + colored(config.title, config.title_color) + '\n'

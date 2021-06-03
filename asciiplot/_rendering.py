from typing import List, Sequence, Optional, Union

import shutil

from asciiplot._utils.coloring import colored
from asciiplot._utils import centering_indentation_len, types
from asciiplot._components.sequences import add_sequences, stretched_sequences
from asciiplot._components.axes import x_axis_comprising_chart, y_axis_comprising_chart, x_label_row
from asciiplot._variable_encapsulations import Config, Params


_n_terminal_columns = shutil.get_terminal_size().columns
_DEFAULT_COLOR = 'WHITE'


def asciiize(
        *sequences: List[float],
        chart_height: int = 5,
        in_between_points_margin: int = 0,

        sequence_colors: Sequence[str] = tuple([_DEFAULT_COLOR]),
        label_color: str = _DEFAULT_COLOR,

        x_labels: Optional[Sequence[Optional[Union[str, float]]]] = None,
        y_label_decimal_places: int = 1,

        x_axis_description: str = '',
        y_axis_description: str = '',
        axis_description_color: str = _DEFAULT_COLOR,

        title: Optional[str] = None,
        title_color: str = _DEFAULT_COLOR,

        chart_indentation: int = 0,
        center_chart: bool = False) -> str:

    # raise Value Error if passed more sequence colors than sequences
    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of passed sequence colors exceeding number of sequences')

    # forward kwargs to config
    kwargs = locals().copy()
    del kwargs['sequences']
    config = Config(**kwargs)

    # stretch sequences if desired
    if config.in_between_points_margin:
        sequences = stretched_sequences(sequences, config.in_between_points_margin)  # type: ignore

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
    if config.center_chart:
        n_whitespaces = centering_indentation_len(params.total_width, reference_length=_n_terminal_columns)
        centering_margin = ' ' * n_whitespaces

        for row_index in range(len(chart_grid)):
            chart_grid[row_index].insert(0, centering_margin)

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


def _create_chart_grid(sequences: types.Sequences, config: Config, params: Params) -> types.ChartGrid:
    """ Creates chart with y-axis and x-axis if desired """

    chart = [[' '] * params.chart_width for _ in range(config.chart_height)]

    add_sequences(sequences, chart, config, params)

    chart = x_axis_comprising_chart(chart, config)
    chart = y_axis_comprising_chart(chart, config, params)

    if config.chart_indentation:
        indentation = ' ' * config.chart_indentation
        chart = [[indentation] + row for row in chart]

    return chart


def _serialize_chart(chart: types.ChartGrid) -> str:
    return '\n'.join([''.join(row).rstrip() for row in chart]) + '\n'


def _title_header(config: Config, params: Params) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    assert config.title is not None
    return ' ' * (centering_indentation_len(len(config.title), reference_length=params.chart_width) + params.horizontal_y_axis_offset) + colored(config.title, config.title_color) + '\n'

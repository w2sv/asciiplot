from asciiplot._utils import (
    colored,
    newlined,
    indented,
    centering_indentation_len
)
from asciiplot._config import Config
from asciiplot._chart import ChartGrid
from . import x_axis_tick_row


def layout_element_containing(serialized_chart: str, config: Config, chart_params: ChartGrid.Params) -> str:
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
    if config.x_axis_ticks:
        serialized_chart = serialized_chart + x_axis_tick_row.render(
            config.x_axis_ticks,
            config.label_color,
            chart_params.columns_to_y_axis_ticks,
            config.inter_points_margin
        )

    return serialized_chart


def _title_header(title: str, title_color: str, chart_width: int, horizontal_y_axis_offset: int) -> str:
    """ Returns:
            aptly indented title header with successive newline """

    return f'{indented(colored(title, title_color), columns=(centering_indentation_len(len(title), reference_length=chart_width) + horizontal_y_axis_offset))}\n'

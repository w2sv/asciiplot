from asciiplot._chart.grid import ChartGrid
from asciiplot._chart.serialized.layout_element_adding.x_axis_tick_row import x_axis_tick_row
from asciiplot._coloring import Color, colored
from asciiplot._config import Config
from asciiplot._utils.formatting import centering_indentation_len, indented, newline_succeeded


def add_layout_elements(serialized_chart: str, config: Config, chart_params: ChartGrid.Params) -> str:

    # add axis descriptions if applicable
    if config.x_axis_description:
        serialized_chart += f' {config.colored_x_axis_description}'
    serialized_chart = newline_succeeded(serialized_chart)

    if config.y_axis_description:
        serialized_chart = f'{newline_succeeded(indented(config.colored_y_axis_description, columns=centering_indentation_len(len(config.y_axis_description), chart_params.columns_to_y_axis_ticks * 2)))}' \
                           f'{serialized_chart}'

    # add title if applicable
    if config.title:
        serialized_chart = _title_header_row(
            config.title,
            config.title_color,
            chart_params.width,
            chart_params.columns_to_y_axis_ticks
        ) + serialized_chart

    # add x-axis ticks if applicable
    if config.x_axis_ticks:
        serialized_chart = serialized_chart + x_axis_tick_row(
            config.x_axis_ticks,
            config.tick_color,
            chart_params.columns_to_y_axis_ticks,
            config.inter_points_margin
        )

    return serialized_chart


def _title_header_row(title: str, title_color: Color, chart_width: int, horizontal_y_axis_offset: int) -> str:
    """ Returns:
            aptly indented title header with successive newline

        >>> print(_title_header_row('Creative title', Color.TAN, chart_width=40, horizontal_y_axis_offset=3))
                        \x1b[38;5;180mCreative title\x1b[0m """

    return newline_succeeded(indented(colored(title, title_color), columns=(centering_indentation_len(len(title), reference_length=chart_width) + horizontal_y_axis_offset)))

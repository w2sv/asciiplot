from asciiplot._chart.serialized.x_axis_tick_row import x_axis_tick_label_row
from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._params import Params
from asciiplot._utils.formatting import centering_indentation_len, indented, newline_trailed


def with_layout_elements(serialized_chart: str, config: Config, params: Params) -> str:
    if config.x_axis_description:
        serialized_chart += f' {config.x_axis_description}'
    serialized_chart = newline_trailed(serialized_chart)

    if config.y_axis_description:
        positioned_y_axis_description = newline_trailed(
            indented(
                config.y_axis_description,
                by=centering_indentation_len(
                    len(config.y_axis_description),
                    reference_length=params.indentation * 2
                )
            )
        )
        serialized_chart = positioned_y_axis_description + serialized_chart

    if config.title:
        serialized_chart = _title_row(
            config.title,
            params.x_axis_width,
            params.indentation
        ) + serialized_chart

    if params.x_axis_tick_label_values:
        serialized_chart += x_axis_tick_label_row(
            params.x_axis_tick_label_values,
            config.label_color,
            config.tick_label_background_color,
            params.y_axis_column,
            config.inter_points_margin
        )

    return serialized_chart


def _title_row(title: ColoredString, chart_width: int, horizontal_y_axis_offset: int) -> str:
    r""" Returns:
            indented title header with successive newline

        >>> repr(_title_row(ColoredString('Creative title', Color.TAN), chart_width=40, horizontal_y_axis_offset=3))
        "'                \\x1b[38;5;180mCreative title\\x1b[0m\\n'" """

    return newline_trailed(
        indented(
            title,
            by=centering_indentation_len(
                title.displayed_length,
                reference_length=chart_width
            ) + horizontal_y_axis_offset
        )
    )
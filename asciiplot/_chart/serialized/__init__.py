from asciiplot._chart.grid import ChartGrid
from asciiplot._chart.serialized.x_axis_tick_row import x_axis_tick_label_row
from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._params import Params
from asciiplot._sequence_interpolation import interpolate_sequences
from asciiplot._type_aliases import PlotSequences
from asciiplot._utils.formatting import centering_indentation_len, indented, newline_succeeded


class SerializedChart(str):
    @classmethod
    def fully_rendered(cls, config: Config, sequences: PlotSequences):
        # Interpolate sequences if required
        if config.inter_points_margin:
            plot_sequences = tuple(interpolate_sequences(sequences, config.inter_points_margin))
        else:
            plot_sequences = sequences  # type: ignore

        params = Params.extract(plot_sequences, config=config)
        chart_grid = ChartGrid(plot_sequences, config=config, params=params)

        return SerializedChart(chart_grid).add_layout_elements(
            config=config,
            params=params
        )

    def __new__(cls, chart_grid: ChartGrid):
        return super().__new__(cls, chart_grid.serialized())

    def add_layout_elements(self, config: Config, params: Params) -> str:
        laid_out_chart = str(self)

        if config.x_axis_description:
            laid_out_chart += f' {config.x_axis_description}'
        laid_out_chart = newline_succeeded(laid_out_chart)

        if config.y_axis_description:
            positioned_y_axis_description = newline_succeeded(
                indented(
                    config.y_axis_description,
                    columns=centering_indentation_len(
                        len(config.y_axis_description),
                        reference_length=params.columns_to_y_axis_ticks * 2
                    )
                )
            )
            laid_out_chart = positioned_y_axis_description + laid_out_chart

        if config.title:
            laid_out_chart = _title_row(
                config.title,
                params.x_axis_width,
                params.columns_to_y_axis_ticks
            ) + laid_out_chart

        if params.x_axis_tick_label_values:
            laid_out_chart += x_axis_tick_label_row(
                params.x_axis_tick_label_values,
                config.label_color,
                config.tick_label_background_color,
                params.columns_to_y_axis_ticks,
                config.inter_points_margin
            )

        return laid_out_chart


def _title_row(title: ColoredString, chart_width: int, horizontal_y_axis_offset: int) -> str:
    r""" Returns:
            indented title header with successive newline

        >>> repr(_title_row(ColoredString('Creative title', Color.TAN), chart_width=40, horizontal_y_axis_offset=3))
        "'                \\x1b[38;5;180mCreative title\\x1b[0m\\n'" """

    return newline_succeeded(
        indented(
            title,
            columns=centering_indentation_len(title.display_length, reference_length=chart_width) + horizontal_y_axis_offset
        )
    )

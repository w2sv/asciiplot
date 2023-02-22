import itertools as itt

import math

from asciiplot._config import Config
from asciiplot._constants import AUTO
from asciiplot._type_aliases import PlotSequences, TickLabelInput, TickLabelValues
from asciiplot._utils.console import console_width
from asciiplot._utils.formatting import centering_indentation_len
from asciiplot._utils.iterables import max_element_length
from typing import Iterator, List, Optional


class Params:

    @classmethod
    def compute(cls, plot_sequences: PlotSequences, config: Config):
        value_entirety: List[float] = list(itt.chain.from_iterable(plot_sequences))

        return cls(
            y_min=int(math.floor(min(value_entirety))),
            y_max=int(math.ceil(max(value_entirety))),
            x_axis_width=max_element_length(plot_sequences),
            x_axis_tick_label_values=cls._x_axis_tick_label_values(
                config.x_axis_tick_label_input,
                config.n_points
            ),
            x_axis_description_len=len(config.x_axis_description) if config.x_axis_description else 0,
            config=config
        )

    def __init__(self,
                 y_min: int,
                 y_max: int,
                 x_axis_width: int,
                 x_axis_tick_label_values: Optional[TickLabelValues],
                 x_axis_description_len: int,
                 config: Config):
        self.y_min = y_min
        self.y_max = y_max

        self.x_axis_width = x_axis_width

        self.x_axis_tick_label_values = x_axis_tick_label_values
        self.x_axis_description_len = x_axis_description_len

        self.y_range: float = abs(y_max - y_min)
        self.i_row_per_y: float = max(1., config.height / self.y_range)
        self.y_axis_tick_labels: List[str] = list(
            self._y_axis_tick_labels(config.height, config.y_axis_tick_label_decimal_places)
        )

        self.y_tick_column_width: int = max_element_length(self.y_axis_tick_labels)
        self.chart_width: int = self.y_tick_column_width + self.x_axis_width + self.x_axis_description_len + 1
        self.indentation: int = self._indentation(config, self.chart_width)
        self.y_axis_column: int = self.indentation + self.y_tick_column_width

    @staticmethod
    def _x_axis_tick_label_values(tick_label_input: TickLabelInput, n_points: int) -> Optional[TickLabelValues]:
        """
        >>> list(Params._x_axis_tick_label_values('auto', 4))
        [1, 2, 3, 4] """

        if tick_label_input == AUTO:
            return range(1, n_points + 1)
        return tick_label_input

    @staticmethod
    def _indentation(config: Config, chart_width: int) -> int:
        if config.indentation:
            return config.indentation
        elif config.center_horizontally:
            return centering_indentation_len(chart_width, reference_length=console_width())
        return 0

    def _y_axis_tick_labels(self, chart_height: int, decimal_places: int) -> Iterator[str]:
        delta_y_per_row = self.y_range / (chart_height - 1)
        for i in range(chart_height):
            label: float = self.y_max - i * delta_y_per_row
            yield f'{round(label, decimal_places):.{decimal_places}f}'

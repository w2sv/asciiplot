import itertools as itt
import math
from typing import Iterator, List, Optional

from asciiplot._config import Config
from asciiplot._utils.iterables import max_element_length
from asciiplot._type_aliases import PlotSequences, TickLabelInput, TickLabelValues
from asciiplot._constants import AUTO


class Params:
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

        self.y_value_range: float = abs(y_max - y_min)
        self.delta_row_index_per_y: float = max(1., config.height / self.y_value_range)
        self.y_axis_tick_labels: List[str] = list(
            self._y_axis_tick_labels(config.height, config.y_axis_tick_label_decimal_places)
        )
        self.y_tick_columns: int = max_element_length(self.y_axis_tick_labels)
        self.columns_to_y_axis_ticks: int = self.y_tick_columns + config.horizontal_indentation

    @classmethod
    def extract(cls, plot_sequences: PlotSequences, config: Config):
        values: List[float] = list(itt.chain.from_iterable(plot_sequences))
        x_axis_width = max_element_length(plot_sequences)

        return cls(
            y_min=int(math.floor(min(values))),
            y_max=int(math.ceil(max(values))),
            x_axis_width=x_axis_width,
            x_axis_tick_label_values=cls._x_axis_tick_label_values(
                config.x_axis_tick_label_input,
                config.n_points
            ),
            x_axis_description_len=len(config.x_axis_description) if config.x_axis_description else 0,
            config=config
        )

    @staticmethod
    def _x_axis_tick_label_values(tick_label_input: TickLabelInput, n_points: int) -> Optional[TickLabelValues]:
        """
        >>> list(Params._x_axis_tick_label_values('auto', 4))
        [1, 2, 3, 4] """

        if tick_label_input == AUTO:
            return range(1, n_points + 1)
        return tick_label_input

    @property
    def total_width(self) -> int:
        return self.columns_to_y_axis_ticks + self.x_axis_width + self.x_axis_description_len + 1

    def _y_axis_tick_labels(self, chart_height: int, decimal_places: int) -> Iterator[str]:
        delta_y_per_row = self.y_value_range / (chart_height - 1)
        for i in range(chart_height):
            label: float = self.y_max - i * delta_y_per_row
            yield f'{round(label, decimal_places):.{decimal_places}f}'
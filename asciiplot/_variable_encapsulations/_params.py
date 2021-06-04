from typing import List
import math
import itertools

from asciiplot._utils import types
from asciiplot._variable_encapsulations._config import Config


class Params:
    def __init__(self, sequences: types.Sequences, config: Config):
        # sequence value extrema
        finite_values = list(filter(math.isfinite, itertools.chain(*sequences)))

        # target extrema
        self.y_min: int = int(math.floor(min(finite_values)))
        self.y_max: int = int(math.ceil(max(finite_values)))

        # y value parameters
        self.y_value_spread: int = abs(self.y_max - self.y_min)
        self.delta_row_index_per_y: float = config.chart_height / [1, self.y_value_spread][bool(self.y_value_spread)]

        # label parameters
        self.y_labels: List[str] = self._compute_labels(config)
        self.n_label_column_columns: int = max(map(len, self.y_labels))

        # widths
        self.chart_width: int = max(map(len, sequences))
        self.horizontal_y_axis_offset: int = self.n_label_column_columns + config.chart_indentation

        self._x_axis_description_len: int = len(config.x_axis_description)

    @property
    def total_width(self) -> int:
        return self.horizontal_y_axis_offset + self.chart_width + self._x_axis_description_len + 1

    def _compute_labels(self, config: Config) -> List[str]:
        label_strings: List[str] = []

        delta_y_per_row = self.y_value_spread / (config.chart_height - 1)
        for i in range(config.chart_height):
            label: float = self.y_max - i * delta_y_per_row

            # format label according to intended decimal places
            if config.y_label_decimal_places:
                decimal_point_adjusted_label = f'{round(label, config.y_label_decimal_places):.{config.y_label_decimal_places}f}'
            else:
                decimal_point_adjusted_label = str(int(label))
            label_strings.append(decimal_point_adjusted_label)

        return label_strings

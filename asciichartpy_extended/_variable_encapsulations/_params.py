from __future__ import annotations
from typing import List
import dataclasses
import math
import itertools

from asciichartpy_extended._types import _Sequences
from asciichartpy_extended._variable_encapsulations._config import Config


@dataclasses.dataclass
class _Params:
    y_min: int
    definition_area_magnitude: int

    y_min: int
    y_max: int

    plot_width: int

    total_width: int
    horizontal_y_axis_offset: int

    labels: List[str]
    label_columns: int

    y_value_spread: int
    delta_row_index_per_y: float

    def __init__(self, sequences: _Sequences, config: Config, definition_area_magnitude: int):
        self.definition_area_magnitude = definition_area_magnitude

        # sequence value extrema
        finite_values = list(filter(math.isfinite, itertools.chain(*sequences)))

        # target extrema
        self.y_min = int(math.floor(min(finite_values)))
        self.y_max = int(math.ceil(max(finite_values)))

        # y value parameters
        self.y_value_spread = abs(self.y_max - self.y_min)
        self.delta_row_index_per_y = config.n_plot_rows / [1, self.y_value_spread][bool(self.y_value_spread)]

        # label parameters
        self.labels = self._compute_labels(config)
        self.label_columns = max(map(len, self.labels))

        # widths
        self.plot_width = max(map(len, sequences))

        self.horizontal_y_axis_offset = self.label_columns + config.label_column_offset
        self.total_width = self.horizontal_y_axis_offset + self.plot_width

    def _compute_labels(self, config: Config) -> List[str]:
        label_strings: List[str] = []

        delta_y_per_row = self.y_value_spread / (config.n_plot_rows - 1)
        for i in range(config.n_plot_rows):
            label: float = self.y_max - i * delta_y_per_row

            # format label according to intended decimal places
            if config.y_label_decimal_places:
                decimal_point_adjusted_label = f'{round(label, config.y_label_decimal_places):.{config.y_label_decimal_places}f}'
            else:
                decimal_point_adjusted_label = str(int(label))
            label_strings.append(decimal_point_adjusted_label)

        return label_strings

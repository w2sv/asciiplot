from __future__ import annotations
from typing import List
import dataclasses
import math
import itertools


from asciichartpy_extended._types import _Sequences
from asciichartpy_extended._config import Config, _NOT_TO_BE_ALTERED


@dataclasses.dataclass
class _Params:
    sequence_values_min: int

    target_min: int
    target_max: int

    definition_area_magnitude: int

    chart_width: int
    horizontal_y_axis_offset: int

    labels: List[str]
    label_columns: int

    y_value_spread: int
    delta_y: float

    def __init__(self, sequences: _Sequences, config: Config):
        # sequence value extrema
        finite_values = list(filter(math.isfinite, itertools.chain(*sequences)))

        self.sequence_values_min = int(math.floor(min(finite_values)))
        sequence_values_max = int(math.ceil(max(finite_values)))

        # target extrema
        self.target_min = max([self.sequence_values_min, config.min])
        self.target_max = min([sequence_values_max, config.max])

        # y value parameters
        self.y_value_spread = self.target_max - self.target_min
        self.delta_y = config.height / self.y_value_spread

        # label parameters
        self.labels = self._compute_labels(config)
        self.label_columns = max(map(len, self.labels))

        # widths
        self.definition_area_magnitude = max(map(len, sequences))

        self.horizontal_y_axis_offset = self.label_columns + config.offset
        self.chart_width = self.horizontal_y_axis_offset + self.definition_area_magnitude

    def _compute_labels(self, config: Config) -> List[str]:
        labels: List[str] = []
        for i in range(config.height + 1):
            label = self.target_max - (i * self.y_value_spread / config.height)
            if config.decimal_places_y_labels != _NOT_TO_BE_ALTERED:
                label = round(label, config.decimal_places_y_labels)
            labels.append(str(label))
        return labels

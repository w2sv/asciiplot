from __future__ import annotations
from typing import List
from dataclasses import dataclass
import math

from asciichartpy_extended._types import _Sequences
from asciichartpy_extended._config import Config, _NOT_TO_BE_ALTERED


@dataclass
class _Params:
    min: int
    max: int

    n_rows: int

    plot_width: int
    chart_width: int
    offset: int

    labels: List[str]
    label_length: int

    def __init__(self, sequences: _Sequences, config: Config):
        self.min = int(math.floor(config.actual_min))
        self.max = int(math.ceil(config.actual_max))

        self.n_rows = config.height

        self.plot_width = max(map(len, sequences))

        self.labels = self._compute_labels(config)
        self.label_length = max(map(len, self.labels))

        self.offset = self.label_length + config.offset
        self.chart_width = self.offset + self.plot_width

    def _compute_labels(self, config: Config) -> List[str]:
        labels: List[str] = []
        for i in range(self.n_rows + 1):
            label = config.max - (i * config.y_value_spread / self.n_rows)
            if config.decimal_places_y_labels != _NOT_TO_BE_ALTERED:
                label = round(label, config.decimal_places_y_labels)
            labels.append(str(label))
        return labels

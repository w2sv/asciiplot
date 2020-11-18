from __future__ import annotations
from dataclasses import dataclass
from math import floor, ceil

from asciichartpy_extended._types import _Sequences
from asciichartpy_extended._config import Config


@dataclass
class Params:
    min: int
    max: int

    n_rows: int

    plot_width: int
    chart_width: int

    def __init__(self, sequences: _Sequences, config: Config):
        self.min = int(floor(config.min * config.ratio))
        self.max = int(ceil(config.max * config.ratio))

        self.n_rows = self.max - self.min

        self.plot_width = max(map(len, sequences))
        self.chart_width = self.plot_width + config.offset

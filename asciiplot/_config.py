import dataclasses
from typing import Optional, Sequence

from asciiplot._coloring import Color, ColoredString
from asciiplot._utils.type_aliases import TickValues


@dataclasses.dataclass(frozen=True)
class Config:
    """ Collection of received chart configuration options """

    height: int
    inter_points_margin: int

    sequence_colors: Sequence[Color]
    label_color: Color

    x_axis_tick_labels: Optional[TickValues]
    y_axis_tick_label_decimal_places: int

    x_axis_description: Optional[ColoredString]
    y_axis_description: Optional[ColoredString]

    title: Optional[ColoredString]

    horizontal_indentation: int
    center_horizontally: bool

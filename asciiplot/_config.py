import dataclasses
from typing import Optional, Sequence

from asciiplot._coloring import Color, ColoredString
from asciiplot._type_aliases import TickLabelInput


@dataclasses.dataclass(frozen=True)
class Config:
    """ Collection of received chart configuration options """

    height: int
    inter_points_margin: int
    n_points: int

    sequence_colors: Sequence[Color]
    background_color: Color
    label_color: Color

    x_axis_tick_label_input: TickLabelInput
    y_axis_tick_label_decimal_places: int
    tick_label_background_color: Color

    x_axis_description: Optional[ColoredString]
    y_axis_description: Optional[ColoredString]

    title: Optional[ColoredString]

    horizontal_indentation: int
    center_horizontally: bool

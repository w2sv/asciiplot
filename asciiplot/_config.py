import dataclasses
from typing import Sequence, Optional, Union

from asciiplot._coloring import colored, Color

Ticks = Sequence[Optional[Union[str, float]]]


@dataclasses.dataclass(frozen=True)
class Config:
    height: int
    inter_points_margin: int

    sequence_colors: Sequence[Color]
    tick_color: Color

    x_axis_ticks: Optional[Ticks]
    y_axis_ticks_decimal_places: int

    x_axis_description: str
    y_axis_description: str
    axis_description_color: Color

    title: Optional[str]
    title_color: Color

    indentation: int
    center: bool

    def axis_description(self, x_axis: bool) -> str:
        return colored([self.y_axis_description, self.x_axis_description][x_axis], self.axis_description_color)

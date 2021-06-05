import dataclasses
from typing import Sequence, Optional, Union

from asciiplot._utils import colored


Ticks = Sequence[Optional[Union[str, float]]]


@dataclasses.dataclass(frozen=True)
class Config:
    height: int
    inter_points_margin: int

    sequence_colors: Sequence[str]
    label_color: str

    x_axis_ticks: Optional[Ticks]
    y_axis_ticks_decimal_places: int

    x_axis_description: str
    y_axis_description: str
    axis_description_color: str

    title: Optional[str]
    title_color: str

    indentation: int
    center: bool

    def axis_description(self, x_axis: bool) -> str:
        return colored([self.y_axis_description, self.x_axis_description][x_axis], self.axis_description_color)

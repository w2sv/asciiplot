import dataclasses
from typing import Sequence, Optional, Union

from typing_extensions import TypeAlias

from asciiplot._coloring import colored, Color


TickValue: TypeAlias = Union[str, float]
TickValues: TypeAlias = Sequence[Optional[TickValue]]


@dataclasses.dataclass
class Config:
    height: int
    inter_points_margin: int

    sequence_colors: Sequence[Color]
    tick_color: Color

    x_axis_ticks: Optional[TickValues]
    y_axis_tick_decimal_places: int

    x_axis_description: str
    colored_x_axis_description: str = dataclasses.field(init=False)
    y_axis_description: str
    colored_y_axis_description: str = dataclasses.field(init=False)

    axis_description_color: dataclasses.InitVar[Color]

    title: Optional[str]
    title_color: Color

    indentation: int
    center: bool

    def __post_init__(self, axis_description_color: Color):
        self.colored_x_axis_description = colored(self.x_axis_description, color=axis_description_color)
        self.colored_y_axis_description = colored(self.y_axis_description, color=axis_description_color)
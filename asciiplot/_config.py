import dataclasses
from typing import Sequence, Optional, Union

from asciiplot._utils import colored


@dataclasses.dataclass(frozen=True)
class Config:
    height: int
    inter_points_margin: int

    sequence_colors: Sequence[str]
    label_color: str

    x_labels: Optional[Sequence[Optional[Union[str, float]]]]
    y_label_decimal_places: int

    x_axis_description: str
    y_axis_description: str
    axis_description_color: str

    title: Optional[str]
    title_color: str

    indentation: int
    center: bool

    def axis_description(self, x_axis: bool) -> str:
        return colored([self.y_axis_description, self.x_axis_description][x_axis], self.axis_description_color)

from typing import Optional, Sequence, Union, Dict
import math
import dataclasses

from asciichartpy_extended import colors


_NOT_TO_BE_ALTERED = -1
_INIT_MIN = -math.inf
_INIT_MAX = math.inf


@dataclasses.dataclass
class Config:
    """ Fields:
            offset: between outer left terminal bound and y-labels
            height: of chart in n rows
            x_labels: may contain less, however not more elements
                than length of longest sequence
            title: displayed in centered manner above chart """

    min: float = _INIT_MIN
    max: float = _INIT_MAX

    offset: int = 3
    height: int = 5
    columns_between_points: int = 0

    sequence_colors: Sequence[str] = (colors.WHITE,)
    decimal_places_y_labels: Optional[int] = _NOT_TO_BE_ALTERED

    display_x_axis: bool = False
    x_labels: Optional[Dict[int, Union[str, float]]] = None

    x_axis_description: Optional[str] = None
    y_axis_description: Optional[str] = None

    title: Optional[str] = None

    def __post_init__(self):
        # process decimal_places_y_labels
        if not self.decimal_places_y_labels:
            self.decimal_places_y_labels = None

        # assert extrema correctness in case of passing of any
        if self.min != _INIT_MIN or self.max != _INIT_MAX and self.min > self.max:
            raise ValueError("Min value shan't exceed max value")

        # assert enablement of display_x_axis in case of passed x_axis_description
        if self.x_axis_description and not self.display_x_axis:
            raise ValueError("Setting of x axis description requires display of x axis")

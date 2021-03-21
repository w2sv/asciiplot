from typing import Optional, Sequence, Union, Dict
import math
import dataclasses

from asciichartpy_extended._coloring import colors


_INIT_MIN = -math.inf
_INIT_MAX = math.inf


@dataclasses.dataclass
class Config:
    """ Fields:
            label_column_offset: between outer left terminal bound and y-labels
            columns_between_points: leads to consistent, linearly interpolated
                stretching of sequences
            n_plot_rows: number of rows
            x_labels: may contain more or less elements than definition area
            title: displayed in centered manner above chart """

    n_plot_rows: int = 5
    label_column_offset: int = 0
    columns_between_points: int = 0

    sequence_colors: Sequence[str] = colors.WHITE,
    axis_description_color: str = colors.WHITE
    x_axis_label_color: str = colors.WHITE

    y_label_decimal_places: int = 1

    display_x_axis: bool = False
    x_labels: Optional[Dict[int, Union[str, float]]] = None

    x_axis_description: str = ''
    y_axis_description: str = ''

    title: Optional[str] = None

    def __post_init__(self):
        """ Processes parameters, asserts value correctness """

        # process y_label_decimal_places
        if not self.y_label_decimal_places:
            self.y_label_decimal_places = None

        # assert enablement of display_x_axis in case of passed x_axis_description
        if self.x_axis_description and not self.display_x_axis:
            raise ValueError("Setting of x axis description requires display of x axis")

from typing import Optional, Sequence, Union, Dict
import math

from asciichartpy_extended._coloring import colors


_INIT_MIN = -math.inf
_INIT_MAX = math.inf


class Config:
    """ Fields:
            label_column_offset: between outer left terminal bound and y-labels
            columns_between_points: leads to consistent, linearly interpolated
                stretching of sequences
            n_plot_rows: number of rows
            x_labels: may contain more or less elements than definition area
            title: displayed in centered manner above chart """

    def __init__(self,
                 n_plot_rows: int = 5,
                 label_column_offset: int = 0,
                 columns_between_points: int = 0,
                 sequence_colors: Sequence[str] = colors.WHITE,
                 axis_description_color: str = colors.WHITE,

                 x_axis_label_color: str = colors.WHITE,
                 y_label_decimal_places: int = 1,

                 display_x_axis: bool = False,
                 x_labels: Optional[Dict[int, Union[str, float]]] = None,

                 x_axis_description: str = '',
                 y_axis_description: str = '',

                 title: Optional[str] = None):

        self.n_plot_rows = n_plot_rows
        self.label_column_offset = label_column_offset
        self.columns_between_points = columns_between_points

        self.sequence_colors = sequence_colors
        self.axis_description_color = axis_description_color
        self.x_axis_label_color = x_axis_label_color

        if x_axis_description and not display_x_axis:
            raise ValueError("Setting of x axis description requires display of x axis")

        self.display_x_axis = display_x_axis
        self.x_labels = x_labels
        self.x_axis_description = x_axis_description

        self.y_axis_description = y_axis_description
        self.y_label_decimal_places = y_label_decimal_places

        self.title = title

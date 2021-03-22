from typing import Optional, Union, Sequence

from asciiplot._coloring import colors


class Config:
    def __init__(self,
                 n_plot_rows: int = 5,
                 label_column_offset: int = 0,
                 columns_between_points: int = 0,

                 sequence_colors: Sequence[str] = colors.WHITE,
                 axis_description_color: str = colors.WHITE,
                 label_color: str = colors.WHITE,

                 x_labels: Optional[Sequence[Optional[Union[str, float]]]] = None,
                 x_axis_description: str = '',
                 y_label_decimal_places: int = 1,
                 y_axis_description: str = '',

                 title: Optional[str] = None,
                 center_plot: bool = False):

        self.n_plot_rows = n_plot_rows
        self.label_column_offset = label_column_offset
        self.columns_between_points = columns_between_points

        self.sequence_colors = sequence_colors
        self.axis_description_color = axis_description_color
        self.label_color = label_color

        self.x_labels = x_labels
        self.x_axis_description = x_axis_description
        self.y_axis_description = y_axis_description
        self.y_label_decimal_places = y_label_decimal_places

        self.title = title
        self.center_plot = center_plot

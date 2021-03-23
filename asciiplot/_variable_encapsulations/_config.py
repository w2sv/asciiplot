from typing import Optional, Union, Sequence


class Config:
    def __init__(
            self,
            n_plot_rows: int,
            label_column_offset: int,
            columns_between_points: int,

            sequence_colors: Sequence[str],
            axis_description_color: str,
            label_color: str,

            x_labels: Optional[Sequence[Optional[Union[str, float]]]],
            x_axis_description: str,
            y_label_decimal_places: int,
            y_axis_description: str,

            title: Optional[str],
            title_color: str,
            center_plot: bool):

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
        self.title_color = title_color
        self.center_plot = center_plot

from asciiplot._config import Config
from asciiplot._chart import ChartGrid


def test_chart_params():
    assert str(ChartGrid.Params.extract(
        ([5, 9, 2], ),
        config=Config(
            height=5,
            inter_points_margin=3,
            axis_description_color='WHITE',
            x_axis_description='x_axis',
            y_axis_description='y_axis',
            y_label_decimal_places=3,
            label_color='WHITE',
            title_color='WHITE',
            title='title',
            x_labels=list(range(3)),
            center=False,
            indentation=4,
            sequence_colors=['WHITE']
        )
    )) == "ChartGrid.Params(y_min=2, y_max=9, y_value_spread=7, delta_row_index_per_y=1.0, width=3, x_axis_description_len=6, y_axis_ticks=['9.000', '7.250', '5.500', '3.750', '2.000'], columns_to_y_axis_ticks=9, label_columns=5)"

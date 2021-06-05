import pytest

from asciiplot._coloring import Color
from asciiplot._config import Config
from asciiplot._chart import ChartGrid


@pytest.mark.parametrize('params,expected', [
    (
        ChartGrid.Params.extract(
            ([5, 9, 2], ),
            config=Config(
                height=5,
                inter_points_margin=3,
                axis_description_color=Color.DEFAULT,
                x_axis_description='x_axis',
                y_axis_description='y_axis',
                y_axis_ticks_decimal_places=3,
                tick_color=Color.DEFAULT,
                title_color=Color.DEFAULT,
                title='title',
                x_axis_ticks=list(range(3)),
                center=False,
                indentation=4,
                sequence_colors=[Color.DEFAULT]
            )
        ),
        "ChartGrid.Params(y_min=2, y_max=9, y_value_spread=7, delta_row_index_per_y=1.0, width=3, x_axis_description_len=6, y_axis_ticks=['9.000', '7.250', '5.500', '3.750', '2.000'], columns_to_y_axis_ticks=9, y_tick_columns=5)"
    ),
    (
        ChartGrid.Params.extract(
            ([89, 4, 53, -80], [92, 75, 44, 44, 101]),
            config=Config(
                height=27,
                inter_points_margin=11,
                axis_description_color=Color.DEFAULT,
                x_axis_description='x_axis',
                y_axis_description='y_axis',
                y_axis_ticks_decimal_places=1,
                tick_color=Color.DEFAULT,
                title_color=Color.DEFAULT,
                title='title',
                x_axis_ticks=list(range(5)),
                center=False,
                indentation=7,
                sequence_colors=[Color.DEFAULT]
            )
        ),
        "ChartGrid.Params(y_min=-80, y_max=101, y_value_spread=181, delta_row_index_per_y=1.0, width=5, x_axis_description_len=6, y_axis_ticks=['101.0', '94.0', '87.1', '80.1', '73.2', '66.2', '59.2', '52.3', '45.3', '38.3', '31.4', '24.4', '17.5', '10.5', '3.5', '-3.4', '-10.4', '-17.3', '-24.3', '-31.3', '-38.2', '-45.2', '-52.2', '-59.1', '-66.1', '-73.0', '-80.0'], columns_to_y_axis_ticks=12, y_tick_columns=5)"
    )
])
def test_chart_params(params, expected):
    assert str(params) == expected

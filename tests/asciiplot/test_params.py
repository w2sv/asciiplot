import pytest

from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._constants import AUTO
from asciiplot._params import Params


@pytest.mark.parametrize(
    'extract_args, expected', [
        (
                (
                        ([5, 9, 2],),
                        Config(
                            height=5,
                            inter_points_margin=3,
                            x_axis_description=ColoredString('x_axis'),
                            y_axis_description=ColoredString('y_axis'),
                            y_axis_tick_label_decimal_places=3,
                            label_color=Color.DEFAULT,
                            background_color=Color.CHARTREUSE_2B,
                            title=ColoredString('title'),
                            x_axis_tick_label_input='auto',
                            center_horizontally=False,
                            horizontal_indentation=4,
                            sequence_colors=[Color.DEFAULT],
                            n_points=3,
                            tick_label_background_color=Color.CHARTREUSE_2B
                        )
                ),
                {
                    'columns_to_y_axis_ticks': 9,
                    'i_row_per_y': 1.0,
                    'x_axis_description_len': 6,
                    'x_axis_tick_label_values': range(1, 4),
                    'x_axis_width': 3,
                    'y_axis_tick_labels': ['9.000', '7.250', '5.500', '3.750', '2.000'],
                    'y_max': 9,
                    'y_min': 2,
                    'y_tick_columns': 5,
                    'y_range': 7
                }
        ),
        (
                (
                        ([89, 4, 53, -80], [92, 75, 44, 44, 101]),
                        Config(
                            height=27,
                            inter_points_margin=11,
                            x_axis_description=ColoredString('x_axis'),
                            y_axis_description=ColoredString('y_axis'),
                            y_axis_tick_label_decimal_places=1,
                            label_color=Color.DEFAULT,
                            background_color=Color.CHARTREUSE_2B,
                            title=ColoredString('title'),
                            x_axis_tick_label_input='auto',
                            center_horizontally=False,
                            horizontal_indentation=7,
                            sequence_colors=[Color.DEFAULT],
                            n_points=5,
                            tick_label_background_color=Color.CHARTREUSE_2B
                        )
                ),
                {
                    'columns_to_y_axis_ticks': 12,
                    'i_row_per_y': 1.0,
                    'x_axis_description_len': 6,
                    'x_axis_tick_label_values': range(1, 6),
                    'x_axis_width': 5,
                    'y_axis_tick_labels': [
                        '101.0',
                        '94.0',
                        '87.1',
                        '80.1',
                        '73.2',
                        '66.2',
                        '59.2',
                        '52.3',
                        '45.3',
                        '38.3',
                        '31.4',
                        '24.4',
                        '17.5',
                        '10.5',
                        '3.5',
                        '-3.4',
                        '-10.4',
                        '-17.3',
                        '-24.3',
                        '-31.3',
                        '-38.2',
                        '-45.2',
                        '-52.2',
                        '-59.1',
                        '-66.1',
                        '-73.0',
                        '-80.0'
                    ],
                    'y_max': 101,
                    'y_min': -80,
                    'y_tick_columns': 5,
                    'y_range': 181
                }
        )
    ]
)
def test_compute(extract_args, expected):
    assert vars(Params.compute(*extract_args)) == expected


def test_total_width(config):
    assert Params(
        y_min=3,
        y_max=16,
        x_axis_tick_label_values=AUTO,
        x_axis_width=20,
        x_axis_description_len=5,
        config=config
    ).total_width == 36
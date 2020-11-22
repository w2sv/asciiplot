"""Module to generate ascii charts.
This module provides a single function `render_chart` that can be used to generate an
ascii chart from a sequences of numbers. The chart can be configured via several
options to tune the output.
"""

from asciichartpy_extended.version import __version__
from asciichartpy_extended._rendering import render_chart
from asciichartpy_extended._config import Config
from asciichartpy_extended import colors
from asciichartpy_extended._sequences import colored


if __name__ == '__main__':
    from random import randint

    p = render_chart([10, 5, 9], [1, 7, 5, 9], config=Config(
        x_axis_description='YOLO',
        y_axis_description='SWAG',
        decimal_places_y_labels=1,
        columns_between_points=5,
        offset=70,
        height=5,
        sequence_colors=[colors.RED, colors.GREEN],
        display_x_axis=True,
        title='SICKPLOT',
        x_labels={i: i for i in range(4)}
    ))

    print(p)

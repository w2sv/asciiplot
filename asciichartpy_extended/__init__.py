"""Module to generate ascii charts.
This module provides a single function `render_chart` that can be used to generate an
ascii chart from a sequences of numbers. The chart can be configured via several
options to tune the output.
"""

from asciichartpy_extended.version import __version__
from asciichartpy_extended._rendering import render_chart
from asciichartpy_extended._sequences import _colored
from asciichartpy_extended._config import Config
from asciichartpy_extended import colors


if __name__ == '__main__':
    from random import randint

    p = render_chart([14, 3, 8], [5, 3, 6], config=Config(
        x_axis_description='YOLO',
        y_axis_description='SWAG',
        decimal_places_y_labels=1,
        columns_between_points=25,
        offset=70,
        sequence_colors=[colors.RED, colors.GREEN],
        display_x_axis=True,
        title='SICKPLOT',
        x_labels={i: i for i in range(3)}
    ))

    print(p)

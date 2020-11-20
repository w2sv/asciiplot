"""Module to generate ascii charts.
This module provides a single function `render_chart` that can be used to generate an
ascii chart from a sequences of numbers. The chart can be configured via several
options to tune the output.
"""

from asciichartpy_extended.version import __version__
from asciichartpy_extended._core import render_chart, _colored
from asciichartpy_extended._config import Config
from asciichartpy_extended import colors


if __name__ == '__main__':
    from random import randint

    p = render_chart([randint(0, 100) for _ in range(20)], config=Config(
        decimal_places_y_labels=1,
        columns_between_points=5,
        offset=30,
        sequence_colors=[colors.RED],
        display_x_axis=True,
        height=15,
        title='SICKPLOT',
        x_labels={i: i + 99 * 10 ** 3 for i in range(20)}
    ))

    print(p)

import pytest

from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._type_aliases import PlotSequence, PlotSequences


@pytest.fixture
def sequences() -> PlotSequences:
    return [
        [4, 6, 3],
        [5, 5, 5],
        [8, 3]
    ]


@pytest.fixture
def fibonacci() -> PlotSequence:
    return [1, 1, 2, 3, 5, 8, 13, 21]


@pytest.fixture
def config() -> Config:
    return Config(
        height=5,
        inter_points_margin=3,
        x_axis_description=ColoredString('x_axis'),
        y_axis_description=ColoredString('y_axis'),
        y_axis_tick_label_decimal_places=3,
        label_color=Color.DEFAULT,
        background_color=Color.CHARTREUSE_2B,
        title=ColoredString('title'),
        x_axis_tick_label_input=range(3),
        center_horizontally=False,
        indentation=4,
        sequence_colors=[Color.DEFAULT],
        n_points=3,
        tick_label_background_color=Color.CHARTREUSE_2B
    )
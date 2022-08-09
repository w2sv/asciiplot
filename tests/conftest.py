import pytest

from asciiplot._sequence_interpolation import PlotSequences


@pytest.fixture
def sequences() -> PlotSequences:
    return [
        [4, 6, 3],
        [5, 5, 5],
        [8, 3]
    ]
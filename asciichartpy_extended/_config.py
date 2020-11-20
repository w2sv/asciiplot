from typing import Optional, Sequence, List, Union, Dict
import itertools
import math
import dataclasses

from asciichartpy_extended._types import _Sequences
from asciichartpy_extended import colors


_NOT_TO_BE_ALTERED = -1


@dataclasses.dataclass
class Config:
    """ Fields:
            offset: between outer left terminal bound and y-labels
            height: of chart in n rows
            x_labels: may contain less, however not more elements
                than length of longest sequence
            title: displayed in centered manner above chart """

    min: float = math.inf
    max: float = -math.inf

    offset: int = 3
    height: int = 5

    sequence_colors: Sequence[str] = (colors.WHITE,)
    decimal_places_y_labels: Optional[int] = _NOT_TO_BE_ALTERED

    columns_between_points: int = 0
    display_x_axis: bool = False
    x_labels: Optional[Dict[int, Union[str, float]]] = None

    title: Optional[str] = None

    y_value_spread: float = dataclasses.field(init=False)
    n_data_points: int = dataclasses.field(init=False)
    delta_y: float = dataclasses.field(init=False)

    def __post_init__(self):
        if not self.decimal_places_y_labels:
            self.decimal_places_y_labels = None

    def process(self, sequences: _Sequences) -> _Sequences:
        """  """

        self.n_data_points = max(map(len, sequences))

        finite_values = list(filter(math.isfinite, itertools.chain(*sequences)))
        self.min = min(self.min, min(finite_values))
        self.max = max(self.max, max(finite_values))

        if self.min > self.max:
            raise ValueError("Min value shan't exceed max value")

        self.y_value_spread = self.max - self.min

        if not self.height:
            self.height = int(self.y_value_spread)

        self.delta_y = self.height / [1, self.y_value_spread][self.y_value_spread > 0]

        if self.x_labels and len(self.x_labels) > self.n_data_points:
            raise ValueError('Number of x-labels exceeds number of x-values')

        if self.columns_between_points:
            sequences = self._padded_sequences(sequences)

        return sequences

    def _padded_sequences(self, sequences: _Sequences) -> _Sequences:
        """
        >>> config = Config(columns_between_points=2)
        >>> config._padded_sequences([list(range(4))])
        [[0, 0.3333333333333333, 0.6666666666666666, 1, 1.3333333333333333, 1.6666666666666665, 2, 2.3333333333333335, 2.666666666666667, 3]] """

        padded_sequences = []
        for sequence in sequences:
            padded_sequence = []
            for i in range(len(sequence[:-1])):
                padded_sequence.append(sequence[i])
                padded_sequence.extend(_fill_points(
                    start=sequence[i],
                    end=sequence[i + 1],
                    n=self.columns_between_points
                ))
            padded_sequences.append(padded_sequence + [sequence[-1]])
        return tuple(padded_sequences)


def _fill_points(start: float, end: float, n: int) -> List[float]:
    """ Returns:
            List of n points of equal step size in between the value range from start to end,
            excluding start and end themselves

        >>> _fill_points(3, 7, n=4)
        [3.8, 4.6, 5.3999999999999995, 6.199999999999999]
        >>> _fill_points(0, 1, 2)
        [0.3333333333333333, 0.6666666666666666] """

    step_size = (end - start) / (n + 1)
    return list(itertools.accumulate([start] + [step_size] * n))[1:]


if __name__ == '__main__':
    print(_fill_points(0, 1, 2))

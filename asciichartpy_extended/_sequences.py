from typing import List
import math
from functools import partial
import itertools

from asciichartpy_extended._utils import _colored
from asciichartpy_extended._params import _Params
from asciichartpy_extended._types import _Sequences, _ChartGrid
from asciichartpy_extended._config import Config


# ---------------
# Padding
# ---------------
def _stretched_sequences(sequences: _Sequences, columns_between_points: int) -> _Sequences:
    """
    >>> _stretched_sequences([list(range(4))])
    [[0, 0.3333333333333333, 0.6666666666666666, 1, 1.3333333333333333, 1.6666666666666665, 2, 2.3333333333333335, 2.666666666666667, 3]] """

    padded_sequences = []
    for sequence in sequences:
        padded_sequence = []
        for i in range(len(sequence[:-1])):
            padded_sequence.append(sequence[i])
            padded_sequence.extend(_fill_points(
                start=sequence[i],
                end=sequence[i + 1],
                n=columns_between_points
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


# ---------------
# Rendering
# ---------------
def _add_sequences(sequences: _Sequences, chart: _ChartGrid, config: Config, params: _Params):
    """ Adds ascii-ized sequences to chart

        Returns:
            last_column_occupying_segment_row_indices: List[int], row indices of sequence ends occupying
                the last chart column """

    SEGMENTS = ['┼', '─', '╰', '╭', '╮', '╯', '│']
    INIT_VALUE = -1

    scaled = partial(_scaled,
                     desired_minimum=params.target_min,
                     desired_maximum=params.target_max,
                     actual_minimum=params.sequence_values_min,
                     delta_y=params.delta_y)

    for i, sequence in enumerate(sequences):
        color = config.sequence_colors[i % len(config.sequence_colors)]
        j = INIT_VALUE

        def set_parcel(row_subtrahend: int, segment: str):
            chart[config.plot_height - row_subtrahend][j + 1] = _colored(segment, color)

        # add '┼' at sequence beginning where sequences overlaps with y-axis
        if math.isfinite(sequence[0]):
            set_parcel(scaled(sequence[0]), SEGMENTS[0])

        # ascii-ize sequence
        while (j := j + 1) < len(sequence) - 1:
            y0 = scaled(sequence[j])
            y1 = scaled(sequence[j + 1])

            if y0 == y1:
                set_parcel(y0, SEGMENTS[1])

            else:
                if y0 > y1:
                    symbol_y0, symbol_y1 = SEGMENTS[4], SEGMENTS[2]
                else:
                    symbol_y0, symbol_y1 = SEGMENTS[5], SEGMENTS[3]

                set_parcel(y0, symbol_y0)
                set_parcel(y1, symbol_y1)

                # add vertical segmentation in case of consecutive sequence
                # value steepness
                for y in range(min(y0, y1) + 1, max(y0, y1)):
                    set_parcel(y, SEGMENTS[6])


def _scaled(value: float,
            desired_minimum: float,
            desired_maximum: float,
            actual_minimum: float,
            delta_y: float) -> int:
    """ Scales sequence point clamped to desired extrema to
    corresponding point within chart value range """

    clamped_value = min(max(value, desired_minimum), desired_maximum)
    return max(int(round(clamped_value * delta_y) - actual_minimum), 0)

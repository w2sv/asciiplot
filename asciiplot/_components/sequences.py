from typing import Iterator
import math
import itertools as itt
import more_itertools

from asciiplot._utils import types
from asciiplot._utils.coloring import colored
from asciiplot._variable_encapsulations import Params, Config


# ---------------
# Padding
# ---------------
def stretched_sequences(sequences: types.Sequences, n_fill_points: int) -> types.Sequences:
    return tuple(map(lambda sequence: _interpolated_sequence(sequence, n_fill_points=n_fill_points), sequences))


def _interpolated_sequence(sequence: types.Sequence, n_fill_points: int) -> types.Sequence:
    """
        >>> _interpolated_sequence(list(range(4)), n_fill_points=3)
        [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
        >>> _interpolated_sequence(list(range(67, 87, 3)), n_fill_points=1)
        [67, 68.5, 70, 71.5, 73, 74.5, 76, 77.5, 79, 80.5, 82, 83.5, 85] """

    return list(
        itt.chain(
            itt.chain.from_iterable(
                ((i, *_fill_points(i, j, n=n_fill_points)) for i, j in more_itertools.pairwise(sequence))
            ),
            [sequence[-1]]
        )
    )


def _fill_points(start: float, end: float, n: int) -> Iterator[float]:
    """ Returns:
            List of n points of equal step size in between the value range from start to end,
            excluding start and end themselves

        >>> list(_fill_points(3, 7, n=4))
        [3.8, 4.6, 5.3999999999999995, 6.199999999999999]
        >>> list(_fill_points(0, 1, n=2))
        [0.3333333333333333, 0.6666666666666666] """

    step_size = (end - start) / (n + 1)
    return itt.islice(
        itt.accumulate(
            itt.chain(
                [start],
                itt.repeat(step_size, n)
            )
        ),
        1,
        None
    )


# ---------------
# Rendering
# ---------------
def add_sequences(sequences: types.Sequences, chart: types.ChartGrid, config: Config, params: Params):
    """ Adds ascii-ized sequences to chart

        Returns:
            last_column_occupying_segment_row_indices: List[int], row indices of sequence ends occupying
                the last chart column """

    SEGMENTS = ['┼', '─', '╰', '╭', '╮', '╯', '│']
    INIT_VALUE = -1

    def _row_index(value: float) -> int:
        """ Scales sequence point clamped to desired extrema to
        corresponding point within chart value range """

        def clamp_to_row_index_bounds(row_index: int) -> int:
            return max(min(row_index, config.chart_height - 1), 0)

        return clamp_to_row_index_bounds(row_index=int(round((value - params.y_min) * params.delta_row_index_per_y)))

    for i, sequence in enumerate(sequences):
        color = config.sequence_colors[i % len(config.sequence_colors)]
        j = INIT_VALUE

        def set_parcel(row_subtrahend: int, segment: str):
            chart[config.chart_height - 1 - row_subtrahend][j + 1] = colored(segment, color)

        # add '┼' at sequence beginning where sequences overlaps with y-axis
        if math.isfinite(sequence[0]):
            set_parcel(_row_index(sequence[0]), SEGMENTS[0])

        # asciiize sequence
        while j < len(sequence) - 2:
            j += 1

            y0 = _row_index(sequence[j])
            y1 = _row_index(sequence[j + 1])

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

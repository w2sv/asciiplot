import math
from functools import partial

from asciichartpy_extended import colors
from asciichartpy_extended._params import _Params
from asciichartpy_extended._types import _Sequences, _Chart
from asciichartpy_extended._config import Config


def _add_sequences(sequences: _Sequences, chart: _Chart, config: Config, params: _Params):
    """ Adds ascii-ized sequences to chart

        Returns:
            last_column_occupying_segment_row_indices: List[int], row indices of sequence ends occupying
                the last chart column """

    SEGMENTS = ['┼', '─', '╰', '╭', '╮', '╯', '│']
    INIT_VALUE = -1

    scaled = partial(_scaled,
                     desired_minimum=config.min,
                     desired_maximum=config.max,
                     actual_minimum=params.min,
                     delta_y=config.delta_y)

    for i, sequence in enumerate(sequences):
        color = config.sequence_colors[i % len(config.sequence_colors)]
        j = INIT_VALUE

        def set_parcel(row_subtrahend: int, segment: str):
            chart[params.n_rows - row_subtrahend][j + 1] = colored(segment, color)

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
    return int(round(clamped_value * delta_y) - actual_minimum)


def colored(string: str, color: str) -> str:
    return color + string + colors.RESET

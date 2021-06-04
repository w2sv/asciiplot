from typing import Iterator, List, Sequence as _Sequence
import itertools as itt

import more_itertools


Sequence = List[float]
Sequences = _Sequence[Sequence]


# ---------------
# Padding
# ---------------
def stretched_sequences(sequences: Sequences, n_fill_points: int) -> Sequences:
    return tuple(map(lambda sequence: _interpolated_sequence(sequence, n_fill_points=n_fill_points), sequences))


def _interpolated_sequence(sequence: Sequence, n_fill_points: int) -> Sequence:
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

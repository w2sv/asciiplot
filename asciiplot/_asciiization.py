from typing import List, Sequence, Optional, Union

from asciiplot._chart.grid import ChartGrid
from asciiplot._coloring import Color
from asciiplot._config import Config
from asciiplot._sequence_interpolation import interpolated_sequences
from asciiplot._chart import serialized


def asciiize(
        *sequences: List[float],
        height: int = 5,
        inter_points_margin: int = 0,

        sequence_colors: Sequence[Color] = tuple([Color.DEFAULT]),
        label_color: Color = Color.DEFAULT,

        x_axis_ticks: Optional[Sequence[Optional[Union[str, float]]]] = None,
        y_axis_tick_decimal_places: int = 1,

        x_axis_description: str = '',
        y_axis_description: str = '',
        axis_description_color: Color = Color.DEFAULT,

        title: Optional[str] = None,
        title_color: Color = Color.DEFAULT,

        indentation: int = 0,
        center: bool = False) -> str:

    """
    >>> print(asciiize(
    ... [1, 1, 2, 3, 5, 8, 13, 21],
    ... height=15,
    ... inter_points_margin=7,
    ...
    ... x_axis_ticks=list(range(10, 18)),
    ... y_axis_tick_decimal_places=0,
    ...
    ... x_axis_description='iteration',
    ... y_axis_description='number',
    ...
    ... title='Fibonacci Sequence',
    ...
    ... indentation=8))
                                 Fibonacci Sequence
       number
        21┤                                                 ╭──────
        19┤                                                ╭╯
        18┤                                               ╭╯
        16┤                                             ╭─╯
        15┤                                           ╭─╯
        13┤                                          ╭╯
        12┤                                        ╭─╯
        11┤                                      ╭─╯
         9┤                                   ╭──╯
         8┤                                 ╭─╯
         6┤                             ╭───╯
         5┤                          ╭──╯
         3┤                   ╭──────╯
         2┤            ╭──────╯
         1┼───────┬────╯──┬───────┬───────┬───────┬───────┬───────┬ iteration
          10      11      12      13      14      15      16      17


    >>> print(asciiize([1, 9, 5], height=8))
    9.0┤╭╮
    7.9┤││
    6.7┤││
    5.6┤│╰
    4.4┤│
    3.3┤│
    2.1┤│
    1.0┼┤┬"""

    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of received sequence colors exceeds number of sequences')

    domain_of_definition_length = max(map(len, sequences))
    if x_axis_ticks is not None and len(x_axis_ticks) > domain_of_definition_length:
        raise ValueError(
            f"X-labels do not match domain of definition; received sequences comprise "
            f"{domain_of_definition_length} distinct x-values, received {len(x_axis_ticks)} labels"
        )

    if indentation and center:
        raise ValueError('Pass either chart_indentation > 0 or set center_chart to True')

    if inter_points_margin:
        plot_sequences = tuple(interpolated_sequences(sequences, inter_points_margin))
    else:
        plot_sequences = sequences

    config = Config(
        height,
        inter_points_margin,
        sequence_colors,
        label_color,
        x_axis_ticks,
        y_axis_tick_decimal_places,
        x_axis_description,
        y_axis_description,
        axis_description_color,
        title,
        title_color,
        indentation,
        center
    )

    chart_grid = ChartGrid(config, sequences=plot_sequences)
    return serialized.render(chart_grid, config=config)

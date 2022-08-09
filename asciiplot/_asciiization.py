from typing import List, Optional, Sequence

from asciiplot._chart.serialized import SerializedChart
from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._utils.type_aliases import TickValues
from asciiplot._sequence_interpolation import interpolated_sequences
from asciiplot._utils.sequences import max_sequence_length


def asciiize(
        *sequences: List[float],
        height: int = 5,
        inter_points_margin: int = 0,

        sequence_colors: Sequence[Color] = tuple([Color.DEFAULT]),
        label_color: Color = Color.DEFAULT,

        x_axis_tick_labels: Optional[TickValues] = None,
        y_axis_tick_label_decimal_places: int = 1,

        x_axis_description: Optional[str] = None,
        y_axis_description: Optional[str] = None,
        axis_description_color: Color = Color.DEFAULT,

        title: Optional[str] = None,
        title_color: Color = Color.DEFAULT,

        horizontal_indentation: int = 0,
        center_horizontally: bool = False) -> str:
    """
    >>> print(asciiize(
    ... [1, 1, 2, 3, 5, 8, 13, 21],
    ... height=15,
    ... inter_points_margin=7,
    ...
    ... x_axis_tick_labels=list(range(10, 18)),
    ... y_axis_tick_label_decimal_places=0,
    ...
    ... x_axis_description='iteration',
    ... y_axis_description='number',
    ...
    ... title='Fibonacci Sequence',
    ...
    ... horizontal_indentation=8))
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

    # Ascertain argument validity
    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of received sequence colors exceeds number of sequences')

    _max_sequence_length = max_sequence_length(sequences)
    if x_axis_tick_labels is not None and len(x_axis_tick_labels) > _max_sequence_length:
        raise ValueError(f"number of x-ticks = {len(x_axis_tick_labels)} does not match max sequence length = {_max_sequence_length}")

    if horizontal_indentation and center_horizontally:
        raise ValueError('Pass either chart_indentation > 0 or set center_chart to True')

    # Interpolate sequences if required
    if inter_points_margin:
        plot_sequences = tuple(interpolated_sequences(sequences, inter_points_margin))
    else:
        plot_sequences = sequences

    # Provide config
    config = Config(
        height=height,
        inter_points_margin=inter_points_margin,
        sequence_colors=sequence_colors,
        label_color=label_color,
        x_axis_tick_labels=x_axis_tick_labels,
        y_axis_tick_label_decimal_places=y_axis_tick_label_decimal_places,
        x_axis_description=ColoredString.get(x_axis_description, axis_description_color),
        y_axis_description=ColoredString.get(y_axis_description, axis_description_color),
        title=ColoredString.get(title, title_color),
        horizontal_indentation=horizontal_indentation,
        center_horizontally=center_horizontally
    )

    return SerializedChart.fully_rendered(config, sequences=plot_sequences)

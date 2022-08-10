from typing import List, Optional, Sequence

from asciiplot._chart.serialized import SerializedChart
from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._constants import AUTO
from asciiplot._type_aliases import TickLabelInput
from asciiplot._utils.iterables import max_element_length


def asciiize(
        *sequences: List[float],
        height: int = 5,
        inter_points_margin: int = 0,

        sequence_colors: Sequence[Color] = (Color.NONE, ),
        background_color: Color = Color.NONE,
        label_color: Color = Color.NONE,

        x_axis_tick_labels: TickLabelInput = AUTO,
        y_axis_tick_label_decimal_places: int = 0,
        axes_background_color: Color = Color.NONE,

        x_axis_description: Optional[str] = None,
        y_axis_description: Optional[str] = None,
        axis_description_color: Color = Color.NONE,

        title: Optional[str] = None,
        title_color: Color = Color.NONE,

        horizontal_indentation: int = 0,
        center_horizontally: bool = False) -> str:
    r"""
    >>> print(asciiize(
    ... [1, 1, 2, 3, 5, 8, 13, 21],
    ... height=15,
    ... inter_points_margin=7,
    ...
    ... x_axis_tick_labels='auto',
    ... y_axis_tick_label_decimal_places=0,
    ...
    ... x_axis_description='iteration',
    ... y_axis_description='number',
    ...
    ... title='Fibonacci Sequence'))
                             Fibonacci Sequence
     number
    21┤                                                 ╭──────
    20┤                                                ╭╯
    18┤                                               ╭╯
    17┤                                             ╭─╯
    15┤                                           ╭─╯
    14┤                                          ╭╯
    12┤                                        ╭─╯
    11┤                                      ╭─╯
    10┤                                   ╭──╯
     8┤                                 ╭─╯
     7┤                             ╭───╯
     5┤                          ╭──╯
     4┤                   ╭──────╯
     2┤            ╭──────╯
     1┼───────┬────╯──┬───────┬───────┬───────┬───────┬───────┬ iteration
      1       2       3       4       5       6       7       8

    >>> print(asciiize(
    ... [12, 8, 5, 3, -1, 2, 4, 7, 12],
    ...
    ... height=14,
    ... inter_points_margin=3,
    ...
    ... x_axis_tick_labels='auto',
    ... x_axis_description='x',
    ... y_axis_description='y',
    ...
    ... title='Parabola'))
                      Parabola
      y
    12┼─╮                            ╭─
    11┤ ╰╮                           │
    10┤  ╰╮                         ╭╯
     9┤   ╰╮                       ╭╯
     8┤    ╰╮                     ╭╯
     7┤     ╰╮                   ╭╯
     6┤      ╰╮                 ╭╯
     5┤       ╰─╮              ╭╯
     4┤         ╰─╮          ╭─╯
     3┤           ╰╮       ╭─╯
     2┤            ╰╮     ╭╯
     1┤             ╰╮  ╭─╯
     0┤              ╰╮╭╯
    -1┬───┬───┬───┬───├╯──┬───┬───┬───┬ x
      1   2   3   4   5   6   7   8   9

    >>> print(asciiize([1, 9, 5], height=8, y_axis_tick_label_decimal_places=1))
    9.0┤╭╮
    7.9┤││
    6.7┤││
    5.6┤│╰
    4.4┤│
    3.3┤│
    2.1┤│
    1.0┼┤┬
       123"""

    # Assert argument validity
    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of received sequence colors exceeds number of sequences')

    if horizontal_indentation and center_horizontally:
        raise ValueError('Pass either chart_indentation > 0 or set center_chart to True')

    config = Config(
        height=height,
        inter_points_margin=inter_points_margin,
        n_points=max_element_length(sequences),
        sequence_colors=sequence_colors,
        background_color=background_color,
        label_color=label_color,
        x_axis_tick_label_input=x_axis_tick_labels,
        y_axis_tick_label_decimal_places=y_axis_tick_label_decimal_places,
        tick_label_background_color=axes_background_color,
        x_axis_description=ColoredString.get(x_axis_description, axis_description_color),
        y_axis_description=ColoredString.get(y_axis_description, axis_description_color),
        title=ColoredString.get(title, title_color),
        horizontal_indentation=horizontal_indentation,
        center_horizontally=center_horizontally
    )

    return SerializedChart.fully_rendered(config, sequences=sequences)

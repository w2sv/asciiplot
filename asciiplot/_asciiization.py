from asciiplot._chart.grid import ChartGrid
from asciiplot._params import Params
from asciiplot._sequence_interpolation import interpolate_sequences
from typing import List, Optional, Sequence, Tuple

from asciiplot._chart.serialized.layout_elements import with_layout_elements
from asciiplot._coloring import Color, ColoredString
from asciiplot._config import Config
from asciiplot._constants import AUTO
from asciiplot._type_aliases import TickLabelInput
from asciiplot._utils.iterables import max_element_length


def asciiize(*sequences: List[float],
             height: int = 5,
             inter_points_margin: int = 0,

             sequence_colors: Sequence[Color] = (Color.DEFAULT,),
             background_color: Color = Color.DEFAULT,
             label_color: Color = Color.DEFAULT,
             label_background_color: Color = Color.DEFAULT,

             x_axis_tick_labels: TickLabelInput = AUTO,
             y_axis_tick_label_decimal_places: int = 0,

             x_axis_description: Optional[str] = None,
             y_axis_description: Optional[str] = None,
             axis_description_color: Color = Color.DEFAULT,

             title: Optional[str] = None,
             title_color: Color = Color.DEFAULT,

             indentation: int = 0,
             center_horizontally: bool = False) -> str:
    r"""
    >>> print(asciiize(
    ... [1, 1, 2, 3, 5, 8, 13, 21],
    ... height=20,
    ... inter_points_margin=7,
    ...
    ... x_axis_tick_labels=AUTO,
    ... y_axis_tick_label_decimal_places=0,
    ...
    ... x_axis_description='iteration',
    ... y_axis_description='number',
    ...
    ... title='Fibonacci Sequence'))
                             Fibonacci Sequence
    number
    21┤                                                      ╭─
    20┤                                                     ╭╯
    19┤                                                    ╭╯
    18┤                                                   ╭╯
    17┤                                                  ╭╯
    16┤                                                 ╭╯
    15┤                                                ╭╯
    14┤                                               ╭╯
    13┤                                              ╭╯
    12┤                                            ╭─╯
    10┤                                           ╭╯
     9┤                                         ╭─╯
     8┤                                       ╭─╯
     7┤                                     ╭─╯
     6┤                                  ╭──╯
     5┤                               ╭──╯
     4┤                           ╭───╯
     3┤                       ╭───╯
     2┤               ╭───────╯
     1┼───────┬───────┤───────┬───────┬───────┬───────┬───────┬ iteration
      1       2       3       4       5       6       7       8

    >>> print(asciiize(
    ... [12, 8, 5, 3, -1, 2, 4, 7, 12],
    ...
    ... height=14,
    ... inter_points_margin=3,
    ...
    ... x_axis_tick_labels=AUTO,
    ... x_axis_description='x',
    ... y_axis_description='y',
    ...
    ... title='Parabola'))
                      Parabola
      y
    12┼╮                              ╭
    11┤╰╮                            ╭╯
    10┤ ╰╮                          ╭╯
     9┤  ╰╮                         │
     8┤   ╰╮                       ╭╯
     7┤    ╰─╮                    ╭╯
     6┤      ╰╮                 ╭─╯
     5┤       ╰╮               ╭╯
     4┤        ╰─╮            ╭╯
     3┤          ╰─╮        ╭─╯
     2┤            ╰╮     ╭─╯
     1┤             ╰╮   ╭╯
     0┤              ╰╮ ╭╯
    -1┬───┬───┬───┬───├─╯─┬───┬───┬───┬ x
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
       123 """

    if len(sequence_colors) > len(sequences):
        raise ValueError('Number of received sequence colors exceeds number of sequences')
    if indentation and center_horizontally:
        raise ValueError('Pass either an indentation OR set center_horizontally to True')

    config = Config(
        height=height,
        inter_points_margin=inter_points_margin,
        n_points=max_element_length(sequences),
        sequence_colors=sequence_colors,
        background_color=background_color,
        label_color=label_color,
        x_axis_tick_label_input=x_axis_tick_labels,
        y_axis_tick_label_decimal_places=y_axis_tick_label_decimal_places,
        tick_label_background_color=label_background_color,
        x_axis_description=ColoredString.make_if_string_present(x_axis_description, axis_description_color),
        y_axis_description=ColoredString.make_if_string_present(y_axis_description, axis_description_color),
        title=ColoredString.make_if_string_present(title, title_color),
        indentation=indentation,
        center_horizontally=center_horizontally
    )

    plot_sequences = _plot_sequences(sequences, config.inter_points_margin)
    params = Params.compute(plot_sequences, config=config)

    return with_layout_elements(
        ChartGrid.get_fully_rendered(plot_sequences, config=config, params=params).serialized(),
        config,
        params
    )


def _plot_sequences(sequences: Tuple[List[float], ...], inter_points_margin: int) -> Tuple[List[float], ...]:
    if inter_points_margin:
        return tuple(interpolate_sequences(sequences, inter_points_margin))
    return sequences

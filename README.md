# __asciiplot__

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asciiplot)
[![Build](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml/badge.svg)](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/w2sv/asciiplot/branch/master/graph/badge.svg?token=69Q1VL8IHI)](https://codecov.io/gh/w2sv/asciiplot)
[![PyPI](https://img.shields.io/pypi/v/asciiplot)](https://pypi.org/project/asciiplot)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/w2sv/asciiplot)
![PyPI - Downloads](https://img.shields.io/pypi/dm/asciiplot)
[![GitHub](https://img.shields.io/github/license/w2sv/asciiplot?style=plastic)](https://github.com/w2sv/asciiplot/blob/master/LICENSE)

#### Platform-agnostic sequence plotting in console, offering various chart appearance configuration options giving rise to an increased GUI suitability

## Installation
```shell
$pip install asciiplot
```

## Plot Appearance Configuration Options

Set:
- chart height & title
- axes descriptions & tick labels, including the possibility to determine the number of decimal points for float labels
- the color of virtually all chart components, picked from a wide array of shades due to the integration of [colored](https://pypi.org/project/colored/)
- consistent margin between consecutive data points to widen your charts
- the chart indentation within its hosting terminal, or whether it ought to be centered in it, respectively

## Usage Examples

```python
from asciiplot import asciiize


print(
    asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],

        height=15,
        inter_points_margin=7,

        x_axis_tick_labels=list(range(1, 9)),
        y_axis_tick_label_decimal_places=0,

        x_axis_description='Iteration',
        y_axis_description='Value',

        title='Fibonacci Sequence',
        horizontal_indentation=6
    )
)
```

                        Fibonacci Sequence
     Value
      21┤                                                     ╭──
      19┤                                                    ╭╯
      18┤                                                   ╭╯
      16┤                                                  ╭╯
      15┤                                                ╭─╯
      13┤                                              ╭─╯
      12┤                                            ╭─╯
      11┤                                          ╭─╯
       9┤                                        ╭─╯
       8┤                                     ╭──╯
       6┤                                 ╭───╯
       5┤                             ╭───╯
       3┤                       ╭─────╯
       2┤             ╭─────────╯
       1┼───────┬─────╯─┬───────┬───────┬───────┬───────┬───────┬ Iteration
        1       2       3       4       5       6       7       8

```python
import numpy as np
from asciiplot import asciiize


print(
    asciiize(
        np.random.randint(-100, 100, 30),
        np.random.randint(-100, 100, 30),

        height=10,
        inter_points_margin=2,

        x_axis_tick_labels=list(range(1, 31)),
        y_axis_tick_label_decimal_places=1,

        title='Random Values',
        horizontal_indentation=6
    )
)
```

                                             Random Values
        96.0┤        ╭╮    ╭──╭╮──╮               ╭──╮   ╭╮       ╭╮    ╭╮          ╭───────╮  ╭─╮
        74.2┤  ╭╮    ││    │  ││  │               │  ╰╮ ╭╯│      ╭╯│   ╭╯╰╮        ╭╯──╯│   ╰╮╭╯ │
        52.4┤ ╭╭╮╮  ╭╯╰╮  ╭╯ ╭╯│  ╰╮   ╭╮    ╭──╮╭╯   │╭╯ ╰╮   ╭─╯ ╰╮╭╮│  │       ╭╯│   │    ╰╯  ╰╮
        30.7┤╭╯│╰╮╮╭╯  │  │  │ ╰╮  │   ││   ╭╯  ╰╯    ╰╯   │   │    ││││  ╰╮     ╭╯╭╯   ╰╮        │
         8.9┼╯╭╯ │╰╯   │ ╭╯  │  │  │   ╭╮╮  │╭╮            ╰╮ ╭╯    ╭╯╰╮   │     │╭╯     │        │
       -12.9┤╭╯  ╰╮    ╰╮│  ╭╯  │  │ ╭─╯╰╮╮╭╭╯│             │╭╯    ╭╯│││   ╭╮╮  ╭╯╯      │        ╰╮
       -34.7┤│    │     ╭╮  │   ╰╮ ╰╭╯│  ╰╮╭╯ ╰╮     ╭───╮  ││    ╭╯ ╰╯╰╮ ╭╯│╰──│        ╰╮  ╭──╮ ╭│
       -56.4┼╯    ╰─╮  ╭╯╰──╯    │ ╭╯╭╯   ││   ╰╮   ╭╯   ╰─╮╰╯  ╭─╯     ╰─╯ ╰╮ ╭╯         │ ╭╯  ╰─╯╰
       -78.2┤       ╰──╯         │╭╯││    ╰╯    │ ╭─╯      ╰╮ ╭─╯            ╰╮│          │╭╯
      -100.0┼──┬──┬──┬──┬──┬──┬──├╯─├╯─┬──┬──┬──├─╯┬──┬──┬──├─╯┬──┬──┬──┬──┬──├╯─┬──┬──┬──├╯─┬──┬──┬ 
            1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30


## Acknowledgements
Core sequence asciiization algorithm adopted from https://github.com/kroitor/asciichart/blob/master/asciichartpy/


## License
[MIT License](https://github.com/w2sv/asciiplot/blob/master/LICENSE)

# __asciiplot__

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml/badge.svg)](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/w2sv/asciiplot/branch/master/graph/badge.svg?token=69Q1VL8IHI)](https://codecov.io/gh/w2sv/asciiplot)
![PyPI](https://img.shields.io/pypi/v/asciiplot)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
#### Platform-agnostic sequence plotting in console, offering various chart appearance configuration options and thus giving rise to an increased degree of GUI suitability

### Install
```shell
$ pip install asciiplot
```

### Plot configuration options

- Setting of consistent margin between data points
- Determination of chart height
- Setting of chart title
- Axes descriptions display
- Setting of x-axis tick labels, possibly being of both numeric and string type
- Determination of y-axis tick label decimal points
- Centering the chart within the target terminal or indenting it by a passed number of columns respectively
- Setting color of all chart components due to integration of [colored](https://pypi.org/project/colored/)

### Examples

```python
from asciiplot import asciiize

print(
    asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        
        height=15,
        inter_points_margin=7,

        x_ticks=list(range(1, 9)),
        y_ticks_decimal_places=0,

        x_axis_description='Iteration',
        y_axis_description='Value',

        title='Fibonacci Sequence',
        indentation=6
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
    
        x_ticks=list(range(1, 31)),
        y_ticks_decimal_places=1,
    
        title='Random Values',
        indentation=6
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

### References
Core sequence asciiization algorithm adopted from https://github.com/kroitor/asciichart/blob/master/asciichartpy/


### License
[MIT License](https://github.com/w2sv/asciiplot/blob/master/LICENSE)

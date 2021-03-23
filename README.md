# __asciiplot__

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)

#### Lightweight, cross-platform asciiized sequence plotting in console, prompted by invocation of one singular function

### Install
```shell
pip install asciiplot
```

### References
Core sequence asciiization algorithm adopted from
kroitor @ https://github.com/kroitor/asciichart/blob/master/asciichartpy/__init__.py

### Plot configuration options

- possibility to set a consistent margin between data points through ```in_between_points_margin``` parameter
- determination of chart height
- possibility of title and axes descriptions display
- setting of x-axis labels, possibly being of both numeric and string type
- determination of number of y-axis label decimal points
- centering the resulting plot within the target terminal or indenting it by a passed number of columns respectively
- color determination of all chart components, picking from wide array of colors thanks to the incorporation of [colored](https://pypi.org/project/colored/)

### Usage

- Obtain chart with asciiized sequences as by calling ```asciiize(*sequences, **kwargs)```
- Valid color names may be retrieved through ```print(asciiplot.color_names)``` 

### Examples

```python
print(
    asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        chart_height=15,
        in_between_points_margin=7,

        sequence_colors=['DARK_MAGENTA_1'],
        label_color='VIOLET',

        x_labels=list(range(1, 9)),
        y_label_decimal_places=0,

        x_axis_description='iteration',
        y_axis_description='number',
        axis_description_color='MEDIUM_PURPLE',

        title='Fibonacci Sequence',
        title_color='LIGHT_RED',

        chart_indentation=6
    )
)


>>>                        Fibonacci Sequence
     number
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
       1┼───────┬─────╯─┬───────┬───────┬───────┬───────┬───────┬ iteration
        1       2       3       4       5       6       7       8
```
```python
import numpy as np

print(
    asciiize(
        np.random.randint(-100, 100, 30),
        np.random.randint(-100, 100, 30),
        chart_height=10,
        in_between_points_margin=2,
    
        sequence_colors=['DARK_MAGENTA_1', 'CYAN'],
        label_color='VIOLET',
    
        x_labels=list(range(1, 31)),
        y_label_decimal_places=1,
    
        x_axis_description='attempt',
        y_axis_description='drawn value',
        axis_description_color='MEDIUM_PURPLE',
    
        title='np.randint values',
        title_color='LIGHT_RED',
    
        chart_indentation=6
    )
)

>>>                                             np.randint values
       drawn value
        96.0┤        ╭╮    ╭──╭╮──╮               ╭──╮   ╭╮       ╭╮    ╭╮          ╭───────╮  ╭─╮
        74.2┤  ╭╮    ││    │  ││  │               │  ╰╮ ╭╯│      ╭╯│   ╭╯╰╮        ╭╯──╯│   ╰╮╭╯ │
        52.4┤ ╭╭╮╮  ╭╯╰╮  ╭╯ ╭╯│  ╰╮   ╭╮    ╭──╮╭╯   │╭╯ ╰╮   ╭─╯ ╰╮╭╮│  │       ╭╯│   │    ╰╯  ╰╮
        30.7┤╭╯│╰╮╮╭╯  │  │  │ ╰╮  │   ││   ╭╯  ╰╯    ╰╯   │   │    ││││  ╰╮     ╭╯╭╯   ╰╮        │
         8.9┼╯╭╯ │╰╯   │ ╭╯  │  │  │   ╭╮╮  │╭╮            ╰╮ ╭╯    ╭╯╰╮   │     │╭╯     │        │
       -12.9┤╭╯  ╰╮    ╰╮│  ╭╯  │  │ ╭─╯╰╮╮╭╭╯│             │╭╯    ╭╯│││   ╭╮╮  ╭╯╯      │        ╰╮
       -34.7┤│    │     ╭╮  │   ╰╮ ╰╭╯│  ╰╮╭╯ ╰╮     ╭───╮  ││    ╭╯ ╰╯╰╮ ╭╯│╰──│        ╰╮  ╭──╮ ╭│
       -56.4┼╯    ╰─╮  ╭╯╰──╯    │ ╭╯╭╯   ││   ╰╮   ╭╯   ╰─╮╰╯  ╭─╯     ╰─╯ ╰╮ ╭╯         │ ╭╯  ╰─╯╰
       -78.2┤       ╰──╯         │╭╯││    ╰╯    │ ╭─╯      ╰╮ ╭─╯            ╰╮│          │╭╯
      -100.0┼──┬──┬──┬──┬──┬──┬──├╯─├╯─┬──┬──┬──├─╯┬──┬──┬──├─╯┬──┬──┬──┬──┬──├╯─┬──┬──┬──├╯─┬──┬──┬ attempt
            1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
```

### License
[MIT License](https://github.com/w2sv/asciiplot/blob/master/LICENSE.txt)

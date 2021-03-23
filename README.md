# __ASCIIPLOT__

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)

#### Lightweight, cross-platform terminal sequence plotting package comprising one singular function enabling the asciiization of sequence(s), whilst allowing to configure the thus created chart via a variety of options

### Install
```shell
pip install asciiplot
```

### Examples

```python

print(asciiize(
        [45, 9, 28, 0, 87, 57, 64, 3, 3, 6, 74, 1],
        [6, 9, 22, 86, -3, 86, 100],
        n_plot_rows=10,
        columns_between_points=4,

        sequence_colors=['DARK_MAGENTA_1', 'CYAN'],
        label_color='VIOLET',

        x_labels=list(range(12)),
        y_label_decimal_places=1,

        axis_description_color='MEDIUM_PURPLE',

        title='Radical Plot',
        title_color='LIGHT_RED',

        label_column_offset=6
    ))

>>>                                 Radical Plot
      100.0┤              ╭╮   ╭╮   ╭─────
       88.6┤              ││   │╰─╮ │
       77.1┤             ╭╯╰╮ ╭╯  ╰╭╯    ╭╮                  ╭╮
       65.7┤            ╭╯  │ │    │─────╯│                 ╭╯╰╮
       54.2┼╮          ╭╯   ╰╮╯   ╭╯      ╰╮               ╭╯  ╰╮
       42.8┤╰╮        ╭╯    ╭│    │        ╰╮             ╭╯    │
       31.3┤ ╰─╮    ╭─│     │╰╮  ╭╯         ╰╮            │     ╰╮
       19.9┤   ╰╮╭╭───╯─╮  ╭╯ ╰╮╭╯           ╰╮          ╭╯      ╰╮
        8.4┼──────╯     ╰─╮│   ││             ╰──────────╯        │
       -3.0┼────┬────┬────├╯───├╯───┬────┬────┬────┬────┬────┬────├
           0    1    2    3    4    5    6    7    8    9    10   11
```
```python
import numpy as np

print(asciiize(
        np.random.randint(-100, 100, 30),
        np.random.randint(-100, 100, 30),
        n_plot_rows=10,
        columns_between_points=2,
    
        sequence_colors=['DARK_MAGENTA_1', 'CYAN'],
        label_color='VIOLET',
    
        x_labels=list(range(30)),
        y_label_decimal_places=1,
    
        axis_description_color='MEDIUM_PURPLE',
    
        title='Arbitrary Plot',
        title_color='LIGHT_RED',
    
        label_column_offset=6
    )
)

>>>                                         Arbitrary Plot
       98.0┤        ╭─╮   ╭──────╮                 ╭──╮       ╭╮             ╭──╮     ╭╮
       76.1┤  ╭╮    │ ╰╮ ╭╯      │    ╭╮          ╭╯  ╰╮      │╰╮           ╭╭╮ ╰╮   ╭╯│       ╭───
       54.2┤  ││   ╭╯  │╭╯       ╰╮   │╰╮╭╮ ╭╮    │  ╭╮│   ╭╮╭╯ ╰╮         ╭╯││  ╰╮  │─╰╮     ╭╯
       32.3┤ ╭│╰╮  │   ╰╯         │  ╭╯ ╭╯│╭╯│   ╭╯╭─╯╰│  ╭╯││   │╮       ╭╯╭╯╰╮  ╰╮╭╯ ││    ╭╯
       10.4┤ ╭╯ │  │             ╭───╮ ╭╯╰╰╮ ╰╮  │╭╯   ╰╮╭╯ ╰│  ╭╰╮╮   ╭╮╭╯ │  │   ╰│  ╰╰╮  ╭╯ ╭╮
      -11.4┤╭│  ╰╮╭╯           ╭─╯ ││╰╮│   │  ╰╮ │╯     │╯  ╭╯╮╭╯ ╰╮╮ ╭╯╰╮ ╭╯  ╰╮  ╭╯   ││ ╭╯  │╰─╮
      -33.3┼╭╯  ╰││           ╭╯   ╰╯ ╰╯   ╰╮  │╭╯      ╰╮  │ ││   ╰╮╭│─╯╰╮│    │ ╭╯    ╰│╭╯  ╭╯  ╰
      -55.2┤│    ╰──────╮   ╭─╯             │  ╰│        ╰─╮│ ╰╯    │╭╯   ╰╯    │╭╯      ╰╯  ╭╯
      -77.1┤│    ╰╯     ╰─╮╭╯               ╰─╮ │          ╰╯       ╰╯          ╰╯       │   │
      -99.0┼╯─┬──┬──┬──┬──├╯─┬──┬──┬──┬──┬──┬─╰┬╯─┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──├──┬╯─┬──┬
           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
```

### License
[MIT License](https://github.com/w2sv/asciiplot/blob/master/LICENSE.txt)

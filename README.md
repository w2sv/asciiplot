# __asciiplot__

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asciiplot)
[![Build](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml/badge.svg)](https://github.com/w2sv/asciiplot/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/w2sv/asciiplot/branch/master/graph/badge.svg?token=69Q1VL8IHI)](https://codecov.io/gh/w2sv/asciiplot)
[![PyPI](https://img.shields.io/pypi/v/asciiplot)](https://pypi.org/project/asciiplot)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/w2sv/asciiplot)
![PyPI - Downloads](https://img.shields.io/pypi/dm/asciiplot)
[![GitHub](https://img.shields.io/github/license/w2sv/asciiplot?style=plastic)](https://github.com/w2sv/asciiplot/blob/master/LICENSE)

#### Platform-agnostic, highly customizable sequence plotting in console

## Installation
```shell
$pip install asciiplot
```

## Plot Appearance Configuration Options

Set:
- chart height & title
- the color of virtually all chart components and areas, picked from a wide array of shades due to the integration of [colored](https://pypi.org/project/colored/)
- consistent margin between consecutive data points to widen your chart
- the chart indentation within its hosting terminal, or whether it ought to be centered in it, respectively
- axes descriptions
- x-axis tick labels, which may be set to contain strings instead of just numeric values
- y-axis tick label decimal places

## Usage Examples

```python
from asciiplot import asciiize, Color


print(
    asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        sequence_colors=[Color.BLUE_3B],
        height=21,
        inter_points_margin=5,
        background_color=Color.LIGHT_SALMON_1,
        label_color=Color.BLUE_VIOLET,
        axes_background_color=Color.DEEP_PINK_3A,
        title='Fibonacci',
        title_color=Color.RED_1,
        x_axis_description='x',
        y_axis_description='y',
        center_horizontally=True
    )
)
```
![alt text](https://github.com/w2sv/asciiplot/blob/master/readme-images/fibonacci.png?raw=true)

```python
from asciiplot import asciiize, Color


print(
    asciiize(
        [17, 21, 19, 19, 5, 7, 12, 4],
        [7, 8, 3, 17, 19, 18, 5, 2, 20],
        sequence_colors=[Color.RED, Color.BLUE_VIOLET],
        inter_points_margin=5,
        height=20,
        background_color=Color.GREY_7,
        title='Random Sequences',
        title_color=Color.MEDIUM_PURPLE,
        label_color=Color.MEDIUM_PURPLE,
        x_axis_description='x',
        y_axis_description='y',
        center_horizontally=True
    )
)
```
![alt text](https://github.com/w2sv/asciiplot/blob/master/readme-images/random.png?raw=true)

## Acknowledgements
Core sequence asciiization algorithm adopted from https://github.com/kroitor/asciichart/blob/master/asciichartpy/

## Testing

```shell
git clone https://github.com/w2sv/asciiplot.git
cd asciiplot
poetry install
make test  # runs mypy, pytest doctest and outputs test coverage
```

## License
[MIT License](https://github.com/w2sv/asciiplot/blob/master/LICENSE)

""" Core sequence asciiization algorithm adopted from
kroitor@https://github.com/kroitor/asciichart/blob/master/asciichartpy/__init__.py

Package functionality comprising:
    - wide array of eligible colors thanks to the incorporation of https://pypi.org/project/colored/
    - ability of setting the color of all chart components
    - enablement of cross-platform usage
    - possibility to set a consistent margin between data points through in_between_points_margin
    - determination of chart height
    - possibility of title and axes descriptions display
    - adding of x-axes with determinable labels, possibly being of both numeric and string type
    - centering the resulting plot within the target terminal or indenting it by a passed number of columns respectively """


from asciiplot.version import __version__
from asciiplot._asciiization import asciiize
from asciiplot._coloring import Color


if __name__ == '__main__':
    print(asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        height=15,
        inter_points_margin=7,

        sequence_colors=[Color.CYAN],
        label_color=Color.DARK_VIOLET_1A,

        x_ticks=list(range(10, 18)),
        y_ticks_decimal_places=0,

        x_axis_description='iteration',
        y_axis_description='number',
        axis_description_color=Color.MEDIUM_TURQUOISE,

        title='Fibonacci Sequence',
        title_color=Color.AQUAMARINE_1A,

        indentation=8
    ))

    print(asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        height=15,
        inter_points_margin=7,

        x_ticks=list(range(10, 18)),
        y_ticks_decimal_places=0,

        x_axis_description='iteration',
        y_axis_description='number',

        title='Fibonacci Sequence',
        indentation=8
    ))

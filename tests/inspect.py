from asciiplot._asciiization import asciiize
from asciiplot._coloring import Color


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

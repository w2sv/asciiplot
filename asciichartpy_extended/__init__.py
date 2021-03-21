""" Refactored, as well as extended fork of asciichartpy to be found at
https://github.com/kroitor/asciichart/tree/master/asciichartpy """


from asciichartpy_extended.version import __version__
from asciichartpy_extended._rendering import asciiize
from asciichartpy_extended._variable_encapsulations._config import Config
from asciichartpy_extended._coloring import colors


if __name__ == '__main__':
    p = asciiize([16, 13, 2, 19], config=Config(
        y_axis_description='SWAG',
        y_label_decimal_places=1,
        columns_between_points=3,
        n_plot_rows=3,
        sequence_colors=[colors.RED, colors.GREEN],
        display_x_axis=True,
        title='SICKPLOT',
        x_labels={0: 0, 1: 1, 2: 2, 3: 9},
        axis_description_color=colors.GREEN,
        x_axis_label_color=colors.MAGENTA
    ))

    print(p)

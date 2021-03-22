""" Refactored, as well as extended fork of asciichartpy to be found at
https://github.com/kroitor/asciichart/tree/master/asciichartpy """


from asciiplot.version import __version__
from asciiplot._rendering import asciiize
from asciiplot._variable_encapsulations._config import Config
from asciiplot._coloring import colors


if __name__ == '__main__':
    p = asciiize([-1, 5, -30, 9], config=Config(
        y_axis_description='SWAG',
        x_axis_description='FLOWYO',
        y_label_decimal_places=1,
        columns_between_points=20,
        n_plot_rows=7,
        sequence_colors=[colors.RED, colors.GREEN],
        title='SICKPLOT',
        x_labels=[None, None, 4, 8],
        axis_description_color=colors.GREEN,
        label_color=colors.MAGENTA,
        center_plot=True
    ))

    print(p)
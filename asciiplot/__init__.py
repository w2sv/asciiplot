""" Refactored, as well as extended fork of asciichartpy to be found at
https://github.com/kroitor/asciichart/tree/master/asciichartpy """


from asciiplot.version import __version__
from asciiplot._rendering import asciiize
from colored.colors import names as color_names


if __name__ == '__main__':
    # import numpy as np
    #
    # seq = np.random.randint(-100, 100, 30)
    # seq1 = np.random.randint(-100, 100, 30)
    #
    # p = asciiize(
    #     seq,
    #     seq1,
    #     n_plot_rows=10,
    #     columns_between_points=2,
    #
    #     sequence_colors=['DARK_MAGENTA_1', 'CYAN'],
    #     label_color='VIOLET',
    #
    #     x_labels=list(range(30)),
    #     y_label_decimal_places=1,
    #
    #     axis_description_color='MEDIUM_PURPLE',
    #
    #     title='Arbitrary Plot',
    #     title_color='LIGHT_RED',
    #
    #     label_column_offset=6
    # )
    #
    # print(p)

    print(asciiize([4, 5, 6]))

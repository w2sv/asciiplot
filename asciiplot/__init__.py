""" Refactored, as well as extended fork of asciichartpy to be found at
https://github.com/kroitor/asciichart/tree/master/asciichartpy """


from asciiplot.version import __version__
from asciiplot._rendering import asciiize
from colored.colors import names as color_names


if __name__ == '__main__':
    p = asciiize(
        [-1, 5, -30, 9],
        # label_column_offset=20,
        y_axis_description='SWAG',
        x_axis_description='FLOWYO',
        y_label_decimal_places=1,
        columns_between_points=20,
        n_plot_rows=7,
        sequence_colors=['DARK_MAGENTA_1'],
        title='SICKPLOT',
        x_labels=[None, None, 4, 8],
        axis_description_color='MEDIUM_PURPLE',
        label_color='VIOLET',
        center_plot=True
    )

    print(p)

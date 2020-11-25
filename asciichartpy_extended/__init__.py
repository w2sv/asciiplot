from asciichartpy_extended.version import __version__
from asciichartpy_extended._rendering import asciiize
from asciichartpy_extended._config import Config
from asciichartpy_extended import colors


if __name__ == '__main__':
    p = asciiize([3, 7, 9], config=Config(
        y_axis_description='SWAG',
        y_label_decimal_places=1,
        columns_between_points=3,
        plot_height=5,
        sequence_colors=[colors.RED, colors.GREEN],
        display_x_axis=True,
        title='SICKPLOT',
        x_labels={0: 'asdf', 1: 1, 2: 2, 3: 9},
        axis_description_color=colors.GREEN,
        x_axis_label_color=colors.MAGENTA
    ))

    print(p)

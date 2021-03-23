""" Core sequence asciiization algorithm adopted from
kroitor@https://github.com/kroitor/asciichart/blob/master/asciichartpy/__init__.py,

package extended by:
    - increased parameter passing convenience
    - extension of eligible colors
    - enablement of cross-platform usage
    - introduction of possibility to set a consistent margin between data points through columns_between_points,
    - possibility of title, axis descriptions display
    - adding of x-axes with determinable labels, possibly being of both numeric and string type,
    - centering the resulting plot within the target terminal or indenting it respectively """


from asciiplot.version import __version__
from asciiplot._rendering import asciiize
from colored.colors import names as color_names


if __name__ == '__main__':
    p = asciiize(
        [6, 4, 3, 6, 7, 4],
        [91, 4, 32, 6, 3],
        n_plot_rows=10,
        columns_between_points=2,

        sequence_colors=['DARK_MAGENTA_1', 'CYAN'],
        label_color='VIOLET',

        x_labels=list(range(6)),
        y_label_decimal_places=1,

        axis_description_color='MEDIUM_PURPLE',

        title='Arbitrary Plot',
        title_color='LIGHT_RED',

        label_column_offset=6
    )

    print(p)

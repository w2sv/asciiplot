from asciiplot import Color, asciiize


if __name__ == '__main__':
    import numpy as np

    # def sigmoid(x):
    #     return 1 / (1 + np.exp(-x))
    #
    # x = np.linspace(-5, 5, 10)
    # y = [sigmoid(x_i) for x_i in x]
    #
    # chart = asciiize(
    #     y,
    #     x_axis_tick_labels=[f'{label:.1f}' for label in x],
    #     inter_points_margin=6,
    #     height=15,
    #     x_axis_description='x',
    #     y_axis_description='y',
    #     y_axis_tick_label_decimal_places=2
    # )

    print()

    x = np.linspace(0, 2 * np.pi, 10)
    y_sin = [np.sin(x_i) for x_i in x]
    y_cos = [np.cos(x_i) for x_i in x]

    print(
        asciiize(
            y_sin,
            y_cos,
            # title="Sin & Cos",
            title_color=Color.DARK_GOLDENROD,
            sequence_colors=[Color.PURPLE_3, Color.RED_1],
            background_color=Color.BLACK,
            label_background_color=Color.DARK_GOLDENROD,
            x_axis_tick_labels=[f'{label:.1f}' for label in x],
            inter_points_margin=6,
            height=10,
            y_axis_tick_label_decimal_places=2,
            center_horizontally=True
        )
    )

    print('\n' * 3)

    print(
        asciiize(
            [0, 1, 1, 2, 3, 5, 8, 13, 21],
            height=22,
            inter_points_margin=5,
            sequence_colors=[Color.BLUE_3B],
            label_color=Color.BLUE_VIOLET,
            tick_point_color=Color.RED_1,
            title='Fibonacci',
            title_color=Color.RED_1,
            center_horizontally=True,
            background_color=Color.LIGHT_SALMON_1,
            label_background_color=Color.DEEP_PINK_3A,
            x_axis_description='x',
            y_axis_description='y'
        )
    )

    print('\n' * 3)

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

    print('\n' * 3)

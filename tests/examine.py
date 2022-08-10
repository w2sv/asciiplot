from asciiplot import Color, asciiize


if __name__ == '__main__':
    # chart = asciiize(
    #     [1, 1, 2, 3, 5, 8, 13, 21],
    #     y_axis_tick_label_decimal_places=0,
    #     height=21,
    #     inter_points_margin=5,
    #     x_axis_tick_labels='auto',
    #     sequence_colors=[Color.STEEL_BLUE],
    #     label_color=Color.BLUE_VIOLET,
    #     title='Fibonacci',
    #     title_color=Color.RED_1,
    #     center_horizontally=True,
    #     background_color=Color.LIGHT_SALMON_1,
    #     axes_background_color=Color.DEEP_PINK_3A,
    #     x_axis_description='x',
    #     y_axis_description='y'
    # )
    chart = asciiize(
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
    print(chart)
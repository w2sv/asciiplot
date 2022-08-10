from asciiplot import Color, asciiize


if __name__ == '__main__':
    chart = asciiize(
        [1, 1, 2, 3, 5, 8, 13, 21],
        y_axis_tick_label_decimal_places=0,
        height=21,
        inter_points_margin=5,
        x_axis_tick_labels=list(range(1, 9)),
        sequence_colors=[Color.STEEL_BLUE],
        label_color=Color.BLUE_VIOLET,
        title='Fibonacci',
        title_color=Color.RED_1,
        center_horizontally=True,
        background_color=Color.LIGHT_SALMON_1
    )
    print(chart)
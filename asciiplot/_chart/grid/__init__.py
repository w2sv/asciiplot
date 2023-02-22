from more_itertools import pairwise

from asciiplot._chart.grid.cell import Cell
from asciiplot._coloring import Color
from asciiplot._config import Config
from asciiplot._params import Params
from asciiplot._type_aliases import PlotSequences
from asciiplot._utils.formatting import indentation
from asciiplot._utils.numerical import clamp_value
from typing import List


class ChartGrid(List[List[Cell]]):
    @classmethod
    def get_fully_rendered(cls, plot_sequences: PlotSequences, config: Config, params: Params):
        grid = cls(config, params)
        grid.add_sequences(plot_sequences)

        grid.add_x_axis()
        grid.add_y_axis_with_tick_labels()

        grid.indent_if_applicable()
        return grid

    def __init__(self, config: Config, params: Params):
        super().__init__(
            [[Cell(bg=config.background_color) for _ in range(params.x_axis_width)] for _ in
             range(config.height)]
        )

        self._config = config
        self._params = params

        self._last_row_index = self._config.height - 1

    def add_sequences(self, sequences: PlotSequences):
        for i_sequence, sequence in enumerate(sequences):
            sequence_color = self._config.sequence_colors[i_sequence % len(self._config.sequence_colors)]

            # add '┼' at beginning where sequence overlaps with y-axis
            self._set_cell(self._x_grid_domain(sequence[0]), 0, '┼', sequence_color)

            for col_index, (x1_value_domain, x2_value_domain) in enumerate(pairwise(sequence)):
                set_cell = lambda x, segment: self._set_cell(x, col_index + 1, segment, sequence_color)

                x1 = self._x_grid_domain(x1_value_domain)
                x2 = self._x_grid_domain(x2_value_domain)

                if x1 == x2:
                    set_cell(x1, '─')
                else:
                    if x1 > x2:
                        segment_x1, segment_x2 = '╮', '╰'
                    else:
                        segment_x1, segment_x2 = '╯', '╭'

                    set_cell(x1, segment_x1)
                    set_cell(x2, segment_x2)

                    # add vertical segment in case of consecutive sequence
                    # value steepness
                    x_min, x_max = sorted([x1, x2])
                    for x in range(x_min + 1, x_max):
                        set_cell(x, '│')

    def _set_cell(self, x: int, y: int, segment: str, color: Color):
        self[self._last_row_index - x][y].set_foreground(segment, color)

    def _x_grid_domain(self, x_original_domain: float) -> int:
        return clamp_value(
            int((x_original_domain - self._params.y_min) * self._params.i_row_per_y),
            lower_bound=0,
            upper_bound=self._last_row_index
        )

    def add_x_axis(self):
        for i, cell in enumerate(self[-1]):
            # add straight horizontal axis segment if parcel doesn't contain
            # a sequence segment, otherwise convert present sequence segment
            # to one comprising both the sequence and axis segment in color
            # of respective sequence

            is_data_point = self._is_data_point(i)

            if cell.is_empty:
                self[-1][i].replace_string('┬' if is_data_point else '─')
            elif is_data_point:
                self[-1][i].replace_string_if_applicable(
                    replacements={
                        '┤': '┼',
                        '─': '┬',
                        '╰': '├',
                        '╯': '┤'
                    }
                )

    def add_y_axis_with_tick_labels(self):
        for i in range(len(self)):
            if self[i][0].is_empty:
                self[i][0].replace_string('┤')
            else:
                self[i][0].replace_string_if_applicable(
                    replacements={
                        '─': '┤',
                        '|': '┼',
                        '┬': '┼'
                    }
                )

            # insert tick label
            self[i].insert(
                0,
                Cell(
                    self._params.y_axis_tick_labels[i].rjust(self._params.y_tick_column_width),
                    fg=self._config.label_color,
                    bg=self._config.tick_label_background_color
                )
            )

    def _is_data_point(self, point_index: int) -> bool:
        """ Returns:
                flag whether point corresponding to point_index is actual
                data point denoted in original sequences instead of interpolated
                one """

        return not point_index % (self._config.inter_points_margin + 1)

    def indent_if_applicable(self):
        if self._params.indentation:
            for i in range(len(self)):
                self[i].insert(0, Cell(indentation(self._params.indentation)))

    def serialized(self) -> str:
        return '\n'.join((''.join(str(cell) for cell in row).rstrip() for row in self))

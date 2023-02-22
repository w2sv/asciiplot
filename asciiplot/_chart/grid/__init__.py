from more_itertools import pairwise

from asciiplot._chart.grid.cell import Cell
from asciiplot._coloring import Color
from asciiplot._config import Config
from asciiplot._params import Params
from asciiplot._type_aliases import PlotSequences
from asciiplot._utils.formatting import indentation
from asciiplot._utils.numerical import clamp_value
from functools import partial
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
            set_sequence_cell = partial(
                self._set_cell,
                color=self._config.sequence_colors[i_sequence % len(self._config.sequence_colors)]
            )

            # add '┼' at beginning where sequence overlaps with y-axis
            set_sequence_cell('┼', self._row_index(sequence[0]), 0)

            # asciiize sequence
            for i_point_a, i_point_b in pairwise(range(len(sequence))):
                set_cell_at_col = partial(set_sequence_cell, i_col=i_point_b)

                y0 = self._row_index(sequence[i_point_a])
                y1 = self._row_index(sequence[i_point_b])

                if y0 == y1:
                    set_cell_at_col('─', y0)
                else:
                    if y0 > y1:
                        symbol_y0, symbol_y1 = '╮', '╰'
                    else:
                        symbol_y0, symbol_y1 = '╯', '╭'

                    set_cell_at_col(symbol_y0, y0)
                    set_cell_at_col(symbol_y1, y1)

                    # add vertical segment in case of consecutive sequence
                    # value steepness
                    for y in range(min(y0, y1) + 1, max(y0, y1)):
                        set_cell_at_col('│', y)

    def _set_cell(self, segment: str, i_row: int, i_col: int, color: Color):
        self[self._last_row_index - i_row][i_col] = Cell(
            segment,
            fg=color,
            bg=self._config.background_color
        )

    def _row_index(self, value: float) -> int:
        return clamp_value(
            int((value - self._params.y_min) * self._params.i_row_per_y),
            lower_bound=0,
            upper_bound=self._last_row_index
        )

    def serialized(self) -> str:
        return '\n'.join((''.join(str(cell) for cell in row).rstrip() for row in self))

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
        """ Besets first parcel of each row with respective y-axis segment
            preceded by colored, adjusted tick value """

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

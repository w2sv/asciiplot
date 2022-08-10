from typing import List

from asciiplot._chart.grid.cell import Cell
from asciiplot._config import Config
from asciiplot._params import Params
from asciiplot._utils import terminal_width
from asciiplot._utils.formatting import centering_indentation_len, indented
from asciiplot._type_aliases import PlotSequences


class ChartGrid(List[List[Cell]]):
    def __init__(self, plot_sequences: PlotSequences, config: Config, params: Params):
        self._config = config
        self._params = params

        super().__init__([[Cell(bg=config.background_color) for _ in range(self._params.x_axis_width)] for _ in range(self._config.height)])

        self._add_sequences(plot_sequences)

        self._add_x_axis()
        self._add_y_axis_with_tick_labels()

        self._indent_if_applicable()

    def _add_sequences(self, sequences: PlotSequences):
        SEGMENTS = ('┼', '─', '╰', '╭', '╮', '╯', '│')
        INIT_VALUE = -1

        def row_index(value: float) -> int:
            """ Scales sequence point clamped to desired extrema to
            corresponding point within chart value range """

            def clamp_to_row_index_bounds(row_index: int) -> int:
                return max(min(row_index, self._config.height - 1), 0)

            return clamp_to_row_index_bounds(row_index=int(round((value - self._params.y_min) * self._params.delta_row_index_per_y)))

        for i, sequence in enumerate(sequences):
            color = self._config.sequence_colors[i % len(self._config.sequence_colors)]
            j = INIT_VALUE

            def set_parcel(row_subtrahend: int, segment: str):
                self[self._config.height - 1 - row_subtrahend][j + 1] = Cell(segment, fg=color, bg=self._config.background_color)

            # add '┼' at sequence beginning where sequences overlaps with y-axis
            set_parcel(row_index(sequence[0]), SEGMENTS[0])

            # asciiize sequence
            while j < len(sequence) - 2:
                j += 1

                y0 = row_index(sequence[j])
                y1 = row_index(sequence[j + 1])

                if y0 == y1:
                    set_parcel(y0, SEGMENTS[1])

                else:
                    if y0 > y1:
                        symbol_y0, symbol_y1 = SEGMENTS[4], SEGMENTS[2]
                    else:
                        symbol_y0, symbol_y1 = SEGMENTS[5], SEGMENTS[3]

                    set_parcel(y0, symbol_y0)
                    set_parcel(y1, symbol_y1)

                    # add vertical segment in case of consecutive sequence
                    # value steepness
                    for y in range(min(y0, y1) + 1, max(y0, y1)):
                        set_parcel(y, SEGMENTS[6])

    def serialized(self) -> str:
        return '\n'.join((''.join(row).rstrip() for row in self))

    def _add_x_axis(self):
        SEGMENTS = ('┬', '─')
        SEGMENT_REPLACEMENTS = {
            '┤': '┼',
            '─': '┬',
            '╰': '├',
            '╯': '┤'
        }

        for i, cell in enumerate(self[-1]):
            # add straight horizontal axis segment if parcel doesn't contain
            # a sequence segment, otherwise convert present sequence segment
            # to one comprising both the sequence and axis segment in color
            # of respective sequence

            is_data_point = self._is_data_point(i)
            if cell.is_empty:
                self[-1][i] = cell.replace_string(SEGMENTS[0] if is_data_point else SEGMENTS[1])
            elif is_data_point:
                self[-1][i] = cell.replace_string_if_applicable(SEGMENT_REPLACEMENTS)

    def _add_y_axis_with_tick_labels(self):
        """ Besets first parcel of each row with respective y-axis segment
            preceded by colored, adjusted tick value """

        DEFAULT_SEGMENT = '┤'
        SEGMENT_REPLACEMENTS = {
            '─': DEFAULT_SEGMENT,
            '|': '┼'
        }

        for i in range(len(self)):
            axis_cell = self[i][0]
            if axis_cell.is_empty:
                axis_cell = axis_cell.replace_string(DEFAULT_SEGMENT)
            else:
                axis_cell = axis_cell.replace_string_if_applicable(SEGMENT_REPLACEMENTS)

            tick_label_cell = Cell(self._params.y_axis_tick_labels[i].rjust(self._params.y_tick_columns), fg=self._config.label_color)
            self[i][0] = Cell(tick_label_cell + axis_cell, bg=self._config.tick_label_background_color)  # TODO

    def _is_data_point(self, point_index: int) -> bool:
        """ Returns:
                flag whether point corresponding to point_index is actual
                data point denoted in original sequences instead of interpolated
                one """

        return not point_index % (self._config.inter_points_margin + 1)

    def _indent_if_applicable(self):
        _n_terminal_columns = terminal_width()

        if self._config.horizontal_indentation:

            # raise if total width exceeding terminal columns
            if self._params.total_width > _n_terminal_columns:
                raise ValueError(f'Plot width = {self._params.total_width} > terminal width = {_n_terminal_columns}')

            for i in range(len(self)):
                self[i][0] = Cell(indented(self[i][0], columns=self._config.horizontal_indentation))

        elif self._config.center_horizontally:
            n_whitespaces = centering_indentation_len(self._params.total_width, reference_length=_n_terminal_columns)
            centering_margin = ' '.rjust(n_whitespaces)

            for row_index in range(len(self)):
                self[row_index].insert(0, Cell(centering_margin))

            self._params.columns_to_y_axis_ticks += n_whitespaces

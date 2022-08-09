import itertools as itt
import math
from typing import Iterator, List

from asciiplot._chart.grid import cell as _parcel
from asciiplot._chart.grid.cell import Cell
from asciiplot._coloring import colored
from asciiplot._config import Config
from asciiplot._utils import terminal_width
from asciiplot._utils.formatting import centering_indentation_len, indented
from asciiplot._utils.sequences import max_sequence_length
from asciiplot._utils.type_aliases import PlotSequences


class ChartGrid(List[List[Cell]]):
    class Params:
        def __init__(self,
                     y_min: int,
                     y_max: int,
                     width: int,
                     x_axis_description_len: int,
                     config: Config):
            self.y_min = y_min
            self.y_max = y_max

            self.width = width
            self.x_axis_description_len = x_axis_description_len

            self.y_value_range: float = abs(y_max - y_min)
            self.delta_row_index_per_y: float = max(1., config.height / self.y_value_range)
            self.y_axis_ticks: List[str] = list(self._y_axis_ticks(config.height, config.y_axis_tick_label_decimal_places))

            self.y_tick_columns: int = max(map(len, self.y_axis_ticks))
            self.columns_to_y_axis_ticks: int = self.y_tick_columns + config.horizontal_indentation

        @classmethod
        def extract(cls, sequences: PlotSequences, config: Config):
            values: List[float] = list(itt.chain.from_iterable(sequences))

            return cls(
                y_min=int(math.floor(min(values))),
                y_max=int(math.ceil(max(values))),
                width=max_sequence_length(sequences),
                x_axis_description_len=len(config.x_axis_description) if config.x_axis_description else 0,
                config=config
            )

        @property
        def total_width(self) -> int:
            return self.columns_to_y_axis_ticks + self.width + self.x_axis_description_len + 1

        def _y_axis_ticks(self, chart_height: int, decimal_places: int) -> Iterator[str]:
            delta_y_per_row = self.y_value_range / (chart_height - 1)
            for i in range(chart_height):
                label: float = self.y_max - i * delta_y_per_row

                # format label according to intended decimal places
                if decimal_places:
                    yield f'{round(label, decimal_places):.{decimal_places}f}'
                else:
                    yield str(int(label))

    def __init__(self, config: Config, sequences: PlotSequences):
        self._config = config
        self.params = self.Params.extract(sequences, config)

        super().__init__([[Cell() for _ in range(self.params.width)] for _ in range(self._config.height)])

        self._add_sequences(sequences)

        self._add_y_axis()
        self._add_x_axis()

        self._indent_if_applicable()

    def _add_sequences(self, sequences: PlotSequences):
        SEGMENTS = ['┼', '─', '╰', '╭', '╮', '╯', '│']
        INIT_VALUE = -1

        def _row_index(value: float) -> int:
            """ Scales sequence point clamped to desired extrema to
            corresponding point within chart value range """

            def clamp_to_row_index_bounds(row_index: int) -> int:
                return max(min(row_index, self._config.height - 1), 0)

            return clamp_to_row_index_bounds(row_index=int(round((value - self.params.y_min) * self.params.delta_row_index_per_y)))

        for i, sequence in enumerate(sequences):
            color = self._config.sequence_colors[i % len(self._config.sequence_colors)]
            j = INIT_VALUE

            def set_parcel(row_subtrahend: int, segment: str):
                self[self._config.height - 1 - row_subtrahend][j + 1] = Cell(segment, color)

            # add '┼' at sequence beginning where sequences overlaps with y-axis
            if math.isfinite(sequence[0]):
                set_parcel(_row_index(sequence[0]), SEGMENTS[0])

            # asciiize sequence
            while j < len(sequence) - 2:
                j += 1

                y0 = _row_index(sequence[j])
                y1 = _row_index(sequence[j + 1])

                if y0 == y1:
                    set_parcel(y0, SEGMENTS[1])

                else:
                    if y0 > y1:
                        symbol_y0, symbol_y1 = SEGMENTS[4], SEGMENTS[2]
                    else:
                        symbol_y0, symbol_y1 = SEGMENTS[5], SEGMENTS[3]

                    set_parcel(y0, symbol_y0)
                    set_parcel(y1, symbol_y1)

                    # add vertical segmentation in case of consecutive sequence
                    # value steepness
                    for y in range(min(y0, y1) + 1, max(y0, y1)):
                        set_parcel(y, SEGMENTS[6])

    def serialized(self) -> str:
        return '\n'.join((''.join(row).rstrip() for row in self))

    def _add_y_axis(self):
        """ Besets first parcel of each row with respective y-axis segment
            preceded by colored, adjusted tick value """

        SEGMENT_REPLACEMENTS = {
            '─': '┤',
            '|': '┼'
        }

        for i in range(len(self)):
            cell = self[i][0]
            if cell.is_empty:
                axis_segment = '┤'
            else:
                axis_segment = cell.replace_string(SEGMENT_REPLACEMENTS).string

            self[i][0] = Cell(f'{colored(self.params.y_axis_ticks[i].rjust(self.params.y_tick_columns), color=self._config.label_color)}{axis_segment}')

    def _add_x_axis(self):
        SEGMENTS = ('┼', '┤', '┬', '─')
        SEGMENT_REPLACEMENTS = {
            '┤': '┼',
            '─': '┬',
            '╰': '├',
            '╯': '┤'
        }

        def is_data_point(point_index: int) -> bool:
            """ Returns:
                    flag whether point corresponding to point_index is actual
                    data point denoted in original sequences instead of interpolated
                    one """

            return not point_index % (self._config.inter_points_margin + 1)

        last_row = self[-1]

        for i, cell in enumerate(last_row):
            # add straight horizontal axis segment if parcel doesn't contain
            # a sequence segment, otherwise convert present sequence segment
            # to one comprising both the sequence and axis segment in color
            # of respective sequence

            _is_data_point = is_data_point(i)
            if cell.is_empty:
                last_row[i] = Cell(SEGMENTS[2] if _is_data_point else SEGMENTS[3])
            elif _is_data_point:
                last_row[i] = cell.replace_string(SEGMENT_REPLACEMENTS)

    def _indent_if_applicable(self):
        _n_terminal_columns = terminal_width()

        if self._config.horizontal_indentation:

            # raise if total width exceeding terminal columns
            if self.params.total_width > _n_terminal_columns:
                raise ValueError(f'Plot width = {self.params.total_width} > terminal width = {_n_terminal_columns}')

            for i in range(len(self)):
                self[i][0] = Cell(indented(self[i][0], columns=self._config.horizontal_indentation))

        elif self._config.center_horizontally:
            n_whitespaces = centering_indentation_len(self.params.total_width, reference_length=_n_terminal_columns)
            centering_margin = ' '.rjust(n_whitespaces)

            for row_index in range(len(self)):
                self[row_index].insert(0, Cell(centering_margin))

            self.params.columns_to_y_axis_ticks += n_whitespaces

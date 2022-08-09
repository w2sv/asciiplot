from typing import Dict

from asciiplot._coloring import Color, colored


class Cell(str):
    def __new__(cls, segment=' ', color=Color.DEFAULT):
        return super().__new__(cls, colored(segment, color=color))

    def __init__(self, segment=' ', color=Color.DEFAULT):
        self.segment = segment
        self.color = color

    @property
    def is_empty(self) -> bool:
        return self.segment == ' '

    def replace_segment(self, segment_replacements: Dict[str, str]):
        r"""
        >>> SEGMENT_REPLACEMENTS = {'┤': '┼'}
        >>> Cell('┤').replace_segment(SEGMENT_REPLACEMENTS)
        '┼'
        >>> repr(Cell('┤', color=Color.RED).replace_segment(SEGMENT_REPLACEMENTS))
        "'\\x1b[38;5;1m┼\\x1b[0m'" """

        return self.__class__(segment_replacements.get(self.segment, self.segment), color=self.color)

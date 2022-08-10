from asciiplot._coloring import Color, ColoredString


_DEFAULT_CONTENT = ' '


class Cell(ColoredString):
    def __new__(cls, string=_DEFAULT_CONTENT, fg_color=Color.NONE, bg_color=Color.NONE):
        return super().__new__(cls, string, fg_color, bg_color)

    def __init__(self, string=_DEFAULT_CONTENT, fg_color=Color.NONE, bg_color=Color.NONE):
        super().__init__(string, fg_color, bg_color)

    @property
    def is_empty(self) -> bool:
        """
        >>> Cell().is_empty
        True """

        return self.string == _DEFAULT_CONTENT
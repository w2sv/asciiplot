from asciiplot._coloring import Color, ColoredString


_DEFAULT_CONTENT = ' '


class Cell(ColoredString):
    def __new__(cls, string=_DEFAULT_CONTENT, fg=Color.NONE, bg=Color.NONE):
        return super().__new__(cls, string, fg, bg)

    def __init__(self, string=_DEFAULT_CONTENT, fg=Color.NONE, bg=Color.NONE):
        super().__init__(string, fg, bg)

    @property
    def is_empty(self) -> bool:
        """
        >>> Cell().is_empty
        True """

        return self.string == _DEFAULT_CONTENT
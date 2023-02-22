from asciiplot._coloring import Color, ColoredString


_DEFAULT_CONTENT = ' '


class Cell(ColoredString):
    def __new__(cls, string=_DEFAULT_CONTENT, fg=Color.DEFAULT, bg=Color.DEFAULT):
        return super().__new__(cls, string, fg, bg)

    def __init__(self, string=_DEFAULT_CONTENT, fg=Color.DEFAULT, bg=Color.DEFAULT):
        super().__init__(string, fg, bg)

    @property
    def is_empty(self) -> bool:
        """
        >>> Cell().is_empty
        True
        >>> Cell("sdaf").is_empty
        False """

        return self.string == _DEFAULT_CONTENT
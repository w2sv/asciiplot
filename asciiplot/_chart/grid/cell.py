from asciiplot._coloring import Color, ColoredString


_DEFAULT_CONTENT = ' '


class Cell(ColoredString):
    def __new__(cls, content=_DEFAULT_CONTENT, color=Color.DEFAULT):
        return super().__new__(cls, content, color)

    def __init__(self, content=_DEFAULT_CONTENT, color=Color.DEFAULT):
        super().__init__(content, color)

    @property
    def is_empty(self) -> bool:
        """
        >>> Cell().is_empty
        True """

        return self.string == _DEFAULT_CONTENT

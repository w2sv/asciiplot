from asciiplot._coloring import ColoredString


DEFAULT_CONTENT = ' '


class Cell(ColoredString):
    @property
    def is_empty(self) -> bool:
        """
        >>> Cell().is_empty
        True """

        return self.string == DEFAULT_CONTENT

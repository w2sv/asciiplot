from typing import Dict, Tuple, Optional
import re

from asciiplot._coloring import RESET_COLOR_ANSI

DEFAULT = ' '


def segment_replaced(parcel: str, segment_replacements: Dict[str, str]) -> str:
    """ Returns:
            segment replaced parcel containing eventually present, original ansi color

        >>> SEGMENT_REPLACEMENTS = {'┤': '┼'}

        >>> segment_replaced('┤', SEGMENT_REPLACEMENTS)
        '┼'
        >>> print(segment_replaced(f'\x1b[36m┤\x1b[0m', SEGMENT_REPLACEMENTS))
        \x1b[36m┼\x1b[0m """

    color, element = contained_elements(parcel)
    new_element = segment_replacements.get(element, element)

    if color:
        return color + new_element + RESET_COLOR_ANSI
    return new_element


_ANSI_ESCAPE_PATTERN = re.compile(r'\x1b[^m]*m')


def contained_elements(parcel: str) -> Tuple[Optional[str], str]:
    """ Returns:
            Tuple[
                ansicolor if present else None,
                sequence segment
            ]

    >>> ansi_color, segment = contained_elements(parcel='\x1b[36m-\x1b[0m')
    >>> print(ansi_color)
    \x1b[36m
    >>> segment
    '-'

    >>> contained_elements(parcel='┤')
    (None, '┤') """

    ansi_sequences = re.findall(_ANSI_ESCAPE_PATTERN, parcel)
    if len(ansi_sequences):
        return ansi_sequences[0], parcel[len(ansi_sequences[0]):-len(RESET_COLOR_ANSI)]
    return None, parcel

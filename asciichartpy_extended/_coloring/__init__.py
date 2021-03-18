from asciichartpy_extended._coloring import colors


def _colored(string: str, color: str) -> str:
    return color + string + colors.RESET

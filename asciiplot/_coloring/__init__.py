from asciiplot._coloring import colors


def _colored(string: str, color: str) -> str:
    return color + string + colors.RESET

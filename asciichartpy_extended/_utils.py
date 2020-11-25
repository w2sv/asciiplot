from asciichartpy_extended import colors


def _colored(string: str, color: str) -> str:
    return color + string + colors.RESET

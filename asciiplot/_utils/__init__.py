import shutil

from .formatting import *


def terminal_columns() -> int:
    return shutil.get_terminal_size().columns

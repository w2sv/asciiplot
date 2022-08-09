import shutil


def terminal_width() -> int:
    return shutil.get_terminal_size().columns

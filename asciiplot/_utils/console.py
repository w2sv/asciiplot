import shutil


def console_width() -> int:
    return shutil.get_terminal_size().columns
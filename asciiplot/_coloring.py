import colored as _colored

import enum
from typing import Dict, Optional, Any


class Color(enum.Enum):
    DEFAULT = None
    BLACK = enum.auto()
    RED = enum.auto()
    GREEN = enum.auto()
    YELLOW = enum.auto()
    BLUE = enum.auto()
    MAGENTA = enum.auto()
    CYAN = enum.auto()
    LIGHT_GRAY = enum.auto()
    DARK_GRAY = enum.auto()
    LIGHT_RED = enum.auto()
    LIGHT_GREEN = enum.auto()
    LIGHT_YELLOW = enum.auto()
    LIGHT_BLUE = enum.auto()
    LIGHT_MAGENTA = enum.auto()
    LIGHT_CYAN = enum.auto()
    WHITE = enum.auto()
    GREY_0 = enum.auto()
    NAVY_BLUE = enum.auto()
    DARK_BLUE = enum.auto()
    BLUE_3A = enum.auto()
    BLUE_3B = enum.auto()
    BLUE_1 = enum.auto()
    DARK_GREEN = enum.auto()
    DEEP_SKY_BLUE_4A = enum.auto()
    DEEP_SKY_BLUE_4B = enum.auto()
    DEEP_SKY_BLUE_4C = enum.auto()
    DODGER_BLUE_3 = enum.auto()
    DODGER_BLUE_2 = enum.auto()
    GREEN_4 = enum.auto()
    SPRING_GREEN_4 = enum.auto()
    TURQUOISE_4 = enum.auto()
    DEEP_SKY_BLUE_3A = enum.auto()
    DEEP_SKY_BLUE_3B = enum.auto()
    DODGER_BLUE_1 = enum.auto()
    GREEN_3A = enum.auto()
    SPRING_GREEN_3A = enum.auto()
    DARK_CYAN = enum.auto()
    LIGHT_SEA_GREEN = enum.auto()
    DEEP_SKY_BLUE_2 = enum.auto()
    DEEP_SKY_BLUE_1 = enum.auto()
    GREEN_3B = enum.auto()
    SPRING_GREEN_3B = enum.auto()
    SPRING_GREEN_2A = enum.auto()
    CYAN_3 = enum.auto()
    DARK_TURQUOISE = enum.auto()
    TURQUOISE_2 = enum.auto()
    GREEN_1 = enum.auto()
    SPRING_GREEN_2B = enum.auto()
    SPRING_GREEN_1 = enum.auto()
    MEDIUM_SPRING_GREEN = enum.auto()
    CYAN_2 = enum.auto()
    CYAN_1 = enum.auto()
    DARK_RED_1 = enum.auto()
    DEEP_PINK_4A = enum.auto()
    PURPLE_4A = enum.auto()
    PURPLE_4B = enum.auto()
    PURPLE_3 = enum.auto()
    BLUE_VIOLET = enum.auto()
    ORANGE_4A = enum.auto()
    GREY_37 = enum.auto()
    MEDIUM_PURPLE_4 = enum.auto()
    SLATE_BLUE_3A = enum.auto()
    SLATE_BLUE_3B = enum.auto()
    ROYAL_BLUE_1 = enum.auto()
    CHARTREUSE_4 = enum.auto()
    DARK_SEA_GREEN_4A = enum.auto()
    PALE_TURQUOISE_4 = enum.auto()
    STEEL_BLUE = enum.auto()
    STEEL_BLUE_3 = enum.auto()
    CORNFLOWER_BLUE = enum.auto()
    CHARTREUSE_3A = enum.auto()
    DARK_SEA_GREEN_4B = enum.auto()
    CADET_BLUE_2 = enum.auto()
    CADET_BLUE_1 = enum.auto()
    SKY_BLUE_3 = enum.auto()
    STEEL_BLUE_1A = enum.auto()
    CHARTREUSE_3B = enum.auto()
    PALE_GREEN_3A = enum.auto()
    SEA_GREEN_3 = enum.auto()
    AQUAMARINE_3 = enum.auto()
    MEDIUM_TURQUOISE = enum.auto()
    STEEL_BLUE_1B = enum.auto()
    CHARTREUSE_2A = enum.auto()
    SEA_GREEN_2 = enum.auto()
    SEA_GREEN_1A = enum.auto()
    SEA_GREEN_1B = enum.auto()
    AQUAMARINE_1A = enum.auto()
    DARK_SLATE_GRAY_2 = enum.auto()
    DARK_RED_2 = enum.auto()
    DEEP_PINK_4B = enum.auto()
    DARK_MAGENTA_1 = enum.auto()
    DARK_MAGENTA_2 = enum.auto()
    DARK_VIOLET_1A = enum.auto()
    PURPLE_1A = enum.auto()
    ORANGE_4B = enum.auto()
    LIGHT_PINK_4 = enum.auto()
    PLUM_4 = enum.auto()
    MEDIUM_PURPLE_3A = enum.auto()
    MEDIUM_PURPLE_3B = enum.auto()
    SLATE_BLUE_1 = enum.auto()
    YELLOW_4A = enum.auto()
    WHEAT_4 = enum.auto()
    GREY_53 = enum.auto()
    LIGHT_SLATE_GREY = enum.auto()
    MEDIUM_PURPLE = enum.auto()
    LIGHT_SLATE_BLUE = enum.auto()
    YELLOW_4B = enum.auto()
    DARK_OLIVE_GREEN_3A = enum.auto()
    DARK_GREEN_SEA = enum.auto()
    LIGHT_SKY_BLUE_3A = enum.auto()
    LIGHT_SKY_BLUE_3B = enum.auto()
    SKY_BLUE_2 = enum.auto()
    CHARTREUSE_2B = enum.auto()
    DARK_OLIVE_GREEN_3B = enum.auto()
    PALE_GREEN_3B = enum.auto()
    DARK_SEA_GREEN_3A = enum.auto()
    DARK_SLATE_GRAY_3 = enum.auto()
    SKY_BLUE_1 = enum.auto()
    CHARTREUSE_1 = enum.auto()
    LIGHT_GREEN_2 = enum.auto()
    LIGHT_GREEN_3 = enum.auto()
    PALE_GREEN_1A = enum.auto()
    AQUAMARINE_1B = enum.auto()
    DARK_SLATE_GRAY_1 = enum.auto()
    RED_3A = enum.auto()
    DEEP_PINK_4C = enum.auto()
    MEDIUM_VIOLET_RED = enum.auto()
    MAGENTA_3A = enum.auto()
    DARK_VIOLET_1B = enum.auto()
    PURPLE_1B = enum.auto()
    DARK_ORANGE_3A = enum.auto()
    INDIAN_RED_1A = enum.auto()
    HOT_PINK_3A = enum.auto()
    MEDIUM_ORCHID_3 = enum.auto()
    MEDIUM_ORCHID = enum.auto()
    MEDIUM_PURPLE_2A = enum.auto()
    DARK_GOLDENROD = enum.auto()
    LIGHT_SALMON_3A = enum.auto()
    ROSY_BROWN = enum.auto()
    GREY_63 = enum.auto()
    MEDIUM_PURPLE_2B = enum.auto()
    MEDIUM_PURPLE_1 = enum.auto()
    GOLD_3A = enum.auto()
    DARK_KHAKI = enum.auto()
    NAVAJO_WHITE_3 = enum.auto()
    GREY_69 = enum.auto()
    LIGHT_STEEL_BLUE_3 = enum.auto()
    LIGHT_STEEL_BLUE = enum.auto()
    YELLOW_3A = enum.auto()
    DARK_OLIVE_GREEN_3 = enum.auto()
    DARK_SEA_GREEN_3B = enum.auto()
    DARK_SEA_GREEN_2 = enum.auto()
    LIGHT_CYAN_3 = enum.auto()
    LIGHT_SKY_BLUE_1 = enum.auto()
    GREEN_YELLOW = enum.auto()
    DARK_OLIVE_GREEN_2 = enum.auto()
    PALE_GREEN_1B = enum.auto()
    DARK_SEA_GREEN_5B = enum.auto()
    DARK_SEA_GREEN_5A = enum.auto()
    PALE_TURQUOISE_1 = enum.auto()
    RED_3B = enum.auto()
    DEEP_PINK_3A = enum.auto()
    DEEP_PINK_3B = enum.auto()
    MAGENTA_3B = enum.auto()
    MAGENTA_3C = enum.auto()
    MAGENTA_2A = enum.auto()
    DARK_ORANGE_3B = enum.auto()
    INDIAN_RED_1B = enum.auto()
    HOT_PINK_3B = enum.auto()
    HOT_PINK_2 = enum.auto()
    ORCHID = enum.auto()
    MEDIUM_ORCHID_1A = enum.auto()
    ORANGE_3 = enum.auto()
    LIGHT_SALMON_3B = enum.auto()
    LIGHT_PINK_3 = enum.auto()
    PINK_3 = enum.auto()
    PLUM_3 = enum.auto()
    VIOLET = enum.auto()
    GOLD_3B = enum.auto()
    LIGHT_GOLDENROD_3 = enum.auto()
    TAN = enum.auto()
    MISTY_ROSE_3 = enum.auto()
    THISTLE_3 = enum.auto()
    PLUM_2 = enum.auto()
    YELLOW_3B = enum.auto()
    KHAKI_3 = enum.auto()
    LIGHT_GOLDENROD_2A = enum.auto()
    LIGHT_YELLOW_3 = enum.auto()
    GREY_84 = enum.auto()
    LIGHT_STEEL_BLUE_1 = enum.auto()
    YELLOW_2 = enum.auto()
    DARK_OLIVE_GREEN_1A = enum.auto()
    DARK_OLIVE_GREEN_1B = enum.auto()
    DARK_SEA_GREEN_1 = enum.auto()
    HONEYDEW_2 = enum.auto()
    LIGHT_CYAN_1 = enum.auto()
    RED_1 = enum.auto()
    DEEP_PINK_2 = enum.auto()
    DEEP_PINK_1A = enum.auto()
    DEEP_PINK_1B = enum.auto()
    MAGENTA_2B = enum.auto()
    MAGENTA_1 = enum.auto()
    ORANGE_RED_1 = enum.auto()
    INDIAN_RED_1C = enum.auto()
    INDIAN_RED_1D = enum.auto()
    HOT_PINK_1A = enum.auto()
    HOT_PINK_1B = enum.auto()
    MEDIUM_ORCHID_1B = enum.auto()
    DARK_ORANGE = enum.auto()
    SALMON_1 = enum.auto()
    LIGHT_CORAL = enum.auto()
    PALE_VIOLET_RED_1 = enum.auto()
    ORCHID_2 = enum.auto()
    ORCHID_1 = enum.auto()
    ORANGE_1 = enum.auto()
    SANDY_BROWN = enum.auto()
    LIGHT_SALMON_1 = enum.auto()
    LIGHT_PINK_1 = enum.auto()
    PINK_1 = enum.auto()
    PLUM_1 = enum.auto()
    GOLD_1 = enum.auto()
    LIGHT_GOLDENROD_2B = enum.auto()
    LIGHT_GOLDENROD_2C = enum.auto()
    NAVAJO_WHITE_1 = enum.auto()
    MISTY_ROSE1 = enum.auto()
    THISTLE_1 = enum.auto()
    YELLOW_1 = enum.auto()
    LIGHT_GOLDENROD_1 = enum.auto()
    KHAKI_1 = enum.auto()
    WHEAT_1 = enum.auto()
    CORNSILK_1 = enum.auto()
    GREY_100 = enum.auto()
    GREY_3 = enum.auto()
    GREY_7 = enum.auto()
    GREY_11 = enum.auto()
    GREY_15 = enum.auto()
    GREY_19 = enum.auto()
    GREY_23 = enum.auto()
    GREY_27 = enum.auto()
    GREY_30 = enum.auto()
    GREY_35 = enum.auto()
    GREY_39 = enum.auto()
    GREY_42 = enum.auto()
    GREY_46 = enum.auto()
    GREY_50 = enum.auto()
    GREY_54 = enum.auto()
    GREY_58 = enum.auto()
    GREY_62 = enum.auto()
    GREY_66 = enum.auto()
    GREY_70 = enum.auto()
    GREY_74 = enum.auto()
    GREY_78 = enum.auto()
    GREY_82 = enum.auto()
    GREY_85 = enum.auto()
    GREY_89 = enum.auto()
    GREY_93 = enum.auto()

    @property
    def value(self) -> str:
        return self.name.lower()

    @property
    def fg_code(self) -> str:
        return _colored.fg(self.value) if self is not Color.DEFAULT else ''

    @property
    def bg_code(self) -> str:
        return _colored.bg(self.value) if self is not Color.DEFAULT else ''


def colored(obj: Any, fg=Color.DEFAULT, bg=Color.DEFAULT) -> str:
    r"""
    >>> repr(colored(69))
    "'69'"
    >>> repr(colored('yessir', fg=Color.BLACK))
    "'\\x1b[38;5;0myessir\\x1b[0m'"
    >>> repr(colored('wasssup', fg=Color.GREY_93))
    "'\\x1b[38;5;255mwasssup\\x1b[0m'" """

    trailing_token = _colored.style.RESET if fg is not Color.DEFAULT or bg is not Color.DEFAULT else ''
    return f'{fg.fg_code}{bg.bg_code}{obj}{trailing_token}'


class ColoredString:
    @classmethod
    def make_if_string_present(cls, string: Optional[str], fg=Color.DEFAULT, bg=Color.DEFAULT) -> Optional['ColoredString']:
        if string is None:
            return None
        return cls(string, fg, bg)

    def __init__(self, string: str, fg=Color.DEFAULT, bg=Color.DEFAULT):
        r"""
        >>> ColoredString('yauoi')
        'yauoi'
        >>> ColoredString('yauoi', fg=Color.TAN, bg=Color.AQUAMARINE_3)
        '\x1b[38;5;180m\x1b[48;5;79myauoi\x1b[0m' """

        self.string = string
        self.fg = fg
        self.bg = bg

    @property
    def displayed_length(self) -> int:
        """
        >>> ColoredString('uiuiui', Color.DARK_CYAN).displayed_length
        6 """

        return len(self.string)

    def replace_string(self, replacement: str) -> 'ColoredString':
        r"""
        >>> ColoredString('a').replace_string('b')
        'b' """

        self.string = replacement
        return self

    def replace_string_if_applicable(self, replacements: Dict[str, str]) -> 'ColoredString':
        r"""
        >>> s = ColoredString('┤').replace_string_if_applicable({'┤': '┼'})
        >>> repr(s)
        "'┼'"
        >>> repr(ColoredString('┤', fg=Color.RED).replace_string_if_applicable({'┤': '┼'}))
        "'\\x1b[38;5;1m┼\\x1b[0m'" """

        self.string = replacements.get(self.string, self.string)
        return self

    def set_foreground(self, string: str, fg: Color) -> 'ColoredString':
        self.string = string
        self.fg = fg
        return self

    def __str__(self):
        return colored(self.string, self.fg, self.bg)

    def __repr__(self):
        return repr(str(self))

    def __len__(self):
        return len(str(self))

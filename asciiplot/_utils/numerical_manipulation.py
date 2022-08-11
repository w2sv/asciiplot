from typing import TypeVar


_T = TypeVar('_T', bound=float)


def clamp_value(value: _T, lower_bound: _T, upper_bound: _T) -> _T:
    return max(min(value, upper_bound), lower_bound)
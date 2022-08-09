from typing import List, Optional, Sequence, Union

from typing_extensions import Protocol, TypeAlias


class Serializable(Protocol):
    def __str__(self) -> str:
        ...


PlotSequence: TypeAlias = List[float]
PlotSequences: TypeAlias = Sequence[PlotSequence]

TickValue: TypeAlias = Union[str, float]
TickValues: TypeAlias = Sequence[Optional[TickValue]]
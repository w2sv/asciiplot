from typing import Iterable, List, Optional, Sequence, Union

from typing_extensions import Literal, Protocol, TypeAlias


class Serializable(Protocol):
    def __str__(self) -> str:
        ...


PlotSequence: TypeAlias = List[float]
PlotSequences: TypeAlias = Sequence[PlotSequence]

TickLabelValue: TypeAlias = Union[str, float]
TickLabelValues: TypeAlias = Iterable[Optional[TickLabelValue]]
AutoLiteral: TypeAlias = Literal['auto']
TickLabelInput: TypeAlias = Union[AutoLiteral, TickLabelValues, None]
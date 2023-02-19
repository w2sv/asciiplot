from typing_extensions import Literal, TypeAlias

from typing import Iterable, List, Optional, Sequence, Union

PlotSequence: TypeAlias = List[float]
PlotSequences: TypeAlias = Sequence[PlotSequence]

TickLabelValue: TypeAlias = Union[str, float]
TickLabelValues: TypeAlias = Iterable[Optional[TickLabelValue]]
AutoLiteral: TypeAlias = Literal['auto']
TickLabelInput: TypeAlias = Union[AutoLiteral, TickLabelValues, None]
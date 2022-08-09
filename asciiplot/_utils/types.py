from typing_extensions import Protocol


class Serializable(Protocol):
    def __str__(self) -> str:
        ...
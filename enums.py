from enum import StrEnum, auto


class BookStatus(StrEnum):
    AVAILABLE = auto()
    RESERVED = auto()
    LOANED = auto()
    LOST = auto()

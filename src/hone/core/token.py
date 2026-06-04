from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class TokenType(Enum):
    INTEGER = auto()
    PLUS = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None

    def __repr__(self) -> str:
        if self.value is None:
            return f"Token({self.type.name})"
        return f"Token({self.type.name}, {self.value})"

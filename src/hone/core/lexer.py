from typing import Iterable

from .token import Token, TokenType


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None

    def advance(self) -> None:
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self) -> None:
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self) -> str:
        digits = []
        while self.current_char is not None and self.current_char.isdigit():
            digits.append(self.current_char)
            self.advance()
        if not digits:
            raise LexerError("Expected digit")
        return "".join(digits)

    def tokens(self) -> Iterable[Token]:
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                yield Token(TokenType.INTEGER, self.integer())
                continue

            if self.current_char == "+":
                yield Token(TokenType.PLUS, self.current_char)
                self.advance()
                continue

            raise LexerError(f"Unexpected character: {self.current_char!r}")

        yield Token(TokenType.EOF)

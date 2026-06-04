from .ast import BinaryOp, Number
from .lexer import Lexer, LexerError
from .token import TokenType


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, text: str) -> None:
        self.lexer = Lexer(text)
        self.tokens = self.lexer.tokens()
        self.current_token = next(self.tokens)

    def eat(self, token_type: TokenType) -> None:
        if self.current_token.type == token_type:
            self.current_token = next(self.tokens)
            return
        raise ParserError(
            f"Expected token {token_type.name}, got {self.current_token.type.name}"
        )

    def factor(self):
        if self.current_token.type == TokenType.INTEGER:
            value = int(self.current_token.value)
            self.eat(TokenType.INTEGER)
            return Number(value)
        raise ParserError(
            f"Expected integer, got {self.current_token.type.name}"
        )

    def parse(self):
        node = self.factor()

        while self.current_token.type == TokenType.PLUS:
            op = self.current_token
            self.eat(TokenType.PLUS)
            node = BinaryOp(left=node, op=op, right=self.factor())

        if self.current_token.type != TokenType.EOF:
            raise ParserError("Unexpected tokens after expression")

        return node

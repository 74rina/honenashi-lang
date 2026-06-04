from dataclasses import dataclass


class ASTNode:
    pass


@dataclass
class Number(ASTNode):
    value: int


@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    op: object
    right: ASTNode

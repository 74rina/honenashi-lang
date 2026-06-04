from .ast import BinaryOp, Number
from .token import TokenType


class InterpreterError(Exception):
    pass


class Interpreter:
    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        visitor = getattr(self, method_name, None)
        if visitor is None:
            raise InterpreterError(f"No visit_{node.__class__.__name__} method")
        return visitor(node)

    def visit_Number(self, node: Number) -> int:
        return node.value

    def visit_BinaryOp(self, node: BinaryOp) -> int:
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op.type == TokenType.PLUS:
            return left + right
        raise InterpreterError(f"Unsupported operator: {node.op.type}")

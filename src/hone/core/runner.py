from .interpreter import Interpreter
from .parser import Parser


def run_source(source: str) -> int:
    parser = Parser(source)
    tree = parser.parse()
    interpreter = Interpreter()
    return interpreter.visit(tree)

"""hone command entry points."""

from .run import main as run_main
from .repl import main as repl_main

__all__ = ["run_main", "repl_main"]

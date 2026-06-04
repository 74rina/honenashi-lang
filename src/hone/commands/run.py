from pathlib import Path

from ..core.runner import run_source


def main(args) -> int:
    source_path = Path(args.path)
    source = source_path.read_text()
    result = run_source(source)
    print(result)
    return 0

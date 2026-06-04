from ..core.runner import run_source


WELCOME = "hone REPL (addition only). Type 'exit' or Ctrl+C to quit."


def main() -> int:
    print(WELCOME)
    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue
        if line.lower() in {"exit", "quit"}:
            break

        try:
            result = run_source(line)
            print(result)
        except Exception as exc:
            print(f"Error: {exc}")

    return 0

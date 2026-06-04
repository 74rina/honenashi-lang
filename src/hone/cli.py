import argparse
import sys

from hone.commands.run import main as run_main
from hone.commands.repl import main as repl_main


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="hone", description="Minimal hone language CLI")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run a hone source file")
    run_parser.add_argument("path", help="Path to .hone source file")

    subparsers.add_parser("repl", help="Start the hone REPL")

    args = parser.parse_args(argv or sys.argv[1:])
    if args.command == "run":
        return run_main(args)
    if args.command == "repl":
        return repl_main()

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

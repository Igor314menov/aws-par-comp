import argparse

DEFAULT_FROM = 1
DEFAULT_TO = 10


def doSmth(from_: int, to: int):
    print(f"From: {from_}")
    print(f"To: {to}")
    pass

def main():
    cli_parser = argparse.ArgumentParser(description="Run prediction backend for custom Python models")
    cli_parser.add_argument("--from_", metavar="FROM", nargs='?', type=int, default=DEFAULT_FROM,
                            help=f"From, defaults to {DEFAULT_FROM}")
    cli_parser.add_argument("--to", metavar="TO", nargs='?', type=int, default=DEFAULT_TO,
                            help=f"To, defaults to {DEFAULT_TO}")
    args = cli_parser.parse_args()

    doSmth(args.from_, args.to)    


if __name__ == "__main__":
    main()


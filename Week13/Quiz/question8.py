import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--items",
    nargs='+',        # + : for  one or more / * : for zero or more
    help="List of items"
)

args = parser.parse_args()

print(args.items)

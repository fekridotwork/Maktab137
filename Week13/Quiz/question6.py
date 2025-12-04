import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="User's name")
args = parser.parse_args()

print(args.name)

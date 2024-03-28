import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument(
    "-x",
    "--independent_variable",
    dest="x",
    type=int,
    required=True,
    help="Column index of the independent variable",
)
parser.add_argument(
    "-y",
    "--dependent_variable",
    dest="y",
    type=int,
    required=True,
    help="Column index of the dependent variable",
)
args = parser.parse_args()

fn: str = args.filename
x: int = args.x
y: int = args.y
print(f"fn = {fn}, x={x}, y={y}")

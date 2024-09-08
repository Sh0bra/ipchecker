import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("-l", "--long", action="store_true")
args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory does not exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)

def build_output(entry, long=False):

    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
import argparse
from pathlib import Path

""" class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
    Create a new ArgumentParser object. All parameters should be passed as keyword arguments. Each parameter has its own more detailed description below, but in short they are:
        prog - The name of the program (default: os.path.basename(sys.argv[0]))
        usage - The string describing the program usage (default: generated from arguments added to parser)
        description - Text to display before the argument help (by default, no text)
        epilog - Text to display after the argument help (by default, no text)
        parents - A list of ArgumentParser objects whose arguments should also be included
        formatter_class - A class for customizing the help output
        prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
        fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)
        argument_default - The global default value for arguments (default: None)
        conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
        add_help - Add a -h/--help option to the parser (default: True)
        allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
        exit_on_error - Determines whether or not ArgumentParser exits with error info when an error occurs. (default: True)
 """

parser = argparse.ArgumentParser()

""" 
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
    Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:
        name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
        action - The basic type of action to be taken when this argument is encountered at the command line.
        nargs - The number of command-line arguments that should be consumed.
        const - A constant value required by some action and nargs selections.
        default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.
        type - The type to which the command-line argument should be converted.
        choices - A sequence of the allowable values for the argument.
        required - Whether or not the command-line option may be omitted (optionals only).
        help - A brief description of what the argument does.
        metavar - A name for the argument in usage messages.
        dest - The name of the attribute to be added to the object returned by parse_args().
 """


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
# python 3
# tensorflow flags, cflags behavior

import argparse

"""
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
action - The basic type of action to be taken when this argument is encountered at the command line.
nargs - The number of command-line arguments that should be consumed.
const - A constant value required by some action and nargs selections.
default - The value produced if the argument is absent from the command line.
type - The type to which the command-line argument should be converted.
choices - A container of the allowable values for the argument.
required - Whether or not the command-line option may be omitted (optionals only).
help - A brief description of what the argument does.
metavar - A name for the argument in usage messages.
dest - The name of the attribute to be added to the object returned by parse_args().
"""

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
parser.add_argument("--oo", help="just a help")
parser.add_argument("-q", "--qqqqq", type=int, default=11, help="just a help")
parser.add_argument("-w", "--haha", dest="uu", type=bool, default=True, help="just a help")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

# problem !!!
# -h will generat weird uppercase name if not set action !!! don't care.

args = parser.parse_args()

# cannot use short name !!
print(args.qqqqq)
print(args.uu)

# python 3
# tensorflow flags, cflags behavior

# multiple modules !!! different from TF flags!!
# use TF.flags or stackoverflow method!!
#http://stackoverflow.com/questions/15494574/using-pythons-argparse-in-multiple-scripts-backed-by-multiple-custom-modules

# check out tensorflow/tensorflow/python/platform/flags.py, it runs parse_args() when tf.app.run()
# an extra module is needed, in which the global parser is defined and argparse is imported.
# it is combersome to construct global parser, stick with TF.flags if possible.

import argparse
import logging
import arg1
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
parser.add_argument("-a", "--aa", type=str, default='haha', help="just a help")

parser.add_argument("-w",
                    "--haha",
                    dest="uu",
                    type=bool,
                    default=True,
                    help="just a help")

PARSER = argparse.ArgumentParser(description='collect web page html data.')

PARSER.add_argument("--data_dir", type=str,
                    default="data/",
                    help="path of data directory.")
# CAT_FETCH is subset of CATEGORIES, only fetch those cats
PARSER.add_argument("--cat_fetch", type=str,
                    default="Business,Society,Science,Recreation,Shopping,Games",
                    # default="Arts,Business,Computers,Health",
                    help="cats to be print, no space, empty to fetch all")

# problem !!!
# -h will generat weird uppercase name if not set action !!! don't care.

# first parse
parser.set_defaults(aa="111")
args = parser.parse_args()
print("\n\nall arguments args:")
for arg in vars(args):
    logging.info("{:12}{}".format(arg, getattr(args, arg)))
# modify and check parsed arguments
if args.uu:
    logging.info("\nchange args.uu")
    args.uu = False
    print("uu:", args.uu)
parser.add_argument("-v",
                    "--verbose",
                    help="increase output verbosity",
                    action="store_true")
# second parse
args = parser.parse_args()


def set_logging(stream=False, fileh=False, filename="example.log"):
    """set basic logging configurations (root logger).
    args:
        stream (bool): whether print log to console.
        fileh (bool): whether write log to file.
        filename (str): the path of log file.
    return:
        configued root logger.
    """
    handlers = []
    level = logging.DEBUG
    log_format = '%(asctime)s: %(message)s'

    if stream:
        handlers.append(logging.StreamHandler())
    if fileh:
        handlers.append(logging.FileHandler(filename))
    logging.basicConfig(format=log_format, handlers=handlers, level=level)
    return logging.getLogger()

# cannot use short name !!
set_logging(stream=True)
print(args.qqqqq)
print(args.uu)
print("\n\nall arguments args:")
for arg in vars(args):
    logging.info("{:12}{}".format(arg, getattr(args, arg)))
print("\n\nall arguments arg1:")
for arg in vars(arg1.args):
    logging.info("{:12}{}".format(arg, getattr(arg1.args, arg)))

import argparse
import logging

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-testttt",
                    "--lalalllal",
                    help="increase output verbosity",
                    action="store_true")

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
print("\ntest all arguments:")
for arg in vars(args):
    logging.info("{:12}{}".format(arg, getattr(args, arg)))

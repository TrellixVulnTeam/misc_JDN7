"""
credit: Yuhui Lin
This is a python utility module usually for my machine learning project.
Support both python 2.6+ and 3.3+.
function:
    - time
    - logging
    - argparse across module
problems:
    - set_defaults override, add_argument no sense, check before override??
    - create newline logger
    http://stackoverflow.com/questions/20111758/how-to-insert-newline-in-python-logging
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import time
import argparse
# import types
# import os

CUR_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")


class MyLogger(object):
    def newline(self, how_many_lines=1):
        """swith handler to blank line hander.
        any better way to re-arrange this function???
        """
        if '__logger' not in self.__dict__:
            raise RuntimeError(
                'please run logger.set_logger() before start logging.')
        logger = self.__dict__['__logger']

        if hasattr(self, 'fh'):
            # Switch handler, output a blank line
            logger.removeHandler(self.fh)
            logger.addHandler(self.fh_blank)
        if hasattr(self, 'sh'):
            # Switch handler, output a blank line
            logger.removeHandler(self.sh)
            logger.addHandler(self.sh_blank)
        if hasattr(self, 'fh') or hasattr(self, 'sh'):
            for i in range(how_many_lines):
                logger.info('')

        # Switch back
        if hasattr(self, 'fh'):
            logger.removeHandler(self.fh_blank)
            logger.addHandler(self.fh)
        if hasattr(self, 'sh'):
            logger.removeHandler(self.sh_blank)
            logger.addHandler(self.sh)

    def set_logger(self,
                   name=None,
                   stream=False,
                   fileh=False,
                   filename='log.txt',
                   level=logging.DEBUG,
                   propagate=False):
        # create logger with hierachical name, a.b.c
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = propagate
        # create formatter and add it to the handlers
        # formatter = logging.Formatter(
        #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')

        # create file handler which logs even debug messages
        if fileh:
            fh = logging.FileHandler(filename)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            logger.fh = fh
            logger.addHandler(fh)

            # Create a "blank line" handler
            fh_blank = logging.FileHandler(filename)
            fh_blank.setLevel(level)
            fh_blank.setFormatter(logging.Formatter(fmt=''))
            logger.fh_blank = fh_blank

        # create console handler with a higher log level
        if stream:
            sh = logging.StreamHandler()
            sh.setLevel(level)
            sh.setFormatter(formatter)
            logger.sh = sh
            logger.addHandler(sh)

            # Create a "blank line" handler
            sh_blank = logging.StreamHandler()
            sh_blank.setLevel(level)
            sh_blank.setFormatter(logging.Formatter(fmt=''))
            logger.sh_blank = sh_blank

        self.__dict__['__logger'] = logger

    def __getattr__(self, name):
        """parse attibutes to logger."""
        if '__logger' not in self.__dict__:
            raise RuntimeError(
                'please run logger.set_logger() before start logging.')
        logger = self.__dict__['__logger']
        return getattr(logger, name)

# usage:
# from utiles import logger
# logger.set_logger()
# logger.newline(2)
logger = MyLogger()

# # old logging:
# # logging
# # usage:
# #   from util import logger
# #   util.set_logging()
# #   logger.info("test-{}".format(1))
# # also used by following functions
# # logger = logging
# # if name is None, return the root logger -- logging
# LOGGER_NAME=None
# logger = logging.getLogger(name=LOGGER_NAME)


# def set_logging(level=logging.INFO,
#                 stream=False,
#                 fileh=False,
#                 filename="log.txt"):
#     """set basic logging configurations (root logger).
#     args:
#         stream (bool): whether print log to console.
#         fileh (bool): whether write log to file.
#         filename (str): the path of log file.
#     return:
#         configued root logger.
#     samples:
#         set_logging(stream=True)
#         logging.debug('This message should appear on the console')
#         logging.info('So should this')
#         logging.warning('And this, too')
#     """
#     handlers = []
#     level = level
#     log_format = '%(asctime)s: %(message)s'
#
#     if stream:
#         handlers.append(logging.StreamHandler())
#     if fileh:
#         handlers.append(logging.FileHandler(filename))
#     logging.basicConfig(format=log_format, handlers=handlers, level=level)
#     return logging.getLogger()
#
#
# def log_newline(self, how_many_lines=1):
#     """swith handler to blank line hander.
#     any better way to re-arrange this function???
#     """
#     if hasattr(self, 'fh'):
#         # Switch handler, output a blank line
#         self.removeHandler(self.fh)
#         self.addHandler(self.fh_blank)
#     if hasattr(self, 'sh'):
#         # Switch handler, output a blank line
#         self.removeHandler(self.sh)
#         self.addHandler(self.sh_blank)
#     if hasattr(self, 'fh') or hasattr(self, 'sh'):
#         for i in range(how_many_lines):
#             self.info('')
#
#     # Switch back
#     if hasattr(self, 'fh'):
#         self.removeHandler(self.fh_blank)
#         self.addHandler(self.fh)
#     if hasattr(self, 'sh'):
#         self.removeHandler(self.sh_blank)
#         self.addHandler(self.sh)
#
#
# def set_logger(name=LOGGER_NAME,
#                stream=False,
#                fileh=False,
#                filename='log.txt',
#                level=logging.DEBUG,
#                propagate=False):
#     # create logger with hierachical name, a.b.c
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.propagate = propagate
#     # create formatter and add it to the handlers
#     # formatter = logging.Formatter(
#     #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     formatter = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')
#
#     # create file handler which logs even debug messages
#     if fileh:
#         fh = logging.FileHandler(filename)
#         fh.setLevel(level)
#         fh.setFormatter(formatter)
#         logger.fh = fh
#         logger.addHandler(fh)
#
#         # Create a "blank line" handler
#         fh_blank = logging.FileHandler(filename)
#         fh_blank.setLevel(level)
#         fh_blank.setFormatter(logging.Formatter(fmt=''))
#         logger.fh_blank = fh_blank
#
#     # create console handler with a higher log level
#     if stream:
#         sh = logging.StreamHandler()
#         sh.setLevel(level)
#         sh.setFormatter(formatter)
#         logger.sh = sh
#         logger.addHandler(sh)
#
#         # Create a "blank line" handler
#         sh_blank = logging.StreamHandler()
#         sh_blank.setLevel(level)
#         sh_blank.setFormatter(logging.Formatter(fmt=''))
#         logger.sh_blank = sh_blank
#
#     # add a method to logger object
#     logger.newline = types.MethodType(log_newline, logger)
#     return logger
#

class _FlagValues(object):
    """FLAG class from tensorflow/python/platform/flags.py.
    two options to design FLAGS:
        1. tensorflow style
            FLAGS.parse_arg, check and modify FLAGS, FLAGS.print()
        2. parse each arg when adding it, using the same parser
            cannot work! each parse refresh all FLAGS
        3. use parser.set_defaults() best!
            override default_value anywhere I like
            problem: add_argument default not make sense !
            ?????????????????
    """

    def __init__(self):
        """Global container and accessor for flags and their values."""
        self.__dict__['__flags'] = {}
        self.__dict__['__parsed'] = False

    def _parse_flags(self):
        # result, unparsed = _global_parser.parse_known_args()
        result = _global_parser.parse_args()
        for flag_name, val in vars(result).items():
            self.__dict__['__flags'][flag_name] = val
        self.__dict__['__parsed'] = True
        # return unparsed

    def __getattr__(self, name):
        """Retrieves the 'value' attribute of the flag --name."""
        if not self.__dict__['__parsed']:
            # self._parse_flags()
            raise ValueError("FLAGS haven't been parsed!")
        if name not in self.__dict__['__flags']:
            raise AttributeError(name)
        return self.__dict__['__flags'][name]

    def __setattr__(self, name, value):
        """Sets the 'value' attribute of the flag --name."""
        if not self.__dict__['__parsed']:
            # self._parse_flags()
            raise ValueError("FLAGS haven't been parsed!")
        self.__dict__['__flags'][name] = value

    def get(self, key):
        """get the value of key.
        if not parsed yet, only parse the flags that have been read.
        """
        if self.__dict__['__parsed']:
            return self.__dict__['__flags'][key]
        else:
            result, unparsed = _global_parser.parse_known_args()
            return result.__dict__[key]

    def overwrite_defaults(self, **kwargs):
        """
        set default value for flags.
        careful:
            parser-level defaults always override argument-level defaults.
        """
        _global_parser.set_defaults(**kwargs)

    def overwrite_none(self, **kwargs):
        """
        set default value for flags.
        different to overwrite_defaults():
            overwrite the flag only if the flag exists and value is None;
            otherwise, do nothing.
        """
        d = self.__dict__.get('__overwrite_none', {})
        d.update(kwargs)
        self.__dict__['__overwrite_none'] = d

    def add(self, *args, **kwargs):
        _global_parser.add_argument(*args, **kwargs)

    def log_flags(self, logger=logger):
        logger.newline()
        logger.info("*******ALL FLAGS*******")
        for attr, value in sorted(self.__dict__['__flags'].items()):
            logger.info("{} = {}".format(attr, value))
        logger.newline()

    def parse_and_log(self, logger=logger):
        """parse arguments.
        print all arguments.
        """
        FLAGS._parse_flags()
        # overwrite some None flags
        for key, value in self.__dict__.get('__overwrite_none', {}).items():
            if key in self.__dict__['__flags']:
                if self.__dict__['__flags'][key] is None:
                    self.__dict__['__flags'][key] = value
            else:
                logger.newline()
                logger.warn(
                    "cannot overwrite flag {}. It does not exist.".format(key))
        # log all valid flags
        FLAGS.log_flags(logger)

# parse command line arguments
# usage:
# type: str, int, float, bool
#   FLAGS = utils.FLAGS
# FLAGS.add_arg("--dd", type=str,
#               default="",
#               help="")
# FLAGS.parse_and_print()
_global_parser = argparse.ArgumentParser()
FLAGS = _FlagValues()
# arg = _global_parser

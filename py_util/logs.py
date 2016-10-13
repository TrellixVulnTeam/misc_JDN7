import logging
import time
import os
import types

CUR_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")

log_dir = "logs"
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, CUR_TIME + ".log")

# please check if log_dir exists before call this function !!!


def set_logging(level=logging.INFO,
                stream=False,
                fileh=False,
                filename="log.txt"):
    """set basic logging configurations (root logger).
    args:
        stream (bool): whether print log to console.
        fileh (bool): whether write log to file.
        filename (str): the path of log file.
    return:
        configued root logger.
    """
    handlers = []
    level = level
    log_format = '%(asctime)s: %(message)s'

    if stream:
        handlers.append(logging.StreamHandler())
    if fileh:
        handlers.append(logging.FileHandler(filename))
    logging.basicConfig(format=log_format, handlers=handlers, level=level)
    return logging.getLogger()


def set_logger(name, stream=False, fileh=False, filename="example.log"):
    """set costumized logging configurations.
    args:
        stream (bool): whether print log to console.
        fileh (bool): whether write log to file.
        filename (str): the path of log file.
    return:
        configued logger.
    """
    # create logger with 'spam_application'
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create file handler which logs even debug messages
    if fileh:
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # create console handler with a higher log level
    if stream:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

def log_newline(self, how_many_lines=1):
    """swith handler to blank line hander.
    any better way to re-arrange this function???
    """
    if hasattr(self, 'fh'):
        # Switch handler, output a blank line
        self.removeHandler(self.fh)
        self.addHandler(self.fh_blank)
    if hasattr(self, 'sh'):
        # Switch handler, output a blank line
        self.removeHandler(self.sh)
        self.addHandler(self.sh_blank)
    if hasattr(self, 'fh') or hasattr(self, 'sh'):
        for i in range(how_many_lines):
            self.info('')

    # Switch back
    if hasattr(self, 'fh'):
        self.removeHandler(self.fh_blank)
        self.addHandler(self.fh)
    if hasattr(self, 'sh'):
        self.removeHandler(self.sh_blank)
        self.addHandler(self.sh)

def create_logger(name=None, stream=False, fileh=False,
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
    formatter = logging.Formatter(
        '%(asctime)s: %(message)s')

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

    # add a method to logger object
    logger.newline = types.MethodType(log_newline, logger)
    return logger

set_logging(stream=True)
l = set_logging(level=20, stream=True)
l.debug('This message should appear on the console')

set_logging(stream=True)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

logger = set_logger("log_test", stream=True)
logger.info("hahahah")


logger = create_logger(name="test1", stream=True)
logger.info('Start reading database')
logger.newline(1)
logger.info('Updating records ...')
logger.newline(2)
logger.info('Finish updating records')

import logging
import time
import os

CUR_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")

log_dir = "logs"
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, CUR_TIME + ".log")

# please check if log_dir exists before call this function !!!

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
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


# set_logging(stream=True)
l = set_logging(stream=True)
l.debug('This message should appear on the console')
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

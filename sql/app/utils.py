import logging
import sys


def get_logger(module_name):
    """Returns logger."""
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt="%(asctime)s %(filename)s:%(lineno)s %(funcName)s %(levelname)s : %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",

    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
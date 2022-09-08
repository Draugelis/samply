import logging


def setup_logger(name):
    logging_format = '%(asctime)s - [%(levelname)s]- %(funcName)s:%(lineno)d -- %(message)s'  # noqa: E501
    formatter = logging.Formatter(logging_format)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    return logger

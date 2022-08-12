import logging

def setup_logger(name):
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d -- [%(levelname)s] %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    return logger
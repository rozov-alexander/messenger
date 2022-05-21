import logging
import sys
import log.server_log_config
import log.client_log_config
import datetime


def log(func):
    def wrapper(*args, **kwargs):
        logger_name = 'server_log' if 'server.py' in sys.argv[0] else 'client_log'
        logger = logging.getLogger(logger_name)

        res = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} была вызвана из {func.__module__}' 
                    f'с аргументами {args} {kwargs} в {datetime.datetime.now()}')
        return res
    return wrapper

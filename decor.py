import logging
import sys
import log.server_log_config
import log.client_log_config
import datetime
import traceback


def log(func):
    def wrapper(*args, **kwargs):
        logger_name = 'server_log' if 'server.py' in sys.argv[0] else 'client_log'
        logger = logging.getLogger(logger_name)

        res = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} была вызвана в модуле {func.__module__}' 
                    f'с аргументами {args} {kwargs} в {datetime.datetime.now()}'
                    f'из функции {traceback.format_stack()[0].strip().split()[-1]}.')
        return res
    return wrapper

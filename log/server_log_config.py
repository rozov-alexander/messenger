import logging
import logging.handlers
import sys
import os
sys.path.append('../')


log = logging.getLogger('server_log')
# Определяем формат сообщений
format = logging.Formatter('%(asctime)s %(levelname)-8s %(module)-6s %(message)s')

# Создаём обработчик, который выводит сообщения в файл
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')
file_hand = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
# Установка уровня сообщений
file_hand.setLevel(logging.DEBUG)
# Подключаем форматирование сообщений
file_hand.setFormatter(format)

log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Передать сообщение обработчику
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическое общение')


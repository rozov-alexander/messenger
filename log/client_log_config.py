import logging 
import sys
import os
sys.path.append('../')


log = logging.getLogger('client_log')
# Определяем формат сообщений
format = logging.Formatter('%(asctime)s %(levelname)-8s %(module)-6s %(message)s')

# Создаём обработчик, который выводит сообщения в файл
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')
file_hand = logging.FileHandler(PATH, encoding='utf-8')
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


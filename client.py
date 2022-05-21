from socket import socket, AF_INET, SOCK_STREAM
from common.constants import *
from common.utils import get_message, send_message
import time
import argparse
import json
import logging
import log.client_log_config
from decor import log


client_logging = logging.getLogger('client_log')


@log
def create_presence(account_name='Guest'):
    """Создание сообщения о присутствии"""
    presence_message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    client_logging.debug(f'Сообщение {PRESENCE} сформировано для пользователя {account_name}')
    return presence_message


@log
def answer_from_server(message):
    """Функция проверяет ответ от сервера. 
    Выдаёт 200, если ответ корректен или 400 при ошибке"""
    client_logging.debug(f'Сообщение от сервера {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


@log
def main():
        
    parser = argparse.ArgumentParser(description="Client script")

    parser.add_argument("-a", dest="ip", default='127.0.0.1')
    parser.add_argument("-p", dest="PORT", default=7777, type=int)
    args = parser.parse_args()

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((args.ip, args.PORT))
    client_logging.info(f'Клиент запущен с параметрами: адрес сервера - {args.ip}, порт - {args.PORT}')
    message_to_server = create_presence()
    send_message(client_socket, message_to_server)

    try:
        answer = answer_from_server(get_message(client_socket))
        client_logging.info(f'Принят ответ от сервера: {answer}')
        print(answer)
    except (ValueError, json.JSONDecodeError):
        client_logging.error('Не удалось декодировать сообщение сервера.')

    client_socket.close()


if __name__ == '__main__':
    main()

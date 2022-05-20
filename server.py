from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from common.constants import *
from common.utils import get_message, send_message
import argparse
import json
import log.server_log_config
import logging
import log.server_log_config


server_logger = logging.getLogger('server_log')


def message_to_client(message):
    """ Функция формирует ответ клиенту в виде JSON"""
    server_logger.debug(f'Сообщение клиенту: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():

    parser = argparse.ArgumentParser(description="Server script")

    parser.add_argument('-a', dest="ip", default='127.0.0.1')
    parser.add_argument("-p", dest="PORT", default=7777, type=int)
    args = parser.parse_args()

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((args.ip, args.PORT))
    server_socket.listen(MAX_CONNECTIONS)


    while True:
        client, client_address = server_socket.accept()
        server_logger.info(f'Установлено соединение с {client_address}')
        try:
            message_from_client = get_message(client)
            server_logger.debug(f'Получено сообщение {message_from_client}')
            print(message_from_client)
            response = message_to_client(message_from_client)
            server_logger.debug(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            print(response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            server_logger.error('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

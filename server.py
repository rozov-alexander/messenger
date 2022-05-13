from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from common.constants import *
from common.utils import get_message, send_message
import argparse
import json


def message_to_client(message):
    """ Функция формирует ответ клиенту в виде JSON"""
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
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = message_to_client(message_from_client)
            send_message(client, response)
            print(response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

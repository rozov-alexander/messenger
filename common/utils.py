from common.constants import *
import json
from decor import log


@log
def get_message(client):
    """
    Утилита приёма и декодирования сообщения.
    Принимает байты, выдаёт словарь, если принято что-то
    другое возвращает ValueError (ошибку значения)
    """

    encoded_response = client.recv(MAX_MESSAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError


@log
def send_message(client, message):
    """
    Утилита кодирования и отправки сообщения:
    принимает для отправки словарь, получает из него строку,
    далее превращает строку в байты и отправляет.
    """
    if not isinstance(message, dict):
        raise TypeError
    print(message)
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    client.send(encoded_message)

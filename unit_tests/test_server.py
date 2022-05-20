import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from server import message_to_client
from common.constants import *
import time


class TestServer(unittest.TestCase):
    """Тестирование функции из модуля server.py"""
  
    def test_correct(self):
        message = {ACTION: PRESENCE, TIME: 9999, USER: {ACCOUNT_NAME: 'Guest'}
        }
        self.assertEqual(message_to_client(message), {'response': 200})
    

    def test_no_user(self):
        # не указан Пользователь
        message = {ACTION: PRESENCE, TIME: 9999}
        self.assertEqual(message_to_client(message), {'response': 400, 'error': 'Bad Request'})
    def test_not_correct_user(self):
        # не указан Пользователь
        message = {ACTION: PRESENCE, TIME: 9999, USER: {ACCOUNT_NAME: 'Admin'}
        }
        self.assertEqual(message_to_client(message), {'response': 400, 'error': 'Bad Request'})
    

    def test_no_time(self):
        # не указано время
        message = {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}
        }
        self.assertEqual(message_to_client(message), {'response': 400, 'error': 'Bad Request'})
    
    
    def test_no_action(self):
        # не указано действие
        message = {TIME: 9999, USER: {ACCOUNT_NAME: 'Guest'}
        }
        self.assertEqual(message_to_client(message), {'response': 400, 'error': 'Bad Request'})



import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence, answer_from_server
from common.constants import *
import time


class TestClient(unittest.TestCase):
    """Тестирование функций из модуля client.py"""
    
    def test_create_presence(self):

        test_presence = create_presence()
        test_presence['time'] = 9999
        self.assertEqual(test_presence, {ACTION: PRESENCE, TIME: 9999, USER: {ACCOUNT_NAME: 'Guest'}})
    

    def test_response_200(self):
        message = {'response': 200}
        self.assertEqual(answer_from_server(message), '200 : OK')

    def test_response_400(self):
        message = {'response': 400, 'error': 'Bad Request'}
        self.assertEqual(answer_from_server(message), '400 : Bad Request')

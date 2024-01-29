import unittest
from flask import url_for
import sys
sys.path.append('../../')  # Añadir el directorio raíz del proyecto al sys.path
from src import server  # Importar el módulo server desde el directorio src

# Flask server class instance
app = server.app

class TestServerRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)

    def test_bookList_route(self):
        response = self.app.get('/bookList')
        self.assertEqual(response.status_code, 200)

    def test_bookInfo_route(self):
        response = self.app.get('/bookInfo')
        self.assertEqual(response.status_code, 200)


'''
class TestSocketIOEvents(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.socket_client = app.test_client()

    def test_check_status_socketio_event(self):
        with app.test_request_context():
            self.socket_client.emit('check_status_request')
            received = self.socket_client.get_received()
            self.assertTrue(any(data['name'] == 'check_status_response' for data in received))

    def test_bookList_socketio_event(self):
        with app.test_request_context():
            self.socket_client.emit('bookList_request', {'typeValue': 'fiction', 'limitValue': 10})
            received = self.socket_client.get_received()
            self.assertTrue(any(data['name'] == 'bookList_response' for data in received))

    def test_bookInfo_socketio_event(self):
        with app.test_request_context():
            self.socket_client.emit('bookInfo_request', {'bookId': 1})
            received = self.socket_client.get_received()
            self.assertTrue(any(data['name'] == 'bookInfo_response' for data in received))
'''

if __name__ == '__main__':
    unittest.main()

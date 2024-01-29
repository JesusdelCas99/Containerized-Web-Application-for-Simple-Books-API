import unittest
from flask import url_for
import sys

# Ensure that the root directory of the project is included in the Python path
sys.path.append('./')

# Import the Flask application
from src import server

# Rename Flask server instance as 'app'
app = server.app

class TestServerRoutes(unittest.TestCase):
    """
    Test case class for testing the routes of the Flask server.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        Sets the Flask application to testing mode and creates a test client for making requests.
        """
        app.testing = True
        self.app = app.test_client()

    def test_index_route(self):
        """
        Test case to check the response of the '/' route.
        Verifies that accessing the '/' route returns a status code of 200 (OK).
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_route(self):
        """
        Test case to check the response of the '/status' route.
        Verifies that accessing the '/status' route returns a status code of 200 (OK).
        """
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)

    def test_bookList_route(self):
        """
        Test case to check the response of the '/bookList' route.
        Verifies that accessing the '/bookList' route returns a status code of 200 (OK).
        """
        response = self.app.get('/bookList')
        self.assertEqual(response.status_code, 200)

    def test_bookInfo_route(self):
        """
        Test case to check the response of the '/bookInfo' route.
        Verifies that accessing the '/bookInfo' route returns a status code of 200 (OK).
        """
        response = self.app.get('/bookInfo')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


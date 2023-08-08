"""
Test script for google auth.
version 1.0
Author - WaleedAhmed05
"""
import unittest
from unittest.mock import patch
import app

class TestAuthRoutes(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    @patch('controllers.auth.AuthController.google_login')
    def test_google_login(self, mock_google_login):
        # Mock the AuthController.google_login() method to avoid external redirects
        mock_google_login.return_value = "Fake Google login page"
        response = self.app.get('/auth/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

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

    @patch('controllers.auth.AuthController.google_login_callback')
    def test_google_login_callback(self, mock_google_login_callback):
        # Mock the AuthController.google_login_callback() method
        # to avoid any external dependencies during testing
        mock_google_login_callback.return_value = "Google login callback response"
        response = self.app.get('/auth/login/callback')
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        # Simulate a request to the user route
        response = self.app.get('/auth/user')
        self.assertEqual(response.status_code, 401)  # Assumption: Unauthorized access should return 401

if __name__ == '__main__':
    unittest.main()

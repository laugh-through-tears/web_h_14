import unittest
from unittest.mock import patch
from api.auth import verify_password, get_password_hash, create_access_token, create_refresh_token, get_email_form_refresh_token, get_current_user

class AuthTestCase(unittest.TestCase):
    @patch('api.auth.verify_password')
    def test_verify_password(self, mock_verify_password):
        """
        Test case for verifying password.
        """
        mock_verify_password.return_value = True
        self.assertTrue(verify_password('plain_password', 'hashed_password'))

    @patch('api.auth.get_password_hash')
    def test_get_password_hash(self, mock_get_password_hash):
        """
        Test case for getting password hash.
        """
        mock_get_password_hash.return_value = 'hashed_password'
        self.assertEqual(get_password_hash('plain_password'), 'hashed_password')

    @patch('api.auth.create_access_token')
    def test_create_access_token(self, mock_create_access_token):
        """
        Test case for creating access token.
        """
        mock_create_access_token.return_value = 'access_token'
        self.assertEqual(create_access_token({'sub': 'test'}), 'access_token')

    @patch('api.auth.create_refresh_token')
    def test_create_refresh_token(self, mock_create_refresh_token):
        """
        Test case for creating refresh token.
        """
        mock_create_refresh_token.return_value = 'refresh_token'
        self.assertEqual(create_refresh_token({'sub': 'test'}), 'refresh_token')

    @patch('api.auth.get_email_form_refresh_token')
    def test_get_email_form_refresh_token(self, mock_get_email_form_refresh_token):
        """
        Test case for getting email from refresh token.
        """
        mock_get_email_form_refresh_token.return_value = 'test@example.com'
        self.assertEqual(get_email_form_refresh_token('token'), 'test@example.com')

    @patch('api.auth.get_current_user')
    def test_get_current_user(self, mock_get_current_user):
        """
        Test case for getting current user.
        """
        mock_get_current_user.return_value = {'email': 'test@example.com'}
        self.assertEqual(get_current_user('db', 'token'), {'email': 'test@example.com'})

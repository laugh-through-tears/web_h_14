import unittest
from api import api, db
from api.models import User

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        api.config['TESTING'] = True
        api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = api.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_registration(self):
        # Test registration endpoint
        response = self.app.post('/register', json={'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in response.json)
        self.assertTrue('refresh_token' in response.json)

    def test_login(self):
        # Test login endpoint
        User.create(username='testuser', password='password')
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in response.json)
        self.assertTrue('refresh_token' in response.json)

    def test_protected_route(self):
        # Test protected route
        User.create(username='testuser', password='password')
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'password'})
        access_token = response.json['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.app.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Protected Route')

if __name__ == '__main__':
    unittest.main()

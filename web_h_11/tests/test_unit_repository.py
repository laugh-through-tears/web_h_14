import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from src.repository import create_contact, get_contact, update_contact, delete_contact

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock(Session)

    def test_create_contact(self):
        contact_data = {"name": "John", "email": "john@example.com"}
        created_contact = create_contact(self.db, contact_data)
        self.assertIsNotNone(created_contact)

    def test_get_contact(self):
        contact_id = 1
        contact = get_contact(self.db, contact_id)
        self.assertIsNone(contact)

    def test_update_contact(self):
        contact_id = 1
        updated_data = {"name": "Updated Name"}
        updated_contact = update_contact(self.db, contact_id, updated_data)
        self.assertIsNone(updated_contact)

    def test_delete_contact(self):
        contact_id = 1
        deleted_contact = delete_contact(self.db, contact_id)
        self.assertIsNone(deleted_contact)

if __name__ == '__main__':
    unittest.main()

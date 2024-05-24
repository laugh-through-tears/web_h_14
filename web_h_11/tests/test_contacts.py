import unittest
from fastapi.testclient import TestClient
from api.main import app
from api.database import get_db, Base
from api import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.config import settings

SQLALCHEMY_DATABASE_URL = settings.TEST_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

class TestContacts(unittest.TestCase):
    def setUp(self):
        self.db = TestingSessionLocal()

    def tearDown(self):
        self.db.close()

    def test_create_contact(self):
        response = client.post("/contacts/", json={"first_name": "John", "last_name": "Doe", "email": "johndoe@example.com", "phone_number": "1234567890", "birth_date": "1990-01-01T00:00:00", "additional_info": "Friend"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_read_contacts(self):
        response = client.get("/contacts/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_contact(self):
        response = client.put("/contacts/1", json={"first_name": "Jane", "last_name": "Doe", "email": "janedoe@example.com", "phone_number": "0987654321", "birth_date": "1991-01-01T00:00:00", "additional_info": "Colleague"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Jane")

    def test_delete_contact(self):
        response = client.delete("/contacts/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

if __name__ == "__main__":
    unittest.main()

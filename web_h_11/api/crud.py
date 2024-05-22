from sqlalchemy.orm import Session
from api.schemas import ContactCreate
from api.schemas import Contact
from api.models import Contact
from api import models
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
from typing import List, Optional
from pydantic import BaseModel

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    birthday: datetime

app = FastAPI()

contacts_db = [
    Contact(id=1, first_name="John", last_name="Doe", email="john@example.com", birthday=datetime(1990, 5, 15)),
    Contact(id=2, first_name="Jane", last_name="Doe", email="jane@example.com", birthday=datetime(1985, 8, 20))
]

async def search_contacts(query: str):
    results = []
    for contact in contacts_db:
        if query.lower() in contact.first_name.lower() or \
           query.lower() in contact.last_name.lower() or \
           query.lower() in contact.email.lower():
            results.append(contact)
    return results

@app.get("/contacts/birthdays/")
async def get_birthdays_within_range():
    today = datetime.now()
    next_week = today + timedelta(days=7)
    birthdays_within_range = []
    for contact in contacts_db:
        if today <= contact.birthday <= next_week:
            birthdays_within_range.append(contact)
    return birthdays_within_range

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, contact_data: ContactCreate):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    for key, value in contact_data.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db.query(Contact).filter(Contact.id == contact_id).delete()
    db.commit()

def search_contacts(db: Session, query: str):
    return db.query(models.Contact).filter(
        (models.Contact.name.ilike(f"%{query}%")) |
        (models.Contact.surname.ilike(f"%{query}%")) |
        (models.Contact.email.ilike(f"%{query}%"))
    ).all()

def get_birthdays_within_range(db: Session, start_date: datetime, end_date: datetime):

    return db.query(models.Contact).filter(
        (models.Contact.birth_date >= start_date) &
        (models.Contact.birth_date <= end_date)
    ).all()



from sqlalchemy.orm import Session
from api.models import Contact

def get_contacts(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of contacts from the database.
    """
    return db.query(Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: Contact):
    """
    Create a new contact in the database.
    """
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_contact(db: Session, contact_id: int):
    """
    Retrieve a single contact by ID from the database.
    """
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, updated_contact: Contact):
    """
    Update an existing contact in the database.
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = updated_contact.name
        contact.email = updated_contact.email
        contact.phone = updated_contact.phone
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    """
    Delete a contact from the database.
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

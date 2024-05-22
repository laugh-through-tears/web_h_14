from sqlalchemy.orm import Session
from api.models import Contact

async def create_contact(db: Session, contact: Contact):
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

async def update_contact(db: Session, contact_id: int, updated_contact: Contact):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for attr, value in updated_contact.dict().items():
            setattr(contact, attr, value)
        db.commit()
        db.refresh(contact)
    return contact

async def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return contact

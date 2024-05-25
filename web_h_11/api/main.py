from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models, database, users, contacts


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Hello World"}

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    """
    Endpoint to retrieve a list of users.
    """
    users = users.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/")
def create_user(user: User, db: Session = Depends(database.get_db)):
    """
    Endpoint to create a new user.
    """
    return users.create_user(db=db, user=user)

@app.get("/contacts/")
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    """
    Endpoint to retrieve a list of contacts.
    """
    contacts = contacts.get_contacts(db, skip=skip, limit=limit)
    return contacts

@app.post("/contacts/")
def create_contact(contact: Contact, db: Session = Depends(database.get_db)):
    """
    Endpoint to create a new contact.
    """
    return contacts.create_contact(db=db, contact=contact)


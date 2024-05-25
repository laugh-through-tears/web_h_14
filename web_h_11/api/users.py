from sqlalchemy.orm import Session
from api.models import User

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of users from the database.
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: User):
    """
    Create a new user in the database.
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    """
    Retrieve a single user by ID from the database.
    """
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, updated_user: User):
    """
    Update an existing user in the database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = updated_user.email
        user.hashed_password = updated_user.hashed_password
        user.is_active = updated_user.is_active
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    """
    Delete a user from the database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

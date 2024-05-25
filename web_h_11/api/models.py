from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class User(Base):
    """
    User model class.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Integer, default=1)
    avatar_url = Column(String, nullable=True)

    contacts = relationship("Contact", back_populates="owner")

class Contact(Base):
    """
    Contact model class.
    """
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone_number = Column(String, index=True)
    birth_date = Column(DateTime, index=True)
    additional_info = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="contacts")


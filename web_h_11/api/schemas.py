from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: int
    avatar_url: Optional[str] = None

    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: datetime
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

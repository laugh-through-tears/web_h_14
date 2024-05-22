from pydantic import BaseModel
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_info: str = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    name: str

    class Config:
        from_attributes = True

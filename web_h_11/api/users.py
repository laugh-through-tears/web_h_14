from libgravatar import Gravatar
from sqlalchemy.orm import Session

from api.schemas import ContactBase



async def get_user_by_email(email: str, db: Session) -> ContactBase:
    return db.query(ContactBase).filter(ContactBase.email == email).first()


async def create_user(body: ContactBase, db: Session) -> ContactBase:
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = ContactBase(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: ContactBase, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()



from sqlalchemy.orm import Session

# from database import models
from database.schemas import UserCreate
from database.models import User
from services.security import crypt_context


def get_user():
    pass


def create_user(db: Session, user: UserCreate):
    hash_password = crypt_context.hash(user.password)

    user.update_password(hash_password)

    db_user = User(**user.to_dict())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

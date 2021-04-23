from fastapi import Depends

from sqlalchemy.orm import Session

# from database import models
from database.schemas import UserCreate
from database.models import User
from services.security import crypt_context
from database.database import engine, SessionLocal
from database.models import Base


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=username).first()
    verify_password = crypt_context.verify(password, user.password)

    if not user.is_active:
        return 'user inactive'

    if not verify_password:
        return 'bad pwd'

    return user


def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hash_password = crypt_context.hash(user.password)

    user.update_password(hash_password)

    db_user = User(**user.to_dict())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

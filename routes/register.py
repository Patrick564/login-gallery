from fastapi import APIRouter, Depends
# from fastapi.utils import Optional

from sqlalchemy.orm import Session

from database.crud_user import create_user
from database.database import SessionLocal, engine
from services.form_schemas import UserData
from database.models import Base
from database.schemas import UserCreate, User


Base.metadata.create_all(bind=engine)


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('', response_model=User)
def register(db: Session = Depends(get_db), form_data: UserCreate = Depends(UserData)):  # noqa
    user = create_user(db, form_data)

    return user

from fastapi import APIRouter, Depends
# from fastapi.utils import Optional

from database.schemas import UserCreate, User
from services.form_schemas import UserData
from services.security import crypt_context


router = APIRouter()


def create_user(username: str, password: str, active: bool = True):
    hash_password = crypt_context.hash(password)
    user = UserCreate(username=username, password=hash_password, active=active)

    return user


@router.post('', response_model=User)
async def register(form_data: UserCreate = Depends(UserData)):
    user = create_user(form_data.username, form_data.password)

    return user

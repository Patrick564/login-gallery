from fastapi import APIRouter, Form, Depends
from fastapi.utils import Optional

from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel


SECRET_KEY = 'e578571cd4d985f058a8a2063f4f4494ec60bb9221a5d02433f8c3048c7ab348'
ALGORITHM = jwt.ALGORITHMS.HS512
ACCESS_TOKEN_EXPIRE_MINUTES = 15


router = APIRouter()

crypt_context = CryptContext(
    schemes=['bcrypt'],
    bcrypt__rounds=13,
    deprecated='auto'
)


class UserData:
    def __init__(
        self,
        username: str = Form(...),
        email: Optional[str] = Form(None),
        password: str = Form(...),
        active: Optional[bool] = Form(None),
    ):
        self.username = username
        self.email = email
        self.password = password
        self.active = active


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    password: str
    active: Optional[bool] = True

    class Config:
        orm_mode = True


def create_user(username: str, password: str, active: bool = True):
    hash_password = crypt_context.hash(password)
    user = UserCreate(username=username, password=hash_password, active=active)

    return user


@router.post('', response_model=User)
async def register(form_data: UserCreate = Depends(UserData)):
    user = create_user(form_data.username, form_data.password)

    return user

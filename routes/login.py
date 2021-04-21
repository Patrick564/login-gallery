from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
# from pydantic import BaseModel

from datetime import datetime, timedelta
# from typing import Optional


SECRET_KEY = 'cbc27988afc2b6d3f8dca078e0fb491fba8f9668abcc62e303957b7c9734439b'
ALGORITHM = 'HS512'
ACCESS_TOKEN_EXPIRE_MINUTES = 15


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # noqa
        "disabled": False,
    }
}


def get_token(username: str, active: bool):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    payload = {
        'sub': username,
        'active': active,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(minutes=15)
    }

    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise credentials_exception

    return token


def get_user(username: str, password: str):
    return {
        'username': username,
        'active': True
    }


@router.post('')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username, form_data.password)
    access_token = get_token(**user)

    return {
        'access_token': access_token,
        'token_type': 'Bearer'
    }

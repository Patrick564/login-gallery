from os import getenv
from dotenv import load_dotenv

from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from datetime import datetime, timedelta
from pytz import timezone

load_dotenv('.env/.env')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')


def create_jwt_token(username: str, email: str, is_active: bool):
    tz = timezone(getenv('LOCAL_TIME_ZONE'))
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    payload = {
        'sub': username,
        'email': email,
        'is_active': is_active,
        'iat': datetime.now(tz=tz),
        'exp': datetime.now(tz=tz) + timedelta(minutes=30)  # noqa
    }

    try:
        jwt_token = jwt.encode(payload, getenv('SECRET_KEY'), algorithm=getenv('ALGORITHM'))  # noqa
    except JWTError:
        raise credentials_exception

    return jwt_token


def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    decoded_payload = jwt.decode(token, getenv('SECRET_KEY'), algorithms=getenv('ALGORITHM'))  # noqa

    return decoded_payload

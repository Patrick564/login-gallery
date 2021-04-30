from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from datetime import datetime, timedelta
from pytz import timezone


SECRET_KEY = 'cbc27988afc2b6d3f8dca078e0fb491fba8f9668abcc62e303957b7c9734439b'
ALGORITHM = 'HS512'
ACCESS_TOKEN_EXPIRE = 30
LOCAL_TIME_ZONE = 'America/Lima'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')


def create_jwt_token(username: str, email: str, is_active: bool):
    tz = timezone(LOCAL_TIME_ZONE)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    payload = {
        'sub': username,
        'email': email,
        'is_active': is_active,
        'iat': datetime.now(tz=tz),
        'exp': datetime.now(tz=tz) + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    }

    try:
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise credentials_exception

    return jwt_token


def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    a = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    print(a)

    return a

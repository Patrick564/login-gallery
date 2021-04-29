from fastapi import status, HTTPException

from jose import jwt, JWTError

from datetime import datetime, timedelta


SECRET_KEY = 'cbc27988afc2b6d3f8dca078e0fb491fba8f9668abcc62e303957b7c9734439b'
ALGORITHM = 'HS512'
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_jwt_token(username: str, email: str, is_active: bool):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    payload = {
        'sub': username,
        'email': email,
        'is_active': is_active,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    try:
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise credentials_exception

    return jwt_token

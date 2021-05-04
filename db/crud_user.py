from fastapi import HTTPException, status

from sqlalchemy.sql import text

from db.models import users
from db.schemas import UserCreate
from db.settings import database
from services.security import crypt_context


async def get_user(username: str, password: str):
    where_clause = text(f'username=\'{username}\'')
    query = users.select(whereclause=where_clause)

    user_query = await database.fetch_one(query)
    user = dict(user_query)

    verify_password = crypt_context.verify(password, user['password'])

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    if not user['is_active']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User is not active',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    if not verify_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {
        'username': user['username'],
        'email': user['email'],
        'is_active': user['is_active']
    }


async def create_user(user: UserCreate):
    hash_password = crypt_context.hash(user.password)

    user.update_password(hash_password)

    query = users.insert().values(**user.to_dict())
    response = await database.execute(query)

    if not response:
        return {
            'error': response,
            'successfull': False
        }

    return {
        'id': response,
        'username': user.username,
        'successfull': True
    }

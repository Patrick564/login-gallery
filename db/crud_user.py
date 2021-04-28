from sqlalchemy.sql import text

from services.security import crypt_context

from db.models import users
from db.schemas import UserCreate
from db.settings import database


async def get_user(username: str, password: str):
    where_clause = text(f'username=\'{username}\'')
    query = users.select(whereclause=where_clause)

    user_query = await database.fetch_one(query)
    user = dict(user_query)

    verify_password = crypt_context.verify(password, user['password'])

    if not user['is_active']:
        return 'user inactive'

    if not verify_password:
        return 'bad pwd'

    return user


async def create_user(user: UserCreate):
    # hash_password = crypt_context.hash(user.password)

    # user.update_password(hash_password)

    # db_user = User(**user.to_dict())

    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)

    # return db_user
    pass

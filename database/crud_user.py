from database.schemas import UserCreate
# from services.security import crypt_context

from database.models import users
from database.database import database


async def get_user(username: str, password: str):
    # user = db.query(User).filter_by(username=username).first()
    # verify_password = crypt_context.verify(password, user.password)

    # if not user.is_active:
    #     return 'user inactive'

    # if not verify_password:
    #     return 'bad pwd'

    print(username, password)

    q = users.select()

    return await database.fetch_all(q)


async def create_user(user: UserCreate):
    # hash_password = crypt_context.hash(user.password)

    # user.update_password(hash_password)

    # db_user = User(**user.to_dict())

    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)

    # return db_user
    pass

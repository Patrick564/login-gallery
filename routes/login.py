from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext

from db.crud_user import get_user
# from db.settings import database


SECRET_KEY = 'cbc27988afc2b6d3f8dca078e0fb491fba8f9668abcc62e303957b7c9734439b'
ALGORITHM = 'HS512'
ACCESS_TOKEN_EXPIRE_MINUTES = 15

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(form_data.username, form_data.password)
    # access_token = get_token(**user)

    return user
    # return {
    #     'access_token': user,
    #     'token_type': 'Bearer'
    # }


# def get_token(username: str, active: bool):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED
#     )
#     payload = {
#         'sub': username,
#         'active': active,
#         'iat': datetime.now(),
#         'exp': datetime.now() + timedelta(minutes=15)
#     }

#     try:
#         token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     except JWTError:
#         raise credentials_exception

#     return token

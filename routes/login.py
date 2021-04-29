from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext

from db.crud_user import get_user

from services.jwt import create_jwt_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(form_data.username, form_data.password)
    access_token = create_jwt_token(**user)

    return {
        'access_token': access_token,
        'token_type': 'Bearer'
    }

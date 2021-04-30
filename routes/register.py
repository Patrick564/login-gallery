from fastapi import APIRouter, Depends

from services.form_schemas import UserData

from db.crud_user import create_user
from db.schemas import UserCreate


router = APIRouter()


@router.post('')
async def register(form_data: UserCreate = Depends(UserData)):
    user = await create_user(form_data)

    return user

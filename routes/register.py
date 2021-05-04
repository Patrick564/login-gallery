from fastapi import APIRouter, Depends

from db.crud_user import create_user
from db.schemas import UserCreate
from schema.user_schema import UserData

router = APIRouter()


@router.post('')
async def register(form_data: UserCreate = Depends(UserData)):
    response = await create_user(form_data)

    return response

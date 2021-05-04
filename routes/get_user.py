from fastapi import APIRouter, Depends

from db.schemas import User
from services.jwt import verify_jwt_token


router = APIRouter()


@router.get('')
async def get_user(current_user: User = Depends(verify_jwt_token)):

    return current_user

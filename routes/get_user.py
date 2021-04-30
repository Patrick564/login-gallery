from fastapi import APIRouter, Depends

from services.jwt import verify_jwt_token

from db.schemas import User


router = APIRouter()


@router.get('')
async def get_user(current_user: User = Depends(verify_jwt_token)):

    return current_user

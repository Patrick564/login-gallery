from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def logout():
    return {
        "logout": True
    }

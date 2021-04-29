from fastapi.utils import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    is_active: bool = True
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

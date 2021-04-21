from fastapi.utils import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    password: str
    active: Optional[bool] = True

    class Config:
        orm_mode = True

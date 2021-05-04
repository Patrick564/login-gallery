from fastapi import Form
from fastapi.utils import Optional


class UserData:
    def __init__(
        self,
        username: str = Form(...),
        email: Optional[str] = Form(None),
        password: str = Form(...),
        is_active: bool = Form(...),
    ):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active

    def update_password(self, hashed_password):
        self.password = hashed_password

    def to_dict(self):
        return self.__dict__
